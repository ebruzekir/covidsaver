# Generated by Django 4.0.4 on 2022-08-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covidappUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('year_of_birth', models.IntegerField()),
                ('tel_no', models.IntegerField()),
                ('ezbo', models.CharField(max_length=50)),
                ('grad', models.CharField(choices=[('ohrid', 'OHRID'), ('struga', 'STRUGA'), ('skopje', 'SKOPJE'), ('tetovo', 'TETOVO'), ('prilep', 'PRILEP'), ('veles', 'VELES'), ('kavadarci', 'KAVADARCI'), ('negotino', 'NEGOTINO'), ('stip', 'STIP'), ('berovo', 'BEROVO'), ('debar', 'KICEVO'), ('bitola', 'BITOLA')], default='ohrid', max_length=20)),
                ('password1', models.CharField(max_length=50)),
                ('kategorija', models.CharField(choices=[('restaurant', 'Restaurant'), ('coffeeShop', 'CoffeeShop')], default='restaurant', max_length=20)),
                ('podkategorija_ohrid', models.CharField(choices=[('tino', 'TINO'), ('porta', 'PORTA'), ('kadmo', 'KADMO')], default='porta', max_length=20)),
                ('podkategorija_struga', models.CharField(choices=[('relax', 'Relax'), ('adenia', 'Adenia')], default='relax', max_length=20)),
                ('podkategorija_skopje', models.CharField(choices=[('joy', 'Joy'), ('destan', 'Destan')], default='restaurant', max_length=20)),
                ('vakciniran', models.BooleanField(default=False)),
                ('prelezankovid', models.BooleanField()),
                ('prelezankovid14dena', models.BooleanField()),
                ('vkupno', models.IntegerField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='cover_images/')),
            ],
        ),
    ]
