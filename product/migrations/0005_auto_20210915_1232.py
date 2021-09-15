# Generated by Django 3.2.7 on 2021-09-15 12:32

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import utils.models_utils


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210904_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discription',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='media',
            name='slug',
        ),
        migrations.AddField(
            model_name='product',
            name='is_acrive',
            field=models.BooleanField(default=False, verbose_name='فعال/غیرفعال'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='image_product',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=utils.models_utils.model_image_directory_path, validators=[django.core.validators.validate_image_file_extension]),
        ),
        migrations.AlterField(
            model_name='media',
            name='video_product',
            field=models.FileField(blank=True, default=None, null=True, upload_to=utils.models_utils.model_image_directory_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='catalog',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='کاتالوگ'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('N', 'Not_Exist'), ('A', 'Active'), ('W', 'Will_not_be_produced'), ('O', 'Ordered')], default='N', max_length=1, verbose_name='وضعیت موجودی'),
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('numeric_value', models.IntegerField(blank=True, null=True)),
                ('string_value', models.CharField(blank=True, max_length=200, null=True)),
                ('att_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.attribute')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='filed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.attribute', verbose_name='فیلد اضافی'),
        ),
    ]
