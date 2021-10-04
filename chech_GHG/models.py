import time

from django.core.validators import validate_image_file_extension
from django.db import models

from utils.models_utils import model_image_directory_path


class AboutUs(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    text = models.TextField()
    imgae = models.ImageField(upload_to=model_image_directory_path, null=True, blank=True,

                                      validators=[validate_image_file_extension], default=None, )


class Timesheet(models.Model):
    day = models.CharField(max_length=50)
    start = models.TimeField()
    end = models.TimeField()

