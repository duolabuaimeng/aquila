import os
import sys
import pandas as pd
from time import time
import json
class aquilaOptions:
      numbers = 1
      read1 = ""
      read2 = ""
      reference_path = ""
      core_path = ""
      out_path = ""
      threads = 1
'''
objective:The filter compares the samples to the core parts of various strains.
          and then screens one or more strains as a reference sequence.
input:
     -n:Filters select the top n strains(default: n=1)
     -1:The first sequence of samples
     -2:The second Sequence of Samples
     -referenceFiles:The directory where the reference sequence is located
     -coreRefFiles:Catalogue of Core Parts of Strains
     -outDir:Output catalogue 
     -t:Number of threads(default:t=1)     
'''
def map(aquilaOptions):
    ################### aquilaFilter model #################
    n = aquilaOptions.numbers
    r1 = aquilaOptions.read1
    r2 = aquilaOptions.read2
    ref_path = aquilaOptions.reference_path
    c_path = aquilaOptions.core_path
    o_path = aquilaOptions.out_path
    t = aquilaOptions.threads
    c_path = c_path+'/coreindex'
    all_core = os.listdir(c_path)
    cores = []
    for c in all_core:
        name = os.path.splitext(c)
        c_name,c_type = name
        if c_type=='':
           cores.append(c_name)  
    #print (cores)
    for core in cores:
        #Sample comparison to strain core
        cmd1 = 'kallisto quant -i %s/%s -t %d -o %s/%s %s %s'%(c_path,core,t,o_path,core,r1,r2)
        os.system(cmd1)
    all_result = os.listdir(o_path)
    ref_name = []
    counts = []
    
    #Sort the results by comparison
    for result in all_result:
        with open("%s/%s/run_info.json"%(o_path,result),'r') as load_f:
             load_dict = json.load(load_f)
             n_p=load_dict['n_pseudoaligned']
             counts.append(n_p)
             s=result.split('_')[1]+'_'+result.split('_')[2]
             ref_name.append(s)
    data = pd.DataFrame(index=ref_name,columns=['counts'],data=counts)
    data.sort_values(by='counts',ascending=False,inplace=True)
    data.to_csv("%s/core_result.csv"%(o_path))
    #Threshold for different filters
    if n==1:
    	target_name = data.index[0]
    	cmd2 = 'kallisto quant -i %s/%s -t %d -o %s/result %s %s'%(ref_path,target_name,t,o_path,r1,r2)
    	os.system(cmd2)
    else:
        if os.path.exists("%s/merge.fna"%(ref_path)):
           os.remove("%s/merge.fna"%(ref_path)) 
        if os.path.exists("%s/merge"%(ref_path)):
           os.remove("%s/merge"%(ref_path)) 
        for i in range(n):
            target_name = data.index[i]
            cmd3 = 'cat %s/%s.fna >> %s/merge.fna'%(ref_path,target_name,ref_path)
            print (cmd3)
            os.system(cmd3)
        cmd4 = 'kallisto index -i %s/merge %s/merge.fna'%(ref_path,ref_path)
        os.system(cmd4)
        cmd5 = 'kallisto quant -i %s/merge -t %d -o %s/result %s %s'%(ref_path,t,o_path,r1,r2)
        os.system(cmd5)
    #Sort the results
    data = pd.read_csv("%s/result/abundance.tsv"%(o_path),sep='\t',index_col=0,encoding='utf-8')
    data.sort_values(by = 'est_counts',ascending=False,inplace=True)
    data.to_csv("%s/result/abundance_sort.tsv"%(o_path))
    #X= list(data.index.values)
    #y= list(data['est_counts'].values)
    #plt.barh(range(len(y[0:10])), y[0:10],tick_label = X[0:10])
    #plt.title('{}'.format(file))
    #plt.savefig('{}/{}/{}.jpg'.format(path,file,file),dpi=600,bbox_inches='tight')
    #plt.show()
    #plt.close()
