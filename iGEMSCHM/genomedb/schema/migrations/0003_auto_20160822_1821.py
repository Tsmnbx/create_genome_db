# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-22 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0002_auto_20160819_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accession',
            name='assembly_key',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='accession',
            name='species_key',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='accession_key',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='key',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='operon_key',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='gene',
            name='species_key',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='hmm_output',
            name='accession_key',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='hmm_output',
            name='key',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='hmm_output',
            name='species_key',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='hmm_profile',
            name='key',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='operon_database',
            name='kegg_orthology_ID',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='operon_database',
            name='key',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='operon_database',
            name='species_key',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='species',
            name='key',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
