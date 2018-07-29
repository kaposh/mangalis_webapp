from django.db import models

# Create your models here.
class Firma(models.Model):
    meno_firmy = models.CharField(max_length=20, verbose_name= "menoFirmy", help_text="Nazov firmy")
    konatel = models.CharField(max_length=40, verbose_name= "Konatel", help_text="Konatel")
    adresa1 = models.CharField(max_length=40, verbose_name= "Adresa1", help_text="Adresa1")
    adresa2 = models.CharField(max_length=40, verbose_name= "Adresa2", help_text="Adresa2")
    psc = models.CharField(max_length=40, verbose_name= "PSC", help_text="PSC")
    krajina = models.CharField(max_length=40, verbose_name="krajina", help_text="krajina")
    telefon = models.CharField(max_length=40, verbose_name="telefon", help_text="telefon")
    email = models.EmailField( verbose_name="email", help_text="email")
    def __str__(self):
        return self.meno_firmy
