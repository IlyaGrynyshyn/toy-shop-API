# Generated by Django 5.0.2 on 2024-03-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_materials_alter_product_options_product_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]