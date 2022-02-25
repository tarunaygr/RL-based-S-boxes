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

def return_rules():
    return rules,names