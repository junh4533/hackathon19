# Generated by Django 2.2.6 on 2019-10-20 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refashion', '0002_auto_20191019_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_number',
            field=models.PositiveSmallIntegerField(default=98507),
        ),
        migrations.AlterField(
            model_name='redemption',
            name='coupon_code',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
