# Generated by Django 4.2.6 on 2023-10-20 18:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0002_cardapio_descricao_cardapio_foto_cardapio_nome_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardapio',
            old_name='serve_pessoas',
            new_name='pedacos',
        ),
        migrations.AlterField(
            model_name='cardapio',
            name='data_adicao',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 20, 15, 12, 29, 641168)),
        ),
    ]
