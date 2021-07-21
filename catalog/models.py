from django.db import models
from django.urls import reverse

# Create your models here.
class Kategoria(models.Model):
    name = models.CharField(max_length=200, verbose_name="Meno kategorie", help_text="Meno kategorie")
    slug = models.SlugField(max_length=200, unique=True, db_index=True,null=True)
    description = models.CharField(max_length=400, verbose_name="Popis kategorie", help_text="Popis kategorie")
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:catalog-kategoria', args=[self.slug])

    class Meta:
        ordering=('name',)
        verbose_name='Kategória'
        verbose_name_plural='Kategórie'


class Souvenir(models.Model):
    name = models.CharField(max_length=200, verbose_name= "Typ suveníru", help_text="Typ suveníru")
    slug = models.SlugField(max_length=200, unique=True, db_index=True,null=True)
    description = models.CharField(max_length=400, verbose_name= "Popis suveníru", help_text="Popis suveníru")
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=30, verbose_name= "Kód suveniru", help_text="Kód suveníru", null=True)
    image = models.ImageField(upload_to='souvenirs_pictures/', verbose_name= "Obrázok suveníru", help_text="Obrázok suveníru")
    available = models.BooleanField(default=True,verbose_name= "Dostupnosť suveníru", help_text="Dostupnosť suveníru")
    pieces = models.IntegerField(verbose_name= "Počet", help_text="Počet na sklade", default=0)

    class Meta:
        ordering=('name',)
        verbose_name='Suvenír'
        verbose_name_plural='Suveníry'
        index_together=(('id', 'slug'))
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:catalog-detail', args=[self.slug,self.id])

