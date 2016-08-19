from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Species(models.Model):
    key = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    
class Accession(models.Model):
    key_assembly = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    species_key = Species.key.filter(max_length=200)
 
    
