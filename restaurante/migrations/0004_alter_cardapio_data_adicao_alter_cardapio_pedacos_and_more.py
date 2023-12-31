# Generated by Django 4.2.6 on 2023-10-20 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0003_rename_serve_pessoas_cardapio_pedacos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardapio',
            name='data_adicao',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 20, 15, 23, 28, 195018)),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='pedacos',
            field=models.IntegerField(default=8, verbose_name='Pedaços'),
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Preço'),
        ),
    ]
