from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import gettext as _

from utils.models_utils import model_image_directory_path, model_supplier_directory_path


class CustomUserManager(BaseUserManager):
    """
    Custom userss model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, phone="", **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_staff(self, email, password, phone="", **extra_fields):
        """
          Create and save a Staff with the given email and password.
          """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Admin userss must have is_staff=True.')
        return self.create_user(email, password, phone, **extra_fields)

    def create_supplier(self, email, password, phone="", **extra_fields):
        """
          Create and save a Supplier with the given email and password.
          """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Admin userss must have is_staff=True.')
        return self.create_user(email, password, phone, **extra_fields)

    def create_superuser(self, email, password, phone="", **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, phone, **extra_fields)


class OurUser(AbstractUser):  #### ADD REGEX (PHONE NUMBER / MAX_LENGHTH) ####
    username = models.CharField(max_length=50, default="defult")
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    first_name = models.CharField(_("نام"), max_length=250, blank=True, null=True)
    last_name = models.CharField(_("نام خانوادگی"), max_length=250, blank=True, null=True)
    age = models.IntegerField(_("سن"), blank=True, null=True)
    avatar = models.ImageField(upload_to=model_supplier_directory_path, blank=True,
                               null=True)  ### esmesh ro be AVATAR taghir bde
    address = models.CharField(_("نشانی"), max_length=500, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'karbaran'
        verbose_name_plural = 'karbaran'

    def __str__(self):
        return self.email


class BaseUers(models.Model):
    user = models.OneToOneField(OurUser, on_delete=models.CASCADE, verbose_name="کاربر")
    wallet_id = models.BigAutoField()

    class Meta:
        abstract = True


class Regular(OurUser):
    GENDER_CHICES = (("مرد", "man"), ("زن", "woman"), ("دیگر", "other"),)

    code_meli = models.IntegerField(_("کدملی"))
    gender = models.CharField(_("جنسیت"), max_length=5, choices=GENDER_CHICES)

    class Meta:
        verbose_name = 'Regular'
        verbose_name_plural = 'Regular'

    def save(self, *args, **kwargs):
        if len(str(self.code_meli)) != 10:
            raise Exception("کد ملی باید ده رقم باشد")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email}"


class Staff(OurUser):
    staff_number = models.IntegerField(_("کد کارمندی"))
    staff_duty = models.CharField(_("مقام"), max_length=50)

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

    def save(self, *args, **kwargs):
        if not self.staff_number > 0:
            raise Exception("کد کارمندی را به صورت صحیح وارد کنید")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.staff_duty}"


class Supplier(OurUser):
    company_name = models.CharField(max_length=200, default="فروشنده حقوقی")
    open_working_hour = models.TimeField("زمان شروع کار در روز")
    close_working_hour = models.TimeField("زمان پایان کار در روز")
    excel_file = models.FileField("فایل اکسل محصولات خود را در اینجا باز گذاری کنید ",
                                  name="EXCEL", upload_to=model_supplier_directory_path, null=True, blank=True)
    bank_shaba = models.IntegerField(_("شماره شبا کارت بانکی خود را وارد کنید"))

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Supplier'

    def save(self, *args, **kwargs):
        if len(str(self.bank_shaba)) != 10:
            raise Exception("کد شبا بایستی 10 رقم داشته باشد", len(str(self.bank_shaba)))
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email}, {self.company_name}"
