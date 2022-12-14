# Generated by Django 2.2.12 on 2022-08-23 18:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djelatnik',
            name='OIB',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10000000000), django.core.validators.MaxValueValidator(99999999999)]),
        ),
        migrations.AlterField(
            model_name='djelatnik',
            name='titula',
            field=models.CharField(choices=[('PR', 'Profesor'), ('AS', 'Asistent')], max_length=100),
        ),
        migrations.AlterField(
            model_name='prostorija',
            name='Broj_prostorije',
            field=models.CharField(max_length=100),
        ),
    ]
