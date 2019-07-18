import os
import sys
aquiladir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,aquiladir) 
from aquila.aquilaindex import aquilaIndex
from aquila.aquilamap import aquilaMap
from aquila._version import VERSION
from time import time
import argparse

#main()
parser = argparse.ArgumentParser(description="aquila")

#create the top-level parser
parser.add_argument('--version', action='version', version=VERSION)
subparsers = parser.add_subparsers(dest='subcommand', help='Select one of the following sub-commands')

#create the parser for the "index" command
parser_a = subparsers.add_parser('index', help='aquila index Module')
parser_a.add_argument('-i', action='store', dest='lib_reference', required=True, 
help='Specify reference genome')
parser_a.add_argument('-c', action='store', dest='core_reference', required=True, 
help='core reference genome')

# create the parser for the "MAP" command
parser_b = subparsers.add_parser('map', help='aquila MAP Module')
parser_b.add_argument('-n', default=1,type=int, action='store', dest='lib_size', required=False, 
help='Number of reference strains (default: 1)')
parser_b.add_argument('-1', default='', action='store', dest='map_inputread1', required=False, 
	help='Input Read Fastq File (Pair 1)')
parser_b.add_argument('-2', default='', action='store', dest='map_inputread2', required=False, 
help='Input Read Fastq File (Pair 2)')
parser_b.add_argument('-referenceFiles', default='', action='store', 
	dest='map_targetref', required=False, 
help='Target Reference Genome Fasta Files Full Path')
parser_b.add_argument('-coreRefFiles', default='', action='store', 
	dest='map_filterref', required=False, 
help='core Reference Genome Fasta Files Full Path')
parser_b.add_argument('-outDir',action='store',default='.',dest='map_outDir',required=False,
help='Output Directory (Default=.(current directory))')
parser_b.add_argument('-t', action='store', dest='map_numthreads', required=False, 
default=1, type=int, help='Number of threads to use by kallisto if different from default (1)')

def main():
    # parse some argument lists
    inputArgs = parser.parse_args()


    ########## aquilaIndex model ############
    if inputArgs.subcommand=='index':
       aquilaOptions = aquilaIndex.aquilaOptions()
       if len(inputArgs.lib_reference)>0:
            aquilaOptions.path_reference = inputArgs.lib_reference
       if len(inputArgs.core_reference)>0:
            aquilaOptions.path_core = inputArgs.core_reference
       aquilaIndex.index_reference(aquilaOptions)
       aquilaIndex.index_core(aquilaOptions)

    ########## aquilaMap model ############
    start =time()
    if inputArgs.subcommand=='map':
       aquilaOptions = aquilaMap.aquilaOptions()
       aquilaOptions.numbers = inputArgs.lib_size
       if len(inputArgs.map_inputread1)>0:
            aquilaOptions.read1 = inputArgs.map_inputread1
       if len(inputArgs.map_inputread2)>0:
            aquilaOptions.read2 = inputArgs.map_inputread2
       if len(inputArgs.map_targetref)>0:
            aquilaOptions.reference_path = inputArgs.map_targetref
       if len(inputArgs.map_filterref)>0:
            aquilaOptions.core_path = inputArgs.map_filterref
       if len(inputArgs.map_outDir)>0:
            aquilaOptions.out_path = inputArgs.map_outDir
       aquilaOptions.threads = inputArgs.map_numthreads
       aquilaMap.map(aquilaOptions)
    end = time()
    time_consume = end-start
    print ('aquilaMap time consuming: %d s'%(time_consume))
if __name__ == "__main__":
    main()
