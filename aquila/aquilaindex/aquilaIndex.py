from time import time
import os

class aquilaOptions:
      path_reference = ""
      path_core = ""

'''
objective:Index the reference sequence of each strain separately,
          The index can be used directly when the filter threshold is 1.
input:
      -i:The folder where the reference sequence is located

'''
def index_reference(aquilaOption):
################### index_reference model #################
    start = time()
    path = aquilaOption.path_reference
    all_strain = os.listdir(path)
    for strain in all_strain:
        index_name = str(str(strain).split('.')[0])
        cmd1 = 'kallisto index -i %s/%s %s/%s'%(path,index_name,path,strain)
        os.system(cmd1)
    end = time()
    time_consume = end-start
    print ('index_reference time consuming: %d s'%(time_consume))

'''
objective:Index the core of each strain's reference sequence
input:
      -c:The folder where the core part of the reference sequence is located

'''

def index_core(aquilaOption):
################### index_core model #################
    start = time()
    path = aquilaOption.path_core
    all_core = os.listdir(path)
    if not os.path.exists('%s/coreindex'%(path)):
       os.makedirs('%s/coreindex'%(path))
    for core in all_core:
        index_name = str(str(core).split('.')[0])
        cmd1 = 'kallisto index -i %s/coreindex/%s %s/%s'%(path,index_name,path,core)
        os.system(cmd1)
    end = time()
    time_consume = end-start
    print ('index_core time consuming: %d s'%(time_consume))
