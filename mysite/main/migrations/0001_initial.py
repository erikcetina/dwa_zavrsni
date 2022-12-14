# Generated by Django 2.2.12 on 2022-08-22 15:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Djelatnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ime', models.CharField(max_length=100)),
                ('Prezime', models.CharField(max_length=100)),
                ('OIB', models.IntegerField(validators=[django.core.validators.MinValueValidator(11), django.core.validators.MaxValueValidator(11)])),
                ('mail', models.EmailField(max_length=254)),
                ('titula', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Oprema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ime_opreme', models.CharField(max_length=100)),
                ('Cijena_opreme', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Prostorija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Broj_prostorije', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('Kat', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(7)])),
            ],
        ),
        migrations.CreateModel(
            name='Rezervacija',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Razdoblje_od', models.DateField()),
                ('Razdoblje_do', models.DateField()),
                ('Djelatnik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Djelatnik')),
                ('Oprema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Oprema')),
                ('Prostorija', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Prostorija')),
            ],
        ),
        migrations.AddField(
            model_name='oprema',
            name='Prostorija',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Prostorija'),
        ),
    ]
