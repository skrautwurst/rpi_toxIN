# Workflow of RPI analysis  

## Antitoxin RNA  
### Sequence gathering  

**Rfam**  
download from Rfam entry RF02519  
directory: /rpi_toxIN/sequence_data/  

**PDB**  
download from PDB to /rpi_toxIN/sequence_data/toxirna_seq_pdb.fasta  
  4ATO: Short et al., 2013  
  2XD0: Blower et al., 2011  
  2XDB: Blower et al., 2011  
  2XDD: Fineran et al., 2009  

**literature 1**  
/rpi_toxIN/sequence_data/toxirna_seq_literature1.fasta  
Blower et al., 2012  
include all organisms, which are additional to the ones from Fineran et al. (2009), RNA sequences added from Table S1
  > |||  
  |-|-|  
  Actinobacillus ureae ATCC 25976  
  Bacillus cereus Rock 1-15  
  Bryantella formatexigens DSM 14469  
  Clostridium botulinum BKT015925  
  Clostridium cellulovorans 743B  
  Clostridium nexile DSM 1787  
  Clostridium phage D-1873  
  Clostridium sp. HGF2  
  Coprobacillus sp. 29_1  
  Coprococcus sp. ART55/1  
  Eubacterium rectale DSM 17629  
  Eubacterium rectale M104/1  
  Eubacterium saburreum DSM 3986  
  Eubacterium saphenum ATCC 49989  
  Eubacterium yurii subsp. margaretiae ATCC 43715  
  Finegoldia magna BVS033A4  
  Fusobacterium sp. 3_1_5R  
  Fusobacterium sp. 4_1_13  
  Fusobacterium sp. D12  
  Fusobacterium ulcerans ATCC 49185  
  Haemophilus parasuis  
  Haemophilus parasuis SH0165  
  Haemophilus somnus 2336 | no sequence in Tab. S1  
  Lachnospiraceae bacterium 2_1_46FAA  
  Lactobacillus gasseri JV-V03  
  Lactobacillus helveticus DSM 20075 | no sequence in Tab. S1  
  Lactobacillus helveticus MTCC 5463 | no sequence in Tab. S1  
  Lactobacillus jensenii 1153 | no sequence in Tab. S1  
  Lactobacillus jensenii 208-1  
  Lactobacillus jensenii 269-3  
  Lactobacillus jensenii 27-2-CHN  
  Lactobacillus jensenii SJ-7A-US | repeats downstream of ORF
  Lactobacillus kefiranofaciens ZW3  
  Leptotrichia goodfellowii F0264  
  Leptotrichia hofstadii F0254  
  Pectobacterium atrosepticum SCRI1039  
  Peptoniphilus duerdenii ATCC BAA-1640  
  Peptoniphilus harei ACS-146-V-Sch2b | no sequence in Tab. S1  
  Roseburia intestinalis M50/1  | large gap between end of ToxI and start of ToxN (292bp)  
  Roseburia intestinalis XB6B4 | large gap between end of ToxI and start of ToxN (232bp)  
  Ruminococcus sp. 5_1_39B_FAA  
  Taylorella equigenitalis MCE9  
  Treponema succinifaciens DSM 2489 | no sequence in Tab. S1  
  Treponema vincentii ATCC 35580  
  Veillonella parvula ACS-068-V-Sch12  

**literature 2**  
/rpi_toxIN/sequence_data/toxirna_seq_literature2.fasta  
Fineran et al., 2009  
RNA sequences from Table S3 (putative ToxIN-type loci of multiple bacteria), column "repeat consensus" contains toxI RNA sequences  
  > YP_001513384|Alkaliphilus_oremlandii_OhILAs  
  CP000047|Bacillus_thuringiensis_serovar_konkukian_97-27_pBT9727  
  AAZ06636|Bacillus_thuringiensis_serovar_kurstaki_HD73_pAW63
  YP_001642731|Bacillus_weihenstephanensis_KBAB4_pBWB402
  FJ176937|Erwinia_carotovora_subsp_atroseptica_1039_pECA1039  
  ZP_02272649|Fusobacterium_nucleatum_subsp_polymorphum_ATCC10953  
  YP_271719|Haemophilus_influenzae_biotype_aegyptius_pF1947  
  ZP_00133190|Histophilus_somni_2336  
  NP_862552|Lactococcus_lactis_subsp_lactis_W-37_pSRQ900  
  ZP_01968975|Ruminococcus_torques_ATCC_27756  
  ZP_01667702|Thermosinus_carboxydivorans_Nor1  


### MSA and secondary structure  
*commands listed for one specific example; applied the same way for further involved files/data*  

**MSA with mlocarna**  

    mlocarna --stockholm -s 400 --tgtdir /rpi_toxIN/msa_toxirna_pdb/ /rpi_toxIN/sequence_data/toxirna_seq_pdb.fasta > /rpi_toxIN/msa_toxirna_pdb/mlocarna_toxirna_pdb.log  

**RNAfold for each sequence**  

    RNAfold -p --MEA -o /rpi_toxIN/rnafold_toxirna/pdb/allrna_pdb_rnafold.out -i /rpi_toxIN/sequence_data/toxirna_seq_pdb.fasta  

**RNAalifold for manual alignment of lit1**

    RNAalifold --noLP --color --mis -r -p --aln --cfactor 0.6 --nfactor 0.5 /rpi_toxIN/msa_toxirna_literature/lit1_manual/msa_manual_lit1.aln > /rpi_toxIN/msa_toxirna_literature/lit1_manual/RNAalifold/alifold_output.txt

    RNAalifold --noLP --color --mis -r -p --aln --cfactor 0.6 --nfactor 0.5 --aln-stk --MEA -C /rpi_toxIN/msa_toxirna_literature/lit1_manual/msa_manual_lit1.aln > /rpi_toxIN/msa_toxirna_literature/lit1_manual/RNAalifold_constraint_hp1/alifold_output.txt

constraint for hairpin loop 1:
.....((((...........))))......................  
constraint for hairpin loop 2:
...............||.............................  

**R-Scape**  

    R-scape -s --fold --outdir /rpi_toxIN/msa_toxirna_literature/lit1_manual/Rscape_hp1/ /rpi_toxIN/msa_toxirna_literature/lit1_manual/RNAalifold/RNAalifold_results.stk  

### Covariance models and homology search
*commands listed for one specific example; applied the same way for further involved files/data*

download bacterial genomes with esearch v7.40:  

    esearch -db nucleotide -query "bacteria[filter] AND refseq[filter]" | efetch -format fasta > /rpi_toxIN/all_genomes.fna  

**Infernal**  

build and calibrate covariane model  

    /infernal-1.1.3/src/cmbuild -o /rpi_toxIN/model_toxirna_pdb/toxi_pdb_cmbuild.out /rpi_toxIN/model_toxirna_pdb/toxipdb_model.cm /rpi_toxIN/msa_toxirna_pdb/results/result.stk
    /infernal-1.1.3/src/cmcalibrate /rpi_toxIN/model_toxirna_pdb/toxipdb_model.cm <!--optional: --cpu <n> -->

homology search with covariance model  

    /infernal-1.1.3/src/cmsearch -o /rpi_toxIN/model_toxirna_pdb/toxipdb_cmsearch.out -A /rpi_toxIN/model_toxirna_pdb/toxipdb_cmsearch_msa.fa --tblout /rpi_toxIN/model_toxirna_pdb/toxipdb_cmsearch_hits.txt --cpu 16 --verbose --nohmmonly -E 1000 -Z 549862.597050 /rpi_toxIN/model_toxirna_pdb/toxipdb_model.cm /rpi_toxIN/all_genomes.fna

        for more relaxed prefilter add --mid (or --nohmm):
    /infernal-1.1.3/src/cmsearch -o /rpi_toxIN/model_toxirna_lit2/toxilit2_cmsearch--mid.out -A /rpi_toxIN/model_toxirna_lit2/toxilit2_cmsearch--mid_msa.fa --tblout /rpi_toxIN/model_toxirna_lit2/toxilit2_cmsearch--mid_hits.txt --mid --cpu 16 --verbose --nohmmonly -E 1000 -Z 549862.597050 /rpi_toxIN/model_toxirna_lit2/toxilit2_model.cm /rpi_toxIN/all_genomes.fna

check covariance model  

    /infernal-1.1.3/src/cmpress /rpi_toxIN/model_toxirna_lit2/toxilit2_model.cm
    /infernal-1.1.3/src/cmscan -o /rpi_toxIN/cmscan_checkup/lit2_cmscan.out --tblout /rpi_toxIN/cmscan_checkup/lit2_cmscan_hits.txt /rpi_toxIN/model_toxirna_lit2/toxilit2_model.cm /rpi_toxIN/sequence_data/toxirna_seq_literature2.fasta

**RNAlien**  
    webserver used  
    download to /rpi_toxIN/rnaalien/  

------------------------------------------------

## Toxin protein

download bacterial proteomes from NCBI FTP server  

**hmmsearch**

    hmmsearch -o /rpi_toxIN/pfam_hmm/toxnpfam_hmmsearch.out -A /rpi_toxIN/pfam_hmm/toxnpfam_hmmsearch_msa.fa --tblout /rpi_toxIN/pfam_hmm/toxnpfam_hmmsearch_hits.txt -Z 47079205 -E 1000 --cpu 10 /rpi_toxIN/pfam_hmm/PF13958_ToxN.hmm /rpi_toxIN/all_proteomes.fa  

**clustering**

    cd-hit -i /rpi_toxIN/sequence_data/PF13958_full_sequences.fasta -o /rpi_toxIN/pfam_clusters/pfam100 -c 1.0 -n 5 -d 0

      -n 5 for -c 1.0 to 0.7
      -n 4 for -c 0.65 to 0.6

------------------------------------------------

## Species comparison

**results processing**  
  extract database IDs and organism name from entries in all sets:

    /rpi_toxIN/all_toxin_hits/extract_id-species.py

    > input file for each set:
    rfam: /rpi_toxIN/sequence_data/RF02519.fa
    pfam: /rpi_toxIN/sequence_data/PF13958_msafull.fasta
          /rpi_toxIN/sequence_data/PF13958_msaseed.fasta
    pdb:  /rpi_toxIN/sequence_data/toxirna_seq_pdb.fasta
    literature1: /rpi_toxIN/sequence_data/toxirna_seq_literature1+idgi.fasta
    literature2: /rpi_toxIN/sequence_data/toxirna_seq_literature2.fasta
    cmsearch: rfam: /rpi_toxIN/model_rfam/toxi_cmsearch_hits.txt
              pdb:  /rpi_toxIN/model_toxirna_pdb/toxipdb_cmsearch_hits.txt
              lit1: /rpi_toxIN/model_toxirna_lit1manual/toxilit1man_cmsearch_hits.txt (deactivate filter for inclusion threshold)
                    /rpi_toxIN/model_toxirna_lit1manual/toxilit1man_cmsearch--mid_hits.txt (deactivate filter for inclusion threshold)
              rfam+lit1: /rpi_toxIN/model_toxirna_rfam+lit1/version_2.0.0RC8/toxirfamlit1_cmsearch--mid_hits.txt (deactivate filter for inclusion threshold)
    hmmsearch: /rpi_toxIN/pfam_hmm/toxnpfam_hmmsearch_hits.txt

    > write output to /rpi_toxIN/all_toxin_hits/

  retrieve taxonomy ID for entries of sets:

    /rpi_toxIN/all_toxin_hits/retrieve_genus.py

    > options:
    t 1: rfam, cmsearch, lit1
    t 2: hmm, lit2
    t 3: pfam
    t 4: pdb

    > input files are output files from extract_id-species.py
    > write output to /rpi_toxIN/all_toxin_hits/

  sort each file according to taxonomy ID and reduce multiple matches for the same taxonomy ID to one entry:

    sort -k1 -n -u /rpi_toxIN/all_toxin_hits/taxidlist_rfam.txt > /rpi_toxIN/all_toxin_hits/taxidlist_rfam_unique.txt

  append all files into one for R script, adapt the line start (sed) for each set:

    for f in /rpi_toxIN/all_toxin_hits/taxidlist_rfam_unique.txt; do sed "s/^/rfam\t/" $f; done | cut -d ',' -f1 >> /rpi_toxIN/species_comparison/inputfile_taxids.txt

  for hmmsearch (/rpi_toxIN/all_toxin_hits/taxidlist_hmm_unique.txt) use:  

    - get all matches annotated as taIII:
    for f in /rpi_toxIN/all_toxin_hits/taxidlist_hmm_unique.txt; do sed "/MULTISPECIES/d; /hypothetical/d; s/^/hmmsearch_taIII\t/" $f; done | cut -d ',' -f1 >> /rpi_toxIN/species_comparison/inputfile_taxids.txt
    - get all matches annotated as hypothetical protein:
    for f in /rpi_toxIN/all_toxin_hits/taxidlist_hmm_unique.txt; do sed "/MULTISPECIES/d; /type_III/d; s/^/hmmsearch_hyppr\t/" $f; done | cut -d ',' -f1 >> /rpi_toxIN/species_comparison/inputfile_taxids.txt

**overlap analysis with UpSet plot**   
  generate plot with R script: /rpi_toxIN/species_comparison/species_visualization.R

------------------------------------------------

## RNA-protein co-alignments

**RPI tools**  
  web services with default parameters  
  sequences from PDB:2XD0, PDB:4ATO for RPISeq and PRIdictor  
  PDB:2XD0 and PDB:4ATO for PRI Hotscore and PLIP  
  download results to /rpi_toxIN/rpi_tools/

**clustering**  
*protein*  

    cd-hit -i /rpi_toxIN/alignments_toxIN/protein/seq_co.fasta -o /rpi_toxIN/alignments_toxIN/protein/cdhit_cluster/seqco95 -c 0.95 -n 5 -d 0

      -n 5 for -c 0.95 to 0.7

*RNA*

    cd-hit-est -i /rpi_toxIN/alignments_toxIN/rna/seq_co.fasta -o /rpi_toxIN/alignments_toxIN/rna/cdhit_cluster/seqco95 -c 0.95 -n 10 -d 0

      -n 10 for -c 0.95
      -n 8  for -c 0.90
      -n 6  for -c 0.85
      -n 5  for -c 0.80

**co-alignments**  

*protein*  
  MSA with mafft  

    mafft /rpi_toxIN/alignments_toxIN/protein/seq_co.fasta > /rpi_toxIN/alignments_toxIN/protein/msa-co_toxnproteins.fasta    

  convert fasta to stockholm files (command line)  

    from Bio import AlignIO
    msa = AlignIO.read("msa-co_toxnproteins.fasta","fasta")
    AlignIO.write(msa,"msa-co_toxnproteins.stk","stockholm")

*RNA*  
  shift starting positions of species sequences manually  
  MSA with mlocarna   

    mlocarna --stockholm --tgtdir /rpi_toxIN/alignments_toxIN/rna/mlocarna_co /rpi_toxIN/alignments_toxIN/rna/seq_co.fasta > /rpi_toxIN/alignments_toxIN/rna/mlocarna_co/mlocarna_cotoxi.log

*annotation of interactions*  
- literature-based interactions for PDB:2XD0 (Blower et al., 2011) and PDB:4ATO (Short et al., 2013)  
- annotation of both reference sequences into the MSA stk files (RNA and protein) with stk annotation lines:  
      #=GS <seqname> DE <residue annotation>  
      #=GR <seqname> AS <residue annotation>  
- pseudoknot secondary structure annotation for RNA MSA stk files    
  5'HP (co-MSA) and 3'HP (all-MSA) merged in consensus:  
      #=GC SS_cons ....AAAAA....<<<<aaaaa......>>>>........  
    (3'HP adjusted according to annotation in Blower et al., 2012, Fig.4)  

- visualization with Jalview (as feature annotations)  

- annotations from literature and CoDNaS-RNA database (cluster 99): see /rpi_toxIN/alignments_toxIN/analysis_protein.txt + _rna.txt and /rpi_toxIN/alignments_toxIN/coevolution.md

*Weblogos*  
  web service of WebLogo 3  

*PyMOL*  
  annotation selection for PDB:2XD0  

    select protein, chain A  
    select aminoacids_blower, chain A & resi 2+3+19+21+23+29+33+52+53+55+58+73+74+79+88+99+100+102+110+112+114+115+116+117+118+119+122  
    select aminoacids_codnas, chain A & resi 20+143  

    select rna, chain H+G  
    select bases_blower, chain H+G & resi 1+6+17+31+32  
    select bases_codnas, chain H+G & resi -3+-2+5+7+8+21+22+23+26+27+28+30  

  annotation selection for PDB:4ATO  

    select protein, chain A  
    select aminoacids, chain A & resi 25+26+27+29+31+37+56+57+58+86+110+117+127+130+131+134+148

    select rna, chain G  
    select bases, chain G & resi 1+2+3+4+5+10+16+17+18+19+20+29+30+31+32+33+34  
