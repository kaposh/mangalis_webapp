# Generated by Django 2.0.6 on 2018-09-18 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Meno kategorie', max_length=200, verbose_name='Meno kategorie')),
                ('description', models.CharField(help_text='Popis kategorie', max_length=400, verbose_name='Popis kategorie')),
            ],
        ),
        migrations.CreateModel(
            name='Souvenir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Typ suveniru', max_length=200, verbose_name='Typ suveniru')),
                ('description', models.CharField(help_text='Popis suveniru', max_length=400, verbose_name='Popis suveniru')),
                ('image', models.ImageField(help_text='Obrazok suveniru', upload_to='souvenirs_pictures/', verbose_name='Obrazok suveniru')),
                ('available', models.BooleanField(default=True, help_text='Dostupnost suveniru', verbose_name='Dostupnost suveniru')),
                ('pieces', models.IntegerField(default=0, help_text='Pocet na sklade', verbose_name='Pocet')),
                ('kategoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Kategoria')),
            ],
        ),
    ]
