# Generated by Django 4.1.2 on 2024-01-08 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount_paid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
