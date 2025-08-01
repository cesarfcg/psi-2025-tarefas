# Generated by Django 5.2.1 on 2025-07-31 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('concluído', 'Concluído'), ('cancelado', 'Cancelado')], default='Pendente', max_length=50)),
                ('prazo', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
