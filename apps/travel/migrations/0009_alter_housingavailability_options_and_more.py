# Generated by Django 4.2.3 on 2023-09-09 07:53

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0008_alter_housingavailability_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='housingavailability',
            options={'verbose_name': 'Календарь', 'verbose_name_plural': 'Календари'},
        ),
        migrations.AlterField(
            model_name='housingreservation',
            name='check_in_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 9, 9))], verbose_name='Заезд'),
        ),
        migrations.AlterField(
            model_name='housingreservation',
            name='check_out_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2023, 9, 9))], verbose_name='Выезд'),
        ),
        migrations.AlterField(
            model_name='housingreservation',
            name='username',
            field=models.CharField(max_length=155, verbose_name='Имя клиента'),
        ),
        migrations.AlterUniqueTogether(
            name='housingavailability',
            unique_together={('rooms', 'date')},
        ),
    ]
