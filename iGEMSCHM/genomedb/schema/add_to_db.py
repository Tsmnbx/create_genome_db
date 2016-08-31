from Bio import SeqIO
from parse_features import *
import models.py

file_name = "GCA_000009145.1_ASM914v1_genomic.gbff"

genome = list(SeqIO.parse(file_name,"genbank"))
first_locus = genome[0]

if is_WGS(first_locus):
    num_of_locus = len(genome)
else:
    num_of_locus = 1

num_of_locus = 1

gene_key_count = 1

for locus_id in range(0, num_of_locus):
    # looping through all locus
    locus = genome[locus_id]
    locus_name = get_locus_name(genome[locus_id])

    # source
    source = locus.features[0]
    # applying all functions related to getting info from source
    sname = (get_species_name(source))
    sub_species = get_subspecies(source)
    strain =(get_strain(source))
    sub_strain = get_sub_strain(source)
    tax = get_taxon(source)
    
    # Adding these values to the Species Model Fields
    s = Species()
    s.key = 1 # will change when dealing with list
    s.name = sname
    s.subspecies = sub_species
    s.strain = strain
    s.sub_strain = sub_strain
    s.taxon = tax

    # number of genes inside the locus, genome[locus]
    num_features = len(locus.features)
    for feature_id in range(1,num_features):
        # if it is a CDS
        if (locus.features[feature_id].type == "CDS"):
            CDS = locus.features[feature_id]
            # applying all functions related to getting info from the CDS
             gname = get_qualifier(CDS, "gene")
             genesym = get_qualifier(CDS, "gene_synonym")
             loctag = get_qualifier(CDS, "locus_tag")
             codstart = get_qualifier(CDS, "codon_start")
             Ec = get_qualifier(CDS, "EC_number")
             proteinid = get_qualifier(CDS, "protein_id")
            pfam = get_qualifier(CDS, "Pfam")
             uniport = get_qualifier(CDS, "UniProt")
             gi = get_qualifier(CDS, "GI")
             prod = get_qualifier(CDS, "product")
             trans = get_qualifier(CDS, "translation")
             func = get_qualifier(CDS, "function")
             note = get_qualifier(CDS, "note")
             start = get_start(CDS)
             end = get_end(CDS)
             strand = get_strand(CDS)
            
            # Adding these values to the Gene Model Fields
            g = Gene()
            g.name = gname
            g.codon_start = codstart
            g.gene_synonym = genesym
            g.species_model = 1 #will change for list of species
            g.accession_model = 1 #will change for list of species
            g.strand = strand
            g.start = start
            g.stop = end
            #g.genebank_annotation =
            #g.cluster_information =
            #g.operon_model =
            #g.gene_order =
            g.protein_product = prod
            g.protein_id = proteinid
            g.function = func
            g.note = note
            g.uniprot = uniport
            g.gi = gi
            g.EC_num = Ec
            g.locus_tag = loctag
            g.translation = trans
            g.key = gene_key_count
            gene_key_count =+1
            
    #Gene.save()
            
            