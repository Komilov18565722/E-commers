# Generated by Django 4.1.2 on 2022-10-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo1',
            field=models.ImageField(upload_to='media/img/product-img/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/product-img/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/product-img/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/product-img/%Y/%m/%d'),
        ),
    ]