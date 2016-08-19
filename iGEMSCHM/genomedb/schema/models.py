from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Species(models.Model):
    key = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    
class Accession(models.Model):
    assembly_key = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    species_key = models.CharField(max_length=200)
 
class Gene(models.Model):
    key = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    species_key = models.CharField(max_length=200)
    accession_key = models.CharField(max_length=200)
    strand = models.IntegerField()
    start = models.IntegerField()
    stop = models.IntegerField()
    genebank_annotation = models.CharField(max_length=200)
    cluster_information = models.CharField(max_length=200)
    operon_key = models.CharField(max_length=200)
    gene_order = models.IntegerField()
    
class Operon_Database(models.Model):
    key = models.CharField(max_length=200)
    
    kegg_orthology_ID = models.CharField(max_length=200)
    
    species_key = models.CharField(max_length=200)
    
    operon_name = models.CharField(max_length=200)
    
    annotation = models.CharField(max_length=200)

class HMM_Output(models.Model):
    key = models.CharField(max_length=200)
    
    accession_key = models.CharField(max_length=200)
    
    species_key = models.CharField(max_length=200)
    
    start = models.IntegerField()
    
    end = models.IntegerField()
    
    hmm_profile_key = models.CharField(max_length=200)

class HMM_Profile(models.Model):
    key = models.CharField(max_length=200)
    
    name = models.CharField(max_length=200)
    
