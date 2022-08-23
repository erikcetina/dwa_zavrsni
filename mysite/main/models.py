from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Djelatnik(models.Model):
    Ime = models.CharField(max_length=100)
    Prezime = models.CharField(max_length=100)
    OIB = models.IntegerField(validators=[MinValueValidator(10000000000), MaxValueValidator(99999999999)])
    email = models.EmailField(unique=True)
    titule_lista = [("PR","Profesor"), ("AS","Asistent")]
    titula = models.CharField(max_length=100, choices=titule_lista)

    def __str__(self):
        return self.Ime
    

class Prostorija(models.Model):
    Broj_prostorije = models.CharField(max_length=100)
    Kat = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(7)])

    def __str__(self):
        return self.Broj_prostorije
    
class Oprema(models.Model):
    Ime_opreme = models.CharField(max_length=100)
    Cijena_opreme = models.DecimalField(max_digits=10, decimal_places=2)
    Prostorija = models.ForeignKey(Prostorija, on_delete=models.CASCADE)

    def __str__(self):
        return self.Ime_opreme

class Rezervacija(models.Model):
    Djelatnik = models.ForeignKey(Djelatnik, on_delete=models.CASCADE)
    Oprema = models.ForeignKey(Oprema, on_delete=models.CASCADE)
    Prostorija = models.ForeignKey(Prostorija, on_delete=models.CASCADE)
    Razdoblje_od = models.DateField()
    Razdoblje_do = models.DateField()

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.Djelatnik, "rezervacija. Od", self.Razdoblje_od, "do", self.Razdoblje_do, ". Prostorija", self.Prostorija)