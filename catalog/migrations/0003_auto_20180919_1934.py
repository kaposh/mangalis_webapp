# Generated by Django 2.0.6 on 2018-09-19 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_souvenir_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='souvenir',
            name='code',
            field=models.CharField(help_text='Kód suveníru', max_length=30, null=True, verbose_name='Kód suveniru'),
        ),
        migrations.AlterField(
            model_name='souvenir',
            name='available',
            field=models.BooleanField(default=True, help_text='Dostupnosť suveníru', verbose_name='Dostupnosť suveníru'),
        ),
        migrations.AlterField(
            model_name='souvenir',
            name='description',
            field=models.CharField(help_text='Popis suveníru', max_length=400, verbose_name='Popis suveníru'),
        ),
        migrations.AlterField(
            model_name='souvenir',
            name='image',
            field=models.ImageField(help_text='Obrázok suveníru', upload_to='souvenirs_pictures/', verbose_name='Obrázok suveníru'),
        ),
        migrations.AlterField(
            model_name='souvenir',
            name='name',
            field=models.CharField(help_text='Typ suveníru', max_length=200, verbose_name='Typ suveníru'),
        ),
        migrations.AlterField(
            model_name='souvenir',
            name='pieces',
            field=models.IntegerField(default=0, help_text='Počet na sklade', verbose_name='Počet'),
        ),
    ]