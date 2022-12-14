# Generated by Django 4.0.4 on 2022-09-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidsaverr2app', '0004_remove_covidappuser_year_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='appuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('vakciniran', models.BooleanField(default=False)),
                ('prelezankovid', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='covidappuser',
            name='tel_no',
        ),
    ]
