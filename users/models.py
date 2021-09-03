from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import gettext as _

from utils.models_utils import model_image_directory_path


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


class OurUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    first_name = models.CharField(_("نام"), max_length=250)
    last_name = models.CharField(_("نام خانوادگی"), max_length=250)
    age = models.IntegerField(_("سن"))
    # wallet= models.OneToOneField("کیف پول داخلی کاربر","wallet", on_delete=models.PROTECT)
    image = models.ImageField(upload_to=model_image_directory_path)
    address = models.CharField(_("نشانی"), max_length=500)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):      return self.email

    class Meta:
        verbose_name = 'karbaran'
        verbose_name_plural = 'karbaran'


class Regular(OurUser):
    pass



class Staff(OurUser):
    pass



class Supplier(OurUser):
    open_working_hour = models.TimeField("زمان شروع کار در روز")
    close_working_hour = models.TimeField("زمان پایان کار در روز")

