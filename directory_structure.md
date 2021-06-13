This file contains the structure of the directories, to ease coordination through all data, files, and scripts.\
Listed order corresponds to the alphabetical order of directories/files.

**readme.md**  
  readme with all commands  

**directory_structure.md**  
  current file  


### /alignments_toxIN  
- RNA and protein co-alignments with the species chosen for co-evolution analysis  
- /figures:   
  - /structures: PDB files 2XD0 and 4ATO with PyMOL session and figures for visualization  
  - /weblogos: weblogos of co-MSA and all-MSA for RNA and protein    
- /protein:  
  - /cdhit_cluster: cd-hit clustering of toxin protein sequences  
  - sequence fasta files, co- and all-MSA, feature annotation files for co- and all-MSA   
- /rna:  
  - /cdhit_cluster: cd-hit clustering of antitoxin RNA sequences  
  - /mlocarna_all and /mlocarna_co: co- and all-MSA, respectively  
  - sequence fasta files and feature annotation files for co- and all-MSA    
- analysis_protein.txt: protein co-MSA annotation and analysis per residue  
- analysis_rna.txt: RNA co-MSA annotation and analysis per residue  
- coevolution.md: information on specific interaction pairs and co-evolutionary investigation  

### /all_toxin_hits  
- processing step for all sequence sets and homology search results  
- extract_id-species.py  
  extract database IDs and organism names of input set  
  output files: "idlist_setname.txt"  
- retrieve_genus.py  
  get taxonomy IDs of set sequences, input are "idlist"-files  
  output files: "taxidlist_setname.txt"  

### /cmscan_checkup  
- cmscan results (verification of the covariance models) for RNA sets literature 1, literature 2, rfam + literature 1  

### /model_rfam  
- covariance model and cmsearch results for the rfam set (RNA)  

### /model_toxirna_lit1manual  
- covariance model and cmsearch results (--mid for run with relaxed filter cutoffs) for the literature 1 set (RNA, manual alignment)  

### /model_toxirna_lit2  
- covariance model and cmsearch results (--mid for run with relaxed filter cutoffs) for the literature 2 set (RNA)  
- underlying MSA is based on mlocarna version 1.9.2.3  

### /model_toxirna_pdb  
- covariance model and cmsearch results for the pdb set (RNA)  

### /model_toxirna_rfam+lit1  
- covariance model and cmsearch results (--mid for run with relaxed filter cutoffs) for the rfam + literature 1 set (RNA)  
- /version_1.9.2.3 and /version_2.0.0.RC8 refers to mlocarna versions of underlying MSA  

### /msa_rfam  
- MSA of rfam set sequences (RNA), used for visualization of secondary structure (MSA from Rfam itself was used for covariance model)  

### /msa_toxirna_literature  
- /lit1_manual:  manual alignment of literature 1 set sequences (RNA)  
  - /mlocarna:  MSA of manually shifted sequences (manual_lit1.fasta)  
  - /RNAalifold:  RNAalifold of manual MSA without constraints  
  - /RNAalifold_constraint_hp1: RNAalifold of manual MSA with constraint for 5'HP  
  - /RNAalifold_constraint_hp2: RNAalifold of manual MSA with constraint for 3'HP  
  - /Rscape_hp1: R-Scape results for 5'HP  
  - /Rscape_hp2: R-Scape results for 3'HP  
  - manual_lit1.fasta: lit1 set with manually shifted starting position of sequences (based on Blower et al., 2012)  
  - msa_manual_lit1.aln: manual MSA of lit1 set (based on Blower et al., 2012)  
- /lit1:  
  MSA of literature 1 set sequences (RNA)  
- /lit2:  
  MSA of literature 2 set sequences (RNA)  

### /msa_toxirna_pdb  
- MSA of pdb set sequences (RNA)  

### /msa_toxirna_rfam+lit1man  
- MSA of rfam + literature 1 set sequences (RNA)  
- one directory per mlocarna version: /version_1.9.2.3 and /version_2.0.0.RC8  

### /pfam_clusters
- cd-hit clustering of PFAM sequences (toxin protein)

### /pfam_hmm
- HMM of Pfam entry PF13958 (download from Pfam, toxin proteins)
- hmmsearch results with that HMM

### /rnafold_toxirna  
- RNAfold single RNA secondary structure prediction for RNA sequence sets literature 1, literature 2, pdb  

### /rnalien  
- results of RNAlien run with CP000905.1 (B. weihenstephanensis, antitoxin RNA)  

### /rpi_tools  
- results of RPI prediction tools: PRIdictor, PRI Hotscore, PLIP  

### /sequence_data  
- concat_fastas.sh  
  concatenate fasta files  
- sequence data from databases and literature
- also includes alignments directly from Rfam and Pfam

### /species_comparison
- inputfile_taxids.txt  
  input file for R-script, collection of organisms of all database and homology search sequence sets  
- species_candidates.txt  
  putative candidates for co-alignment analysis  
- species_exactoverlaps.txt  
  overlaps as seen in UpSet plot  
- species_visualization.R  
  R-script to generate UpSet plot  
- UpSet plots  
