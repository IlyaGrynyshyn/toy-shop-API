# Generated by Django 5.0.2 on 2024-03-26 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0010_alter_product_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.IntegerField(),
        ),
    ]
