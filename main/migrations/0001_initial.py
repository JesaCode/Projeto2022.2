# Generated by Django 4.1.1 on 2022-10-03 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Troca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('darFigurinhas', models.CharField(max_length=50)),
                ('recebeFigurinhas', models.CharField(max_length=10)),
                ('valor', models.FloatField(max_length=10)),
                ('descricao', models.CharField(max_length=165)),
                ('ativa', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Figurinha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6)),
                ('nomeFigurinha', models.CharField(max_length=50)),
                ('tipoFigurinha', models.CharField(max_length=10)),
                ('trocasFigurinha', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.troca')),
            ],
        ),
    ]
