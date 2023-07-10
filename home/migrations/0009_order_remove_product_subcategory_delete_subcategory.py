# Generated by Django 4.2.3 on 2023-07-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0008_wishlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("username", models.CharField(max_length=300)),
                ("fname", models.CharField(max_length=300)),
                ("lname", models.CharField(max_length=300)),
                ("email", models.EmailField(max_length=300)),
                ("phone", models.CharField(max_length=300)),
                ("address", models.TextField()),
                ("city", models.CharField(max_length=300)),
                ("state", models.CharField(max_length=300)),
                ("country", models.CharField(max_length=300)),
                ("pincode", models.CharField(max_length=300)),
                ("total_price", models.FloatField()),
                ("payment_mode", models.CharField(max_length=300)),
                ("payment_id", models.CharField(max_length=300, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Out for Shipping", "Out for Shipping"),
                            ("Completed", "Completed"),
                        ],
                        default="Pending",
                        max_length=300,
                    ),
                ),
                ("message", models.TextField(null=True)),
                ("tracking_no", models.CharField(max_length=300, null=True)),
                ("created_at", models.DateTimeField()),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="product",
            name="subcategory",
        ),
        migrations.DeleteModel(
            name="SubCategory",
        ),
    ]
