from __future__ import unicode_literals

from django.db import models

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
    
    # species pointer
    species_model = models.ForeignKey(Species) #SpeciesKey 1111111
 
class Gene(models.Model):
    key = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, null=True)
    gene_synonym = LIST OF STR, null=True
    
    # species pointer
    species_model = models.ForeignKey(Species) #SpeciesKey 1111111
    
    # accession pointer
    accession_model = models.ForeignKey(Accession, null=True) #AssemblyName 22222
    
	strand = models.CharField(max_length=200) # double check that sense (empty) == "+"
    start = models.IntegerField()
    stop = models.IntegerField()
    genebank_annotation = models.CharField(max_length=200, null=True)
    cluster_information = models.CharField(max_length=200, null=True)
    
    # make into operon pointer?
    operon_model = models.CharField(max_length=200, unique=True, null=True) # Operon key 333333333
    
    gene_order = models.IntegerField() #ask Fahim/Heba
    protein_product = models.CharField(max_length=200, null=True)
    protein_id = models.CharField(max_length=200, null=True)
    function = models.CharField(max_length=200, null=True)
    note = models.CharField(max_length=200, null=True)
    uniprot = models.CharField(max_length=200, null=True, unique=True)
    gi = models.CharField(max_length=200, unique=True)
    EC_num = models.CharField(max_length=200, null=True, unique=True)
    locus_tag = models.CharField(max_length=200, unique=True)
    translation = models.CharField(max_length=200, unique=True)
    
class Operon_Database(models.Model):
    key = models.CharField(max_length=200, unique=True)  # Operon key 3333333333
    operon_name = models.CharField(max_length=200)
    kegg_orthology_ID = models.CharField(max_length=200, unique=True)
    
    # make into species pointer?
    species_model = models.ForeignKey(Species) #SpeciesKey 1111111
    annotation = models.CharField(max_length=200)

class HMM_Output(models.Model):
    key = models.CharField(max_length=200, unique=True)
    
    # make into accession pointer
    accession_model = models.ForeignKey(Accession) #AssemblyName 222222
    
    start = models.IntegerField()
    end = models.IntegerField()
    
    # make into hmm_profile?
    hmm_profile_key = models.CharField(max_length=200, unique=True) #HMM PROFILE KEY 4444444

class HMM_Profile(models.Model):
    key = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    
