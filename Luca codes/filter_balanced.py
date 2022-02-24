import os

for filename in os.listdir('experiments/enumeration_quadratic_rules'):

    with open('experiments/enumeration_quadratic_rules/'+filename, 'r') as fin, \
            open('filtered_'+filename, 'w') as fout:
        
        lines = fin.readlines()
        for i, line in enumerate(lines):
            
            if 'Rule' in line:

                rule_ok = True
                line_idx = i+1
                
                while rule_ok and line_idx < len(lines) and 'Size' in lines[line_idx]:

                    if r'BAL: false' in lines[line_idx]:
                        rule_ok = False

                    line_idx += 1

                if rule_ok:
                    fout.write(lines[i])


