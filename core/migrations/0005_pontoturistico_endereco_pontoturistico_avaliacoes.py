# Generated by Django 4.0.4 on 2022-05-04 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localizacao', '0001_initial'),
        ('avaliacoes', '0001_initial'),
        ('core', '0004_pontoturistico_comentarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='Endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='localizacao.endereco'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.avaliacao'),
        ),
    ]
