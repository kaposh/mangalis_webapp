# Generated by Django 2.0.6 on 2018-09-19 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='souvenir',
            name='slug',
            field=models.SlugField(max_length=40, null=True, unique=True),
        ),
    ]
