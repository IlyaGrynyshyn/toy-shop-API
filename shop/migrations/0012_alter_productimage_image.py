# Generated by Django 5.0.2 on 2024-03-26 20:25

import shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0011_alter_product_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productimage",
            name="image",
            field=models.ImageField(
                blank=True,
                max_length=255,
                null=True,
                upload_to=shop.models.product_image_file_path,
            ),
        ),
    ]