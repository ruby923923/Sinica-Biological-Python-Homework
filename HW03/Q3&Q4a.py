#!/usr/bin/env python
# coding: utf-8

# In[16]:


import sys 

#function
def get_any_percent(seq, letters, sig_digits=2):
    for i in seq:
        if '>' in i:
            print(i.strip())
            continue
        else:
            seq_len =len(i)
            assert seq_len != 0,'sequence not existence'
            x = i.upper().strip()
            
            total_letters = 0
            
            for l in letters:
                l = l.upper()
                
                #check if l is ATCG 
                DNA_bases = ['A','T','C','G']
                if (l not in DNA_bases):
                    print('letter ['+ l +'] not DNA base!')
                assert l in DNA_bases,'not DNA base'
                    
                total_letters += x.count(l)
    
            proportion = total_letters/seq_len
            proportion_rounded = round(proportion, sig_digits)
    
        print (str(letters) + ' proportion = '+ str(proportion_rounded))
    return

#main
with open(sys.argv[1],'r') as fh:
    f_list = fh.readlines()
    
get_any_percent(f_list,str(sys.argv[2]))


# In[ ]:




