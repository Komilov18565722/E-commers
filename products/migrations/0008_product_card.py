# Generated by Django 4.1.2 on 2022-10-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_photo1_alter_product_photo2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='card',
            field=models.BooleanField(default=0),
        ),
    ]