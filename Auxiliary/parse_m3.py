import sys

with open('outputs_m_6.txt','r') as fin:
    
    lines=fin.readlines()

with open('funcs_m6.py','w') as fout:
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
            

