# Generated by Django 4.1.5 on 2023-02-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineShop', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]
