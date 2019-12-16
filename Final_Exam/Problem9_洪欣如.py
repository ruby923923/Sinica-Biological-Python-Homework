
# coding: utf-8

# In[34]:


import Bio
import re
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Alphabet import generic_dna
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Data import CodonTable


# In[35]:


#read file
gene = SeqIO.read('Final_exam_Regex_input.fasta','fasta')
seq_name = gene.id
seq_seq = gene.seq


# In[36]:


#write file 
output = open('Problem9_洪欣如.txt','w')


# In[37]:


#find pattern
pattern_1 = re.compile(r'ggatcc')
pattern_2 = re.compile(r'cggccg')
pattern_3 = re.compile(r'gccggc')
pattern_4 = re.compile(r'gaattc')

seqence =str(seq_seq)

def pattern_finder(pattern):
    for m in re.finditer(pattern,seqence):
        output.write(str(m.group())+'\t'+str(m.start())+'-'+str(m.end())+'\n')
    return

pattern_finder(pattern_1)
pattern_finder(pattern_2)
pattern_finder(pattern_3)
pattern_finder(pattern_4)

output.close()

