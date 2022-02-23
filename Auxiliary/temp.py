d=2
m=2
n=8


set_d=[]
for i in range(1,m+1):
  set_d.append(i)
set_d=set(set_d)


I=[]
for i in range(d+1):
  I.append(findsubsets(set_d,i))
# print(I)

anf_coef=np.zeros(2**m)
indexed_subsets=[j for sub in I for j in sub]
# print(indexed_subsets)
# print(len(I[2]))
L=[]

T=[]
for i in range(1,(len(I[2])+1)):
  T.append(findsubsets(I[2],i))
T=[j for sub in T for j in sub]
# T.insert(0,[])
# print(T)

P=[]
print()
one_dim=np.array(list(map(list,I[1]))).flatten()
for i in range(1,len(one_dim)+1):
  P.append(findsubsets(one_dim,i))
  # print(P)
P=[j for sub in P for j in sub]
print(P)

for t in T:
  for x in t:
    index=indexed_subsets.index(x)
    anf_coef[index]=1
  for p in P:
    cond = indexed_subsets

  
  
  
  def rule_210(ip):
  res=(ip[0]^(ip[0]&ip[1])^ip[2])
  return res

def rule_108(ip):
  return (ip[1]^(ip[0]&ip[2]))

def rule_68(ip):
  return (ip[1]^(ip[0]&ip[1]))

def rule_238(ip):
  return (ip[0]^ip[1]^(ip[0]&ip[1]))

def rule_120(ip):
  return ((ip[0]&ip[1])^ip[2])

def rule_180(ip):
  return (ip[1]^(ip[0]&ip[1])^ip[2])

def rule_30(ip):
  return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2])

def rule_92(ip):
  return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))