# Generated by Django 5.0.4 on 2024-04-17 23:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidade', models.CharField(max_length=100)),
                ('icone', models.ImageField(blank=True, null=True, upload_to='icones')),
            ],
        ),
        migrations.CreateModel(
            name='DadosMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.CharField(max_length=30)),
                ('nome', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=15)),
                ('rua', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('rg', models.ImageField(upload_to='rgs')),
                ('cedula_identidade_medica', models.ImageField(upload_to='cim')),
                ('foto', models.ImageField(upload_to='fotos_perfil')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('valor_consulta', models.FloatField(default=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('especialidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='medico.especialidades')),
            ],
        ),
    ]
