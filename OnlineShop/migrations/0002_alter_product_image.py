# Generated by Django 4.1.5 on 2023-02-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnlineShop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/img/'),
        ),
    ]
