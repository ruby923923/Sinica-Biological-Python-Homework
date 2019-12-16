
# coding: utf-8

# In[10]:


import Bio
import re
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.Alphabet import generic_dna
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio.Data import CodonTable


# In[11]:


#read file
gene = SeqIO.read('Input.fasta','fasta')
seq_name = gene.id
seq_seq = gene.seq


# In[12]:


#write file 
output = open('Problem8_洪欣如.txt','w')


# In[13]:


#count GC
GC_percent = GC(seq_seq)
GC_percent

output.write('(a)'+'\n')
output.write(str(seq_name)+'\t'+str(GC_percent)+'%'+'\n')
output.write('\n')


# In[14]:


#transcribe and translate
ts = seq_seq.transcribe()
tl_id_1 = seq_seq.translate(table=1)
tl_id_2 = seq_seq.translate(table=2)

print(ts)
print(tl_id_1)
print(tl_id_2)

output.write('(b)'+'\n')
output.write('Transcribe:'+'\n'+str(ts)+'\n')
output.write('Standard codon table translate:'+'\n'+str(tl_id_1)+'\n')
output.write('Mitochondrial codon table translate:'+'\n'+str(tl_id_2)+'\n')
output.write('\n')


# In[15]:


#Stop codon finding
standard_table = CodonTable.unambiguous_dna_by_id[1]
mito_table = CodonTable.unambiguous_dna_by_id[2]

std_stop = standard_table.stop_codons
mito_stop = mito_table.stop_codons


# In[16]:


std_stop_pos = []
std_stop_codon = []
mito_stop_pos = []
mito_stop_codon = []

sequence = str(seq_seq)
n = len(sequence)
k=0
while k < n-2:
    codon = sequence[k:k+3]
    if codon in std_stop:
        std_stop_pos.append(str(k+1)+'-'+str(k+3))
        std_stop_codon.append(codon)
    if codon in mito_stop:
        mito_stop_pos.append(str(k+1)+'-'+str(k+3))
        mito_stop_codon.append(codon)    
    k += 1


# In[17]:


std_TAA = []
std_TAG = []
std_TGA = []
mito_TAA = []
mito_TAG = []
mito_AGA = []
mito_AGG =[]

for i in range(len(std_stop_codon)):
    if std_stop_codon[i] == 'TAA':
        std_TAA.append(i) 
    elif std_stop_codon[i] == 'TAG':
        std_TAG.append(i) 
    elif std_stop_codon[i] == 'TGA':
        std_TGA.append(i)   

for i in range(len(mito_stop_codon)):
    if mito_stop_codon[i] == 'TAA':
        mito_TAA.append(i) 
    elif mito_stop_codon[i] == 'TAG':
        mito_TAG.append(i) 
    elif mito_stop_codon[i] == 'AGA':
        mito_AGA.append(i)  
    elif mito_stop_codon[i] == 'AGG':
        mito_AGG.append(i)  
    
std_TAA_pos = []
std_TAG_pos = []
std_TGA_pos = []
mito_TAA_pos = []
mito_TAG_pos = []
mito_AGA_pos = []
mito_AGG_pos =[]
    
for i in std_TAA:
    std_TAA_pos.append(std_stop_pos[i])
for i in std_TAG:
    std_TAG_pos.append(std_stop_pos[i])
for i in std_TGA:
    std_TGA_pos.append(std_stop_pos[i])
for i in mito_TAA:
    mito_TAA_pos.append(mito_stop_pos[i])
for i in mito_TAG:
    mito_TAG_pos.append(mito_stop_pos[i])
for i in mito_AGA:
    mito_AGA_pos.append(mito_stop_pos[i])
for i in mito_AGG:
    mito_AGG_pos.append(mito_stop_pos[i])
     
output.write('(c)'+'\n')
output.write('Codon-table-name (1)'+'\n')
output.write('TAA'+'\t'+str(std_TAA_pos)+'\n')
output.write('TAG'+'\t'+str(std_TAG_pos)+'\n')
output.write('TGA'+'\t'+str(std_TGA_pos)+'\n')
output.write('Codon-table-name (2)'+'\n')
output.write('TAA'+'\t'+str(mito_TAA_pos)+'\n')
output.write('TAG'+'\t'+str(mito_TAG_pos)+'\n')
output.write('AGA'+'\t'+str(mito_AGA_pos)+'\n')
output.write('AGG'+'\t'+str(mito_AGG_pos)+'\n')

output.write('\n')

output.close()

