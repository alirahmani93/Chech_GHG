import re
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_image_file_extension

from users.models import OurUser, Supplier, Regular
from utils.models_utils import model_image_directory_path

# Create your models here.
User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name="دسته")
    sub_category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, blank=True,
                                     verbose_name="زیر مجموعه")

    class Meta:
        verbose_name = "دسته بندی ها"
        verbose_name_plural = "گروه بندی"

    def __str__(self):
        return f"{self.title},{self.id}"


class Brand(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30, blank=True, null=True, verbose_name="کشور دفتر مرکزی")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name="شهر دفتر مرکزی")
    phone_number = models.IntegerField(blank=True, null=True, verbose_name="تلفن دفتر مرکزی")
    email = models.EmailField(blank=True, null=True, verbose_name="ایمیل دفتر مرکزی")

    def __str__(self):
        return f"{self.name}"


class Media(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="media")
    image_product = models.ImageField(upload_to=model_image_directory_path, null=True, blank=True,
                                      validators=[validate_image_file_extension], default=None, )
    video_product = models.FileField(upload_to=model_image_directory_path, null=True, blank=True, default=None)
    description = models.CharField(max_length=100, default=None)

    def __str__(self):
        return f'{self.description}'


class Attributekey(models.Model):
    att_fk = models.ForeignKey("Attributekey", on_delete=models.CASCADE, related_name="attkey", null=True, blank=True)
    title = models.CharField(max_length=50, null=True, blank=True, default=None)
    unit = models.CharField(max_length=50, unique=True, null=True, blank=True, default=None)
    is_numeric = models.BooleanField()
    is_float = models.BooleanField()
    is_string = models.BooleanField()
    is_time = models.BooleanField()
    is_datetime = models.BooleanField()

    @property
    def find_type(self):
        if self.is_time:
            return self.is_time
        elif self.is_datetime:
            return self.is_datetime
        elif self.is_string:
            return type(str)
        elif self.is_float:
            return self.is_float
        elif self.is_numeric:
            return self.is_numeric
        return False

    # def save(self, *args, **kwargs):
    #     KEYS = [self.is_time, self.is_datetime, self.is_string, self.is_float, self.is_numeric]
    #     x = 0
    #     print(KEYS)
    #     for key in KEYS:
    #         # print(key, self.find_type)
    #         print(key.__class__.__name__)
    #         if self.find_type == key.__class__.__name__:
    #             x += 1
    #             print(x, key)
    #             return super().save(self, *args, **kwargs)
    #
    #     if x != 1: raise ValueError("bish az do mord entehkhb kardi")



    def __str__(self):
        return f"{self.title}"


class Attribute(models.Model):
    attrs = models.ForeignKey("Attributekey", on_delete=models.CASCADE, related_name="attrval", null=True, blank=True)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="attrproduct", null=True, blank=True)
    numeric_value = models.IntegerField(null=True, blank=True)
    float_value = models.FloatField(null=True, blank=True)
    string_value = models.CharField(max_length=200, null=True, blank=True)
    datetime_value = models.DateTimeField(null=True, blank=True)
    time_value = models.TimeField(null=True, blank=True)

    def save(self, *args, **kwargs): #TODO Eshtebah save mishe
        """
        print(bool(self.numeric_value),self.attrs.find_type)
        print(bool(self.float_value),self.attrs.find_type)
        y= self.attrs.find_type.__class__
        x=0
        if  self.numeric_value.__class__ == y and not None : x =+1
        elif self.float_value.__class__ == y and not None : x =+1
        elif self.string_value.__class__ == y and not None : x =+1
        elif self.datetime_value.__class__ == y and not None :  x =+1
        elif self.time_value.__class__ == y and not None : x =+1
        print(x,y,self.string_value.__class__)
        """
        return super().save(self, *args, **kwargs)

    @property
    def find_val(self):
        val = None
        if self.attrs.is_time:
            val = self.time_value
        elif self.attrs.is_datetime:
            val = self.datetime_value
        elif self.attrs.is_string:
            val = self.string_value
        elif self.attrs.is_float:
            val = self.float_value
        elif self.attrs.is_numeric:
            val = self.numeric_value
        return val

    def __str__(self):
        return f"{self.attrs.title} , {self.find_val}"


class Product(models.Model):
    Not_Exist, Active, Will_not_be_produced, Ordered = "N", "A", "W", "O"
    status_choices = [("N", "Not_Exist"), ("A", "Active"), ("W", "Will_not_be_produced"), ("O", "Ordered")]

    ### FK ###
    supplier = models.ForeignKey(to=Supplier, on_delete=models.RESTRICT, null=True, blank=True)
    filed = models.ManyToManyField("Attributekey", through=Attribute, blank=True, verbose_name="Extra Filed")
    cat = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey("Brand", on_delete=models.SET_NULL, null=True, blank=True)
    #### Product ####
    name = models.CharField(max_length=50, )
    slug = models.SlugField(unique=True, null=True, blank=True, allow_unicode=True)
    count = models.IntegerField("تعداد", default=0)
    status = models.CharField("وضعیت موجودی", choices=status_choices, max_length=1, default="N")
    size = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField("توضیحات اضافی", max_length=30, null=True, blank=True)
    upc = models.PositiveBigIntegerField(null=True, blank=True, help_text="بارکد ۱۲ رقمی")
    catalog = models.FileField("کاتالوگ", upload_to="", null=True, blank=True)  ### How to connerct CDN?? #TODO
    is_archive = models.BooleanField("فعال/غیرفعال", default=False)

    ## Price ###  set Temp price for this product (( if (end - start) > (end - now) ==> cost = temporary_price
    price = models.FloatField(default=0, help_text="﷼")  # ex:10 000
    set_time = models.DateTimeField(auto_now_add=True)  # ex: 1400/06/10
    ## set Temp and start & end date
    date_start = models.DateTimeField("زمان شروع تخفیف", null=True, blank=True)  # ex: 1400/06/12
    date_end = models.DateTimeField("زمان پایان تخفیف", null=True, blank=True)  # ex: 1400/06/14
    Temporary_price = models.FloatField(verbose_name="قیمت مموقت", null=True, blank=True)  # ex: 15 000
    cost = models.FloatField("قیمت محصول", null=True, blank=True)  # last Price

    @property
    def original_price(self):
        if self.date_start < timezone.now() < self.date_end:
            return True
        else:
            return False

    def save(self, force_insert=True, *args, **kwargs):
        if self.status == "N" and self.count > 0:
            raise Exception("تعداد کالا با وضعیت همخوانی ندارد ")
        if self.count < 0:
            raise Exception("تعداد کالا نمیتواند منفی باشد")
        if not self.date_start < self.date_end:
            raise Exception("تاریخ شروع از تاریخ پایان کمتر است ")

        if self.original_price:
            self.cost = 0
            self.cost = self.Temporary_price
        else:
            self.cost = 0
            self.cost = self.price

        if self.slug:
            slugify(self.slug, allow_unicode=True)
        return super().save()

    class Meta:
        verbose_name = "محصولات"
        verbose_name_plural = "محصولات"

    # def __str__(self):
    #     return f"{self.name}, {self.cost}, {self.id}"
