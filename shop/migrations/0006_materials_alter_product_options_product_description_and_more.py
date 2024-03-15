# Generated by Django 5.0.2 on 2024-03-15 15:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0005_remove_product_image_productimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Materials",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Material",
                "verbose_name_plural": "Materials",
                "ordering": ["id"],
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["id"],
                "verbose_name": "Product",
                "verbose_name_plural": "Products",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="size",
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="productimage",
            name="product",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_images",
                to="shop.product",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="fabric",
            field=models.ManyToManyField(to="shop.materials"),
        ),
    ]