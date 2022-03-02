from scipy.fft import set_backend
import Auxiliary.s_box as sbox
import Auxiliary.funcs_filtered_outputs_m_3 as m3
from datetime import datetime
rules_list,rule_names=m3.return_rules()

rules=[m3.rule_178,m3.rule_92,m3.rule_154,m3.rule_18,m3.rule_68,m3.rule_172,m3.rule_222,m3.rule_46]

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
for i in range(8):
    rule_test=rules.copy()
    for rule in rules_list:
        rule_test[i]=rule
        sbox.state_crypto_strength(rule_test)

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)