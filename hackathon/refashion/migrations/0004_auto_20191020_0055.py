# Generated by Django 2.2.6 on 2019-10-20 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refashion', '0003_auto_20191019_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_number',
            field=models.PositiveSmallIntegerField(default=17180),
        ),
    ]