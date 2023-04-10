# Generated by Django 4.1.3 on 2023-04-04 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='home.brand'),
            preserve_default=False,
        ),
    ]