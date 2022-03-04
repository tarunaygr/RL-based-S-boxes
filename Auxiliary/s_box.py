from cmath import inf
import numpy as np
import matplotlib.pyplot as plt
import sys
import itertools
from . import funcs_filtered_outputs_m_3 as m3
# import Auxiliary.funcs_filtered_outputs_m_4 as m4
# import Auxiliary.funcs_filtered_outputs_m_5 as m5
# import Auxiliary.funcs_filtered_outputs_m_6 as m6

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
# Returns:
# Output bit after running the rule and XORing the results
def rule_op(rule,nb_size,ca_len,ca):
  ops=[]
  for i in range(len(ca)-nb_size+1):
    nbr=[]
    for j in range(nb_size):
      nbr.append(ca[i+j])
  ops.append(rule(nbr))
  res=0
  for op in ops:
    res^=op
  return res

#CA Rules Definitions which we run on the Cellular Automata. These are rules of neighbourhood size 3
rule_list,rule_names= m3.return_rules()
# rules=[m3.rule_178,m3.rule_92,m3.rule_154,m3.rule_18,m3.rule_68,m3.rule_172,m3.rule_222,m3.rule_46]
# rules=rule_list[:8]

# Function to emulate the output of the S-box. It outputs the inputs and corresponding outputs in a bit list form.
# Parameters:
# rules - The list of CA rules which we will run.
# Returns:
# inputs - All possible inputs tried in the s-box
# outputs - Outputs for the correspoding values of input

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

# Function to check the bijectivity of the s-box function. Returns 1 if bijective, 0 if not
# Parameters:
# decimal_repr - Decimal Representation of the outputs produced by S-box
# Return:
# 1 if the s-box is bijective. 0 otherwise
def bijectivity(decimal_repr):
  len_ops=len(decimal_repr)
  len_distinct=len(set(decimal_repr))
  if (len_ops==len_distinct):
    print("It is Bijective")
    return 1
  else:
    print("Not Bijective")
    return 0


# Function to Calculate the Difference Distribution Table of the S-box function and returns its differential uniformity
# Parameters:
# decimal_repr - Decimal Representation of the outputs produced by S-box
# Returns:
# The maximum value in the DDT ( the differential uniformity of the s-box)
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

def innerprod(a,x):
  res=0
  if (len(x)!=len(a)):
    print(f"SIZE a={len(a)} SIZE x={len(x)}")
  for i in range(len(a)):
    res^=((a[i]*x[i])%2)
  return res

#The function to calcute the WHT of the s-box for given values of u,v
# Parameters:
# u,v
# inarray - 2D array with all possible inputs to the s-box
# outarray - 2D array with the corresponding outputs for the inputs 
# Returns:
# WHT value 
def WHT_Calc(u,v,inarray,outarray):
  WHT=0
  for i in range(len(inarray)):
    x=innerprod(v,outarray[i])
    y=innerprod(u,inarray[i])
    WHT+=pow(-1,x^y)
  # print(f'u={u} v={v} WHT={WHT}')
  return WHT

# Function to find the max value of WHT over all the values of u,v
# Parameters:
# inarray - 2D array with all possible inputs to the s-box
# outarray - 2D array with the corresponding outputs for the inputs 
# Returns:
# the maximum value of WHT

def get_WHT_spectrum(inarray,outarray):
  
  input_binaries=[]
  for i in range(256):
    input_binaries.append(list(map(int, str(decimalToBinary(i)))))
  v_vals = input_binaries.copy()[1:]
  u_vals = input_binaries.copy()
  # v_vals=v_vals[1:]
  # u_vals=u_vals[1:]
  max=-inf
  for u in u_vals:
    for v in v_vals:
      WHT_curr=abs(WHT_Calc(u,v,inarray,outarray))
      if (WHT_curr>max):
        # print(f'U={u} V={v} WHY ={WHT_curr}')
        max=WHT_curr
  return max
      
def get_WHT_spectrum(inarray,outarray):
  v_vals = list(itertools.product([0, 1], repeat=8))
  u_vals = list(itertools.product([0, 1], repeat=8))
  v_vals=v_vals[1:]
  # u_vals=u_vals[1:]
  max=-inf
  for u in u_vals:
    for v in v_vals:
      WHT_curr=abs(WHT_Calc(u,v,inarray,outarray))
      if (WHT_curr>max):
        # print(f'U={u} V={v} WHY ={WHT_curr}')
        max=WHT_curr
  return max
      
# Function to Calculate the Nonlinearity of the s-box
# Parameters: 
# inarray - 2D array with all possible inputs to the s-box
# outarray - 2D array with the corresponding outputs for the inputs 
# n - The size of each input (8 here)
# Returns;
# Nonlinearity of the s-box
def NLcalc(inarray,outarray,n):
  wht=get_WHT_spectrum(inarray,outarray)
  # print(f'wht={wht}')
  NL = pow(2,n-1) - wht/2
  return NL

# Function to calculate the cryptographic strength of an s-box.
# Parameters:
# rules -  the set of rules to run the sbox
# Returns:
# The strength of the s-box according to our formulation
def state_crypto_strength(rules_index):
  print("Current State Checking Strength")
  print(rules_index)
  rules=[ rule_list[i]  for i in rules_index]
  inarray,outarray = Sbox(rules)
  print("INARRAY")
  for i in inarray:
    if(len(i)!=8):
      print(i)
  print("OUTARRAY")
  for i in outarray:
    if(len(i)!=8):
      print(i)
  decimal_repr=[]
  for bit_list in outarray:
    decimal_repr.append(BinaryTodecimal(bit_list))
  DU = diff_uniformity(decimal_repr)
  NL = NLcalc(inarray,outarray,8)
  print(f"DU = {str(DU)} NL={str(NL)}")
  normalised_NL = (NL/112)*100
  DU1 = ((DU-4)/(128-4))*100
  normalised_DU = 100 - DU1
  reward = (normalised_NL + normalised_DU)/2
  
  return reward
  
# Function to calculate the immediate reward for a particular state transition.
# Parameters:
# rule1 - the initial state of the s-box
# rule2 - the final state of the s-box
# Returns:
# The immediate reward achieved by the transition
def state_transition_reward(rule1, rule2):
  return state_crypto_strength(rule2) - state_crypto_strength(rule1)
