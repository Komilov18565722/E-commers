# Generated by Django 4.1.2 on 2022-10-08 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo1',
            field=models.ImageField(upload_to='media/img/product-img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/product-img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/product-img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/product-img'),
        ),
    ]
