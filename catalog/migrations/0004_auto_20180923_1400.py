# Generated by Django 2.0.6 on 2018-09-23 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20180919_1934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategoria',
            options={'ordering': ('name',), 'verbose_name': 'Kategória', 'verbose_name_plural': 'Kategórie'},
        ),
        migrations.AddField(
            model_name='kategoria',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='souvenir',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
