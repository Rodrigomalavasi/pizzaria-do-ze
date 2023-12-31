# Generated by Django 4.2.6 on 2023-10-20 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardapio',
            name='descricao',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='cardapio',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='cardapio',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='cardapio',
            name='preco',
            field=models.FloatField(default=0.0, verbose_name='Preço'),
        ),
        migrations.AddField(
            model_name='cardapio',
            name='serve_pessoas',
            field=models.IntegerField(default=8, verbose_name='Serve para quantas pessoas'),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='data_adicao',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 20, 14, 25, 18, 367851)),
        ),
    ]
