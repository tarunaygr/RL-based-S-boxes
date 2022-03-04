import numpy as np

rules,names=funcs_m3.return_rules()
# print(names)
def rule_op(rule,nb_size,ca_len,ca):
  ops=[]
  for i in range(0,ca_len,nb_size):
    ops.append(rule(ca[i:i+nb_size+1]))
  res=0
  for op in ops:
    res^=op
  return res


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

def decimalToBinary(n):
    return "{0:09b}".format(int(n))
  
def BinaryTodecimal(bit_list):
  dec=0
  for bit in bit_list:
    dec=(dec<<1)|bit
  return dec

ip,op=Sbox(rules)
# print(op)
for i in range(len(names)):
    
    r=[t[i] for t in op]
    if(np.array(r).sum()==128):
        print(names[i])
