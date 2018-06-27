from django.db import models

# Create your models here.
class Souvenir(models.Model):
    name = models.CharField(max_length=200, verbose_name= "Typ suveniru", help_text="Typ suveniru")
    description = models.CharField(max_length=400, verbose_name= "Popis suveniru", help_text="Popis suveniru")
    image = models.ImageField(upload_to='souvenirs_pictures/', verbose_name= "Obrazok suveniru", help_text="Obrazok suveniru")
    available = models.BooleanField(default=True,verbose_name= "Dostupnost suveniru", help_text="Dostupnost suveniru")
    pieces = models.IntegerField(verbose_name= "Pocet", help_text="Pocet na sklade", default=0)
    def __str__(self):
        return self.name
