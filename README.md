# aquila
## aquila:Identification of Food-borne Pathogens with Low Abundance
### Introduction
aquila consists of two modules for sequencing-based metagenomic profiling. The aquilaIndex module index the core parts of various strains and index the database data of various strains.The aquilaMap module firstly aligns the reads to the core reference library and select selection of one or more strains as reference sequences,secondly aligns the reads to the target reference library which we build before.Report files: 1) a summary report (.tsv) that contains the numbers and proportions of reads aligned to each genome identified in the sample 2) a sorted summary report (_sort.tsv) that save the sorted results 3) run_info.json is a json file containing information about the run 4) abundances.h5 is a HDF5 binary file containing run info.

# Manual
First of all, we should:
- Change directory (cd) to aquila folder
- cd into aquila directory and call aquilaIndex module help for details
## index

