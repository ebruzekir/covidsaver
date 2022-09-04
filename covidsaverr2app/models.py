from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
kategorija_choices = (
    ('restaurant', 'Restaurant'),
    ('coffeeShop', 'CoffeeShop')
)
pod_kategorija_choices_ohrid = (
    ('tino', 'TINO'),
    ('porta', 'PORTA'),
    ('kadmo', 'KADMO'),

)
pod_kategorija_choices_struga = (
    ('relax', 'Relax'),
    ('adenia', 'Adenia')
)
pod_kategorija_choices_Skopje = (
    ('1', 'Joy'),
    ('1', 'Destan')
)
grad_choices = (
    ('ohrid', 'OHRID'),
    ('struga', 'STRUGA'),
    ('skopje', 'SKOPJE'),
    ('tetovo', 'TETOVO'),
    ('prilep', 'PRILEP'),
    ('veles', 'VELES'),
    ('kavadarci', 'KAVADARCI'),
    ('negotino', 'NEGOTINO'),
    ('stip', 'STIP'),
    ('berovo', 'BEROVO'),
    ('debar', 'KICEVO'),
    ('bitola', 'BITOLA')
)
class appuser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    vakciniran = models.BooleanField(default=False)
    prelezankovid = models.BooleanField()
class covidappUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


    username = models.CharField(max_length=50)
    grad = models.CharField(max_length=20, choices=grad_choices, default='ohrid')
    password1 = models.CharField(max_length=50)
    kategorija = models.CharField(max_length=20, choices=kategorija_choices, default='restaurant')
    podkategorija_ohrid = models.CharField(max_length=20, choices=pod_kategorija_choices_ohrid, default='porta')
    podkategorija_struga = models.CharField(max_length=20, choices=pod_kategorija_choices_struga, default='relax')
    podkategorija_skopje = models.CharField(max_length=20, choices=pod_kategorija_choices_Skopje, default='restaurant')
    vakciniran = models.BooleanField(default=False)
    prelezankovid = models.BooleanField()
    prelezankovid14dena = models.BooleanField()
    vkupno = models.IntegerField()
    cover_image = models.ImageField(upload_to="cover_images/", null=True, blank=True)
    # not USERNAME_FIELD = username
    USERNAME_FIELD = 'ezbo'
    set_password = 'password'


def __str__(self):
    return self.ezbo


class Grad(models.Model):
    name = models.CharField(max_length=40)

    # grad = models.CharField(max_length=50, choices=grad_choices)
    # id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.name


class Restoran(models.Model):
    grad = models.ForeignKey(Grad, on_delete=models.SET_NULL, blank=True, null=True)
    # id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    ime = models.CharField(max_length=50)
    grad = models.ForeignKey(Grad, on_delete=models.SET_NULL, blank=True, null=True)
    restoran = models.ForeignKey(Restoran, on_delete=models.SET_NULL, blank=True, null=True)



    def __str__(self):
        return self.name
