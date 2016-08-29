from __future__ import unicode_literals
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Species(models.Model):
    key = models.CharField(max_length=200, unique=True, blank=True) # SpeciesKey 1111111
    name = models.CharField(max_length=200, blank=True)
    subspecies = models.CharField(max_length=200, blank=True)
    strain = models.CharField(max_length=200, blank=True)
    sub_strain = models.CharField(max_length=200, blank=True)
    taxon = models.IntegerField(null=True) #ASK: integer or str?
    
class Accession(models.Model):
    key = models.CharField(max_length=200, unique=True, blank=True) # AssemblyName 222222
    name = models.CharField(max_length=200, blank=True)
    species_model = models.ForeignKey(Species, null=True, on_delete=models.CASCADE) #SpeciesKey 1111111
 
class Operon_Database(models.Model):
    key = models.CharField(max_length=200, unique=True, blank=True) # Operon key 3333333333
    operon_name = models.CharField(max_length=200, blank=True)
    kegg_orthology_ID = models.CharField(max_length=200, unique=True, blank=True)
    species_model = models.ForeignKey(Species, null=True, on_delete=models.CASCADE) #SpeciesKey 1111111
    annotation = models.CharField(max_length=200, blank=True)

class Gene(models.Model):
    key = models.CharField(max_length=200, unique=True, blank=True)
    name = models.CharField(max_length=200, blank=True)
    gene_synonym = ArrayField(models.CharField(max_length=200, blank=True), null=True)
    species_model = models.ForeignKey(Species, null=True, on_delete=models.CASCADE) #SpeciesKey 1111111
    accession_model = models.ForeignKey(Accession, null=True, on_delete=models.SET_NULL) #AssemblyName 22222
    strand = models.CharField(max_length=200, blank=True)
    start = models.IntegerField(null=True)
    stop = models.IntegerField(null=True)
    genebank_annotation = models.CharField(max_length=200, blank=True)
    cluster_information = models.CharField(max_length=200, blank=True)
    operon_model = models.ForeignKey(Operon_Database, null=True, on_delete=models.SET_NULL)
    gene_order = models.IntegerField(null=True)
    protein_product = models.CharField(max_length=200, blank=True)
    protein_id = models.CharField(max_length=200, blank=True)
    function = models.CharField(max_length=200, blank=True)
    note = models.CharField(max_length=200, blank=True)
    uniprot = models.CharField(max_length=200, blank=True, unique=True)
    gi = models.CharField(max_length=200, unique=True, blank=True)
    EC_num = models.CharField(max_length=200, blank=True, unique=True)
    locus_tag = models.CharField(max_length=200, unique=True, blank=True)
    translation = models.CharField(max_length=200, unique=True, blank=True)

class HMM_Profile(models.Model):
    key = models.CharField(max_length=200, unique=True, blank=True)
    name = models.CharField(max_length=200, blank=True)
        
class HMM_Output(models.Model):
    key = models.CharField(max_length=200, unique=True, blank=True)
    accession_model = models.ForeignKey(Accession, null=True, on_delete=models.CASCADE) #AssemblyName 222222
    start = models.IntegerField(null=True)
    end = models.IntegerField(null=True)
    hmm_profile_key = models.ForeignKey(HMM_Profile, null=True, on_delete=models.CASCADE) #HMM PROFILE KEY 4444444

#Integer fields should always be checked for NULL value if the requirement for the field is that they must be filled

