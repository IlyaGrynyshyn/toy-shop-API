# Generated by Django 5.0.2 on 2024-04-11 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0003_order_delivery_city_order_delivery_warehouse"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="track_number",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
