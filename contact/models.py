from django.db import models

# Create your models here.
class Firma(models.Model):
    meno_firmy = models.CharField(max_length=20, verbose_name= "menoFirmy", help_text="Nazov firmy", default="")
    konatel = models.CharField(max_length=40, verbose_name= "Konatel", help_text="Konatel", default="")
    konatel1 = models.CharField(max_length=40, verbose_name= "Konatel Alt", help_text="Konatel Alt", default="")
    adresa1 = models.CharField(max_length=40, verbose_name= "Adresa1", help_text="Adresa1", default="")
    adresa2 = models.CharField(max_length=40, verbose_name= "Adresa2", help_text="Adresa2", default="")
    psc = models.CharField(max_length=40, verbose_name= "PSC", help_text="PSC", default="")
    krajina = models.CharField(max_length=40, verbose_name="krajina", help_text="krajina", default="")
    telefon = models.CharField(max_length=40, verbose_name="telefon", help_text="telefon", default="")
    telefon1 = models.CharField(max_length=40, verbose_name="telefon1", help_text="telefon1", default="")
    email = models.EmailField( verbose_name="email", help_text="email")
    def __str__(self):
        return self.meno_firmy
