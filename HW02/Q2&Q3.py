#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import sys

def revcomp (seq):
    reverse_seq = seq.upper().replace('A','temp').replace('T','A').replace('temp','T').replace('G','temp').replace('C','G').replace('temp','C')
    revcomp_seq = reverse_seq.rstrip()[::-1]
    assert len(revcomp_seq) != 0,'sequence not existence'

    return revcomp_seq
    
#main    

out_file = open(sys.argv[2],'w')

with open(sys.argv[1],'r') as fh:
    f_list = fh.readlines()
    assert f_list != [],'file is empty'
    
    for exon in f_list:
        if '>' in exon:
            out_file.write(exon)
            continue
        else:
            revcomp_exon = revcomp(exon)
            out_file.write(revcomp_exon)
            out_file.write('\n')

out_file.close()


# In[ ]:




