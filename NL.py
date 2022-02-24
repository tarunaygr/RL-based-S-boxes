#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import matplotlib.pyplot as plt
import sys
import itertools
from matplotlib.pyplot import figure


# In[1]:


print("hello")


# In[9]:


rules=[]
names=[]
def rule_136(ip):
	return ((ip[0]&ip[1]))

rules.append(rule_136)
names.append("rule_136")
def rule_34(ip):
	return (ip[0]^(ip[0]&ip[1]))

rules.append(rule_34)
names.append("rule_34")
def rule_68(ip):
	return (ip[1]^(ip[0]&ip[1]))

rules.append(rule_68)
names.append("rule_68")
def rule_238(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1]))

rules.append(rule_238)
names.append("rule_238")
def rule_120(ip):
	return ((ip[0]&ip[1])^ip[2])

rules.append(rule_120)
names.append("rule_120")
def rule_210(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2])

rules.append(rule_210)
names.append("rule_210")
def rule_180(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2])

rules.append(rule_180)
names.append("rule_180")
def rule_30(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2])

rules.append(rule_30)
names.append("rule_30")
def rule_160(ip):
	return ((ip[0]&ip[2]))

rules.append(rule_160)
names.append("rule_160")
def rule_10(ip):
	return (ip[0]^(ip[0]&ip[2]))

rules.append(rule_10)
names.append("rule_10")
def rule_108(ip):
	return (ip[1]^(ip[0]&ip[2]))

rules.append(rule_108)
names.append("rule_108")
def rule_198(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2]))

rules.append(rule_198)
names.append("rule_198")
def rule_80(ip):
	return (ip[2]^(ip[0]&ip[2]))

rules.append(rule_80)
names.append("rule_80")
def rule_250(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2]))

rules.append(rule_250)
names.append("rule_250")
def rule_156(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2]))

rules.append(rule_156)
names.append("rule_156")
def rule_54(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2]))

rules.append(rule_54)
names.append("rule_54")
def rule_40(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2]))

rules.append(rule_40)
names.append("rule_40")
def rule_130(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2]))

rules.append(rule_130)
names.append("rule_130")
def rule_228(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2]))

rules.append(rule_228)
names.append("rule_228")
def rule_78(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2]))

rules.append(rule_78)
names.append("rule_78")
def rule_216(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2]))

rules.append(rule_216)
names.append("rule_216")
def rule_114(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2]))

rules.append(rule_114)
names.append("rule_114")
def rule_20(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2]))

rules.append(rule_20)
names.append("rule_20")
def rule_190(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2]))

rules.append(rule_190)
names.append("rule_190")
def rule_192(ip):
	return ((ip[1]&ip[2]))

rules.append(rule_192)
names.append("rule_192")
def rule_106(ip):
	return (ip[0]^(ip[1]&ip[2]))

rules.append(rule_106)
names.append("rule_106")
def rule_12(ip):
	return (ip[1]^(ip[1]&ip[2]))

rules.append(rule_12)
names.append("rule_12")
def rule_166(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2]))

rules.append(rule_166)
names.append("rule_166")
def rule_48(ip):
	return (ip[2]^(ip[1]&ip[2]))

rules.append(rule_48)
names.append("rule_48")
def rule_154(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2]))

rules.append(rule_154)
names.append("rule_154")
def rule_252(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2]))

rules.append(rule_252)
names.append("rule_252")
def rule_86(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2]))

rules.append(rule_86)
names.append("rule_86")
def rule_72(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2]))

rules.append(rule_72)
names.append("rule_72")
def rule_226(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2]))

rules.append(rule_226)
names.append("rule_226")
def rule_132(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2]))

rules.append(rule_132)
names.append("rule_132")
def rule_46(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2]))

rules.append(rule_46)
names.append("rule_46")
def rule_184(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2]))

rules.append(rule_184)
names.append("rule_184")
def rule_18(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2]))

rules.append(rule_18)
names.append("rule_18")
def rule_116(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2]))

rules.append(rule_116)
names.append("rule_116")
def rule_222(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2]))

rules.append(rule_222)
names.append("rule_222")
def rule_96(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_96)
names.append("rule_96")
def rule_202(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_202)
names.append("rule_202")
def rule_172(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_172)
names.append("rule_172")
def rule_6(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_6)
names.append("rule_6")
def rule_144(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_144)
names.append("rule_144")
def rule_58(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_58)
names.append("rule_58")
def rule_92(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_92)
names.append("rule_92")
def rule_246(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_246)
names.append("rule_246")
def rule_232(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_232)
names.append("rule_232")
def rule_66(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_66)
names.append("rule_66")
def rule_36(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_36)
names.append("rule_36")
def rule_142(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_142)
names.append("rule_142")
def rule_24(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_24)
names.append("rule_24")
def rule_178(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_178)
names.append("rule_178")
def rule_212(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_212)
names.append("rule_212")
def rule_126(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_126)
names.append("rule_126")


# In[19]:


rules[1]


# In[4]:


import sys
file=sys.argv[1]
with open(file,'r') as fin:
    
    lines=fin.readlines()

with open('funcs_'+file+'.py','w') as fout:
    fout.write('rules=[]\n')
    fout.write('names=[]\n')
    for line in lines:
        if 'Rule' in line:
            number=line.split('-')[0][5:-1]
            
            fout.write(f'def rule_{number}(ip):\n\treturn (')
            eqn=line.split('=')[1].split('N')[0][1:-1].replace(' ','')
            print(eqn)
            monomials=eqn.split('+')
            for j,m in enumerate(monomials):
                m=m.split('x')[1:]
                for i,s in enumerate(m): 
                    if(len(m)>1 and i==0):
                        fout.write('(')
                    if(i>0):
                        fout.write('&')                   
                    if(s=='1'):
                        fout.write('ip[0]')
                    elif(s=='2'):
                        fout.write('ip[1]')
                    elif(s=='3'):
                        fout.write('ip[2]')
                    elif(s=='4'):
                        fout.write('ip[3]')
                    elif(s=='5'):
                        fout.write('ip[4]')
                    elif(s=='6'):
                        fout.write('ip[5]')
                    if(i==len(m)-1 and len(m)>1):
                        fout.write(')')
                if(j!=len(monomials)-1):
                    fout.write('^')
            fout.write(')\n\n')
            fout.write(f'rules.append(rule_{number})\n')
            fout.write(f'names.append("rule_{number}")\n')


# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import sys
import itertools
from matplotlib.pyplot import figure
import Auxiliary.funcs_m3 as m3

#Helper Functions

# Convert a decimal number into a corresponding array of bit values
def decimalToBinary(n): 
    return "{0:09b}".format(int(n))
  
# Convert the binary representation array into the corresponding decimal value
def BinaryTodecimal(bit_list):
  dec=0
  for bit in bit_list:
    dec=(dec<<1)|bit
  return dec

# Function which runs the CA rule over the CA and xors the rule outputs and returns a single bit value 
# Parameters:
# rule - the list of CA rules to be run on the CA
# nb_size - Size of the neighbourhood considered
# ca_len  - Number of cells in the Cellular Automata
# ca  - The input CA configuration to run the rules on

def rule_op(rule,nb_size,ca_len,ca):
  ops=[]
  for i in range(0,ca_len,nb_size):
    ops.append(rule(ca[i:i+nb_size+1]))
  res=0
  for op in ops:
    res^=op
  return res

#CA Rules Definitions which we run on the Cellular Automata. These are rules of neighbourhood size 3
rule_list,rule_names= m3.return_rules()

rules=[m3.rule_210,m3.rule_108,m3.rule_68,m3.rule_238,m3.rule_120,m3.rule_180,m3.rule_30,m3.rule_92]
# rules=rule_list[:8]

# Function to emulate the output of the S-box. It outputs the inputs and corresponding outputs in a bit list form.
# Parameters:
# rules - The list of CA rules which we will run.

def Sbox(rules):
  inputs=[]
  outputs=[]
  for i in range(256):
    res = list(map(int, str(decimalToBinary(i))))
    
    inputs.append(res[1:])
    op=[]
    for rule in rules:
      op.append(rule_op(rule,3,8,res))
    outputs.append(op)
    # print(f'{res[1:]} ->{op}')
  return inputs,outputs

inputs,outputs=Sbox(rules)
# We convert the bit list of outputs into decimal values
decimal_repr=[]
for bit_list in outputs:
  decimal_repr.append(BinaryTodecimal(bit_list))

figure(figsize=(10,6))
plt.hist(decimal_repr,bins=256);

# Function to check the bijectivity of the s-box function. Returns 1 if bijective, 0 if not
# Parameters:
# decimal_repr - Decimal Representation of the outputs produced by S-box
def bijectivity(decimal_repr):
  len_ops=len(decimal_repr)
  len_distinct=len(set(decimal_repr))
  if (len_ops==len_distinct):
    print("It is Bijective")
    return 1
  else:
    print("Not Bijective")
    return 0

bijectivity(decimal_repr)

# Function to Calculate the difference Distribution Table of the S-box function and returns its differential uniformity
# Parameters:
# decimal_repr - Decimal Representation of the outputs produced by S-box
def diff_uniformity(decimal_repr):
  ddt=np.zeros((256,256))
  for a in range(256):
    for x in range(256):
      sum=x^a
      F1=decimal_repr[sum]
      F2=decimal_repr[x]
      b=F1^F2
      ddt[a][b]+=1
  for i in range(256):
    ddt[i][i]=0
  ddt[0]=np.zeros(256)
  return (np.amax(ddt))

diff_uniformity(decimal_repr)


# In[20]:


import itertools
lst = list(itertools.product([0, 1], repeat=8))


# In[21]:


lst


# In[22]:


def dotprod(a,x):
    for i in range(len(a)):
        if a[i] == 1:
            b[i] = x[i]
        else:
            b[i] = 0
    return b


# In[25]:


def WHTcalc(sinput, soutput,i):
    v = list(itertools.product([0, 1], repeat=8))
    u = list(itertools.product([0, 1], repeat=8))
    x = sinput
    f_x = soutput
    for i in range(len(v)):
        for j in range(len(omega)):
            WHT[i] += pow((-1),np.bitwise_xor(dotprod(v,f_x),dotprod(u,x)))        
    return WHT
    


# In[ ]:


def NLcalc(WHT):
    NL = pow(2,7) - (0.5)*np.max(WHT)
    

