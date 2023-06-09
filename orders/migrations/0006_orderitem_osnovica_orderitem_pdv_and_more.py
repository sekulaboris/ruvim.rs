# Generated by Django 4.1.5 on 2023-05-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_company_alter_order_m_broj_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='osnovica',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=10),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='pdv',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=10),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=10),
        ),
    ]
