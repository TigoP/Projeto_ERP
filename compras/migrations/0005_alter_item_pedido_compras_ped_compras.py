# Generated by Django 5.1 on 2024-08-21 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_fornecedor_ie_fornecedor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_pedido_compras',
            name='ped_compras',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='compras.pedido_compras'),
        ),
    ]
