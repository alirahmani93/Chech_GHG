# Generated by Django 3.2.7 on 2021-09-04 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_catalog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catalog',
            field=models.FileField(default=None, upload_to='', verbose_name='کاتالوگ'),
        ),
    ]
