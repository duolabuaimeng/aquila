# aquila
## aquila:Identification of Food-borne Pathogens with Low Abundance
### Introduction
aquila consists of two modules for sequencing-based metagenomic profiling. The aquilaIndex module index the core parts of various strains and index the database data of various strains.The aquilaMap module firstly aligns the reads to the core reference library and select selection of one or more strains as reference sequences,secondly aligns the reads to the target reference library which we build before.Report files: 1) a summary report (.tsv) that contains the numbers and proportions of reads aligned to each genome identified in the sample 2) a sorted summary report (_sort.tsv) that save the sorted results 3) run_info.json is a json file containing information about the run 4) abundances.h5 is a HDF5 binary file containing run info.

# Manual
First of all, we should:
- change directory (cd) to aquila folder
- cd into aquila directory and call aquilaIndex module help for details
  
  cd ../aquila
  python aquila.py index -h
  
## index
Now you can build your own database,you need to make sure that kallisto is already in your path. We need the database of strains and the database of the core part of strains, which can be downloaded in NCBI.Attention should be paid to the naming of the core part of the strain.(strain named Bacillus_cereus ,core part of strain named: only_Bacillus_cereus_blastn ) 

python aquila.py index -i path1 -c path2

Required arguments:
-i, string                    the directory of strains.

-c, string                    the directory of core part of strains.

call aquilaMap module help for details
python aquila.py map -h
## map
First you need to make sure that the index has been established.

python aquila.py map -n 5 -1 read_1 -2 read_2 -referenceFiles path1 -coreRefFiles path2 -outDir path3

Required arguments:
-1, string                    paired-end and requires an even number of FASTQ files represented as pairs

-2, string                    paired-end and requires an even number of FASTQ files represented as pairs

-referenceFiles, string       the directory where the strain index is located

-coreRefFiles, string         the directory where the core part of strain index is located

-outDir, string               directory to write output to

Optional arguments:
-n, int                       this parameter represents several strains of filters that we have screened as reference sequences.
                              (default: 1)

-t, int                       number of threads to use (default: 1)

