from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Species(models.Model):
    key = models.CharField(max_length=200, unique=True) #SpeciesKey 1111111
    name = models.CharField(max_length=200)
    
class Accession(models.Model):
    assembly_key = models.CharField(max_length=200, unique=True) #AssemblyName 222222
    name = models.CharField(max_length=200)
    species_key = models.CharField(max_length=200, unique=True) #SpeciesKey 1111111
 
class Gene(models.Model):
    key = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    # make into species pointer?
    species_key = models.CharField(max_length=200, unique=True) #SpeciesKey 1111111
    # make into accession pointer?
    accession_key = models.CharField(max_length=200, unique=True) #AssemblyName 22222
    strand = models.CharField(max_length=200)
    start = models.IntegerField()
    stop = models.IntegerField()
    genebank_annotation = models.CharField(max_length=200)
    cluster_information = models.CharField(max_length=200, null=True)
    # make into operon pointer?
    operon_key = models.CharField(max_length=200, unique=True) # Operon key 333333333
    gene_order = models.IntegerField()
    
class Operon_Database(models.Model):
    key = models.CharField(max_length=200, unique=True)  # Operon key 3333333333
    operon_name = models.CharField(max_length=200)
    kegg_orthology_ID = models.CharField(max_length=200, unique=True)
    # make into species pointer?
    species_key = models.CharField(max_length=200, unique=True) #SpeciesKey 1111111
    annotation = models.CharField(max_length=200)

class HMM_Output(models.Model):
    key = models.CharField(max_length=200, unique=True)
    # make into accession pointer?
    accession_key = models.CharField(max_length=200, unique=True) #AssemblyName 222222
    # make into species pointer?
    species_key = models.CharField(max_length=200, unique=True) #SpeciesKey 1111111
    start = models.IntegerField()
    end = models.IntegerField()
    # make into hmm_profile?
    hmm_profile_key = models.CharField(max_length=200, unique=True) #HMM PROFILE KEY 4444444

class HMM_Profile(models.Model):
    key = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    
