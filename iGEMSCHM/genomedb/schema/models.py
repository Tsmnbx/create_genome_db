from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Species(models.Model):
    key = models.CharField(max_length=200, unique=True) # SpeciesKey 1111111
    name = models.CharField(max_length=200)
    subspecies = models.CharField(max_length=200, null=True)
    strain = models.CharField(max_length=200, null=True)
    sub_strain = models.CharField(max_length=200, null=True)
    taxon = models.IntegerField() #ASK: integer or str?
    
class Accession(models.Model):
    key = models.CharField(max_length=200, unique=True) # AssemblyName 222222
    name = models.CharField(max_length=200)
    species_model = models.ForeignKey(Species, on_delete=models.CASCADE) #SpeciesKey 1111111
 
class Operon_Database(models.Model):
    key = models.CharField(max_length=200, unique=True) # Operon key 3333333333
    operon_name = models.CharField(max_length=200)
    kegg_orthology_ID = models.CharField(max_length=200, unique=True)
    species_model = models.ForeignKey(Species, on_delete=models.CASCADE) #SpeciesKey 1111111
    annotation = models.CharField(max_length=200)

class Gene(models.Model):
    key = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, null=True)
    gene_synonym = ArrayField(models.CharField(max_length=200), null=True)
    species_model = models.ForeignKey(Species, on_delete=models.CASCADE) #SpeciesKey 1111111
    accession_model = models.ForeignKey(Accession, null=True, on_delete=models.SET_NULL) #AssemblyName 22222
    strand = models.CharField(max_length=200, null=True)
    start = models.IntegerField()
    stop = models.IntegerField()
    genebank_annotation = models.CharField(max_length=200, null=True)
    cluster_information = models.CharField(max_length=200, null=True)
    operon_model = models.ForeignKey(Operon_Database, null=True, on_delete=models.SET_NULL)
    gene_order = models.IntegerField()
    protein_product = models.CharField(max_length=200, null=True)
    protein_id = models.CharField(max_length=200, null=True)
    function = models.CharField(max_length=200, null=True)
    note = models.CharField(max_length=200, null=True)
    uniprot = models.CharField(max_length=200, null=True, unique=True)
    gi = models.CharField(max_length=200, unique=True)
    EC_num = models.CharField(max_length=200, null=True, unique=True)
    locus_tag = models.CharField(max_length=200, unique=True)
    translation = models.CharField(max_length=200, unique=True)

class HMM_Profile(models.Model):
    key = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
        
class HMM_Output(models.Model):
    key = models.CharField(max_length=200, unique=True)
    accession_model = models.ForeignKey(Accession, on_delete=models.CASCADE) #AssemblyName 222222
    start = models.IntegerField()
    end = models.IntegerField()
    hmm_profile_key = models.ForeignKey(HMM_Profile, on_delete=models.CASCADE) #HMM PROFILE KEY 4444444


