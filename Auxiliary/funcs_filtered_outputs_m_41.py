rules=[]
names=[]
def rule_34952(ip):
	return ((ip[0]&ip[1]))

rules.append(rule_34952)
names.append("rule_34952")
def rule_8738(ip):
	return (ip[0]^(ip[0]&ip[1]))

rules.append(rule_8738)
names.append("rule_8738")
def rule_17476(ip):
	return (ip[1]^(ip[0]&ip[1]))

rules.append(rule_17476)
names.append("rule_17476")
def rule_61166(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1]))

rules.append(rule_61166)
names.append("rule_61166")
def rule_30840(ip):
	return ((ip[0]&ip[1])^ip[2])

rules.append(rule_30840)
names.append("rule_30840")
def rule_53970(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2])

rules.append(rule_53970)
names.append("rule_53970")
def rule_46260(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2])

rules.append(rule_46260)
names.append("rule_46260")
def rule_7710(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2])

rules.append(rule_7710)
names.append("rule_7710")
def rule_30600(ip):
	return ((ip[0]&ip[1])^ip[3])

rules.append(rule_30600)
names.append("rule_30600")
def rule_56610(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[3])

rules.append(rule_56610)
names.append("rule_56610")
def rule_47940(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[3])

rules.append(rule_47940)
names.append("rule_47940")
def rule_4590(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[3])

rules.append(rule_4590)
names.append("rule_4590")
def rule_34680(ip):
	return ((ip[0]&ip[1])^ip[2]^ip[3])

rules.append(rule_34680)
names.append("rule_34680")
def rule_11730(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^ip[3])

rules.append(rule_11730)
names.append("rule_11730")
def rule_19380(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^ip[3])

rules.append(rule_19380)
names.append("rule_19380")
def rule_57630(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^ip[3])

rules.append(rule_57630)
names.append("rule_57630")
def rule_41120(ip):
	return ((ip[0]&ip[2]))

rules.append(rule_41120)
names.append("rule_41120")
def rule_2570(ip):
	return (ip[0]^(ip[0]&ip[2]))

rules.append(rule_2570)
names.append("rule_2570")
def rule_27756(ip):
	return (ip[1]^(ip[0]&ip[2]))

rules.append(rule_27756)
names.append("rule_27756")
def rule_50886(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2]))

rules.append(rule_50886)
names.append("rule_50886")
def rule_20560(ip):
	return (ip[2]^(ip[0]&ip[2]))

rules.append(rule_20560)
names.append("rule_20560")
def rule_64250(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2]))

rules.append(rule_64250)
names.append("rule_64250")
def rule_40092(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2]))

rules.append(rule_40092)
names.append("rule_40092")
def rule_13878(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2]))

rules.append(rule_13878)
names.append("rule_13878")
def rule_24480(ip):
	return ((ip[0]&ip[2])^ip[3])

rules.append(rule_24480)
names.append("rule_24480")
def rule_62730(ip):
	return (ip[0]^(ip[0]&ip[2])^ip[3])

rules.append(rule_62730)
names.append("rule_62730")
def rule_37740(ip):
	return (ip[1]^(ip[0]&ip[2])^ip[3])

rules.append(rule_37740)
names.append("rule_37740")
def rule_14790(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^ip[3])

rules.append(rule_14790)
names.append("rule_14790")
def rule_44880(ip):
	return (ip[2]^(ip[0]&ip[2])^ip[3])

rules.append(rule_44880)
names.append("rule_44880")
def rule_1530(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^ip[3])

rules.append(rule_1530)
names.append("rule_1530")
def rule_25500(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^ip[3])

rules.append(rule_25500)
names.append("rule_25500")
def rule_51510(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^ip[3])

rules.append(rule_51510)
names.append("rule_51510")
def rule_10280(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2]))

rules.append(rule_10280)
names.append("rule_10280")
def rule_33410(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2]))

rules.append(rule_33410)
names.append("rule_33410")
def rule_58596(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2]))

rules.append(rule_58596)
names.append("rule_58596")
def rule_20046(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2]))

rules.append(rule_20046)
names.append("rule_20046")
def rule_55512(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2]))

rules.append(rule_55512)
names.append("rule_55512")
def rule_29298(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2]))

rules.append(rule_29298)
names.append("rule_29298")
def rule_5140(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2]))

rules.append(rule_5140)
names.append("rule_5140")
def rule_48830(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2]))

rules.append(rule_48830)
names.append("rule_48830")
def rule_55080(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^ip[3])

rules.append(rule_55080)
names.append("rule_55080")
def rule_32130(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3])

rules.append(rule_32130)
names.append("rule_32130")
def rule_7140(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3])

rules.append(rule_7140)
names.append("rule_7140")
def rule_45390(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3])

rules.append(rule_45390)
names.append("rule_45390")
def rule_10200(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3])

rules.append(rule_10200)
names.append("rule_10200")
def rule_36210(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3])

rules.append(rule_36210)
names.append("rule_36210")
def rule_60180(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3])

rules.append(rule_60180)
names.append("rule_60180")
def rule_16830(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3])

rules.append(rule_16830)
names.append("rule_16830")
def rule_49344(ip):
	return ((ip[1]&ip[2]))

rules.append(rule_49344)
names.append("rule_49344")
def rule_27242(ip):
	return (ip[0]^(ip[1]&ip[2]))

rules.append(rule_27242)
names.append("rule_27242")
def rule_3084(ip):
	return (ip[1]^(ip[1]&ip[2]))

rules.append(rule_3084)
names.append("rule_3084")
def rule_42662(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2]))

rules.append(rule_42662)
names.append("rule_42662")
def rule_12336(ip):
	return (ip[2]^(ip[1]&ip[2]))

rules.append(rule_12336)
names.append("rule_12336")
def rule_39578(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2]))

rules.append(rule_39578)
names.append("rule_39578")
def rule_64764(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2]))

rules.append(rule_64764)
names.append("rule_64764")
def rule_22102(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2]))

rules.append(rule_22102)
names.append("rule_22102")
def rule_16320(ip):
	return ((ip[1]&ip[2])^ip[3])

rules.append(rule_16320)
names.append("rule_16320")
def rule_38250(ip):
	return (ip[0]^(ip[1]&ip[2])^ip[3])

rules.append(rule_38250)
names.append("rule_38250")
def rule_62220(ip):
	return (ip[1]^(ip[1]&ip[2])^ip[3])

rules.append(rule_62220)
names.append("rule_62220")
def rule_22950(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^ip[3])

rules.append(rule_22950)
names.append("rule_22950")
def rule_53040(ip):
	return (ip[2]^(ip[1]&ip[2])^ip[3])

rules.append(rule_53040)
names.append("rule_53040")
def rule_26010(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^ip[3])

rules.append(rule_26010)
names.append("rule_26010")
def rule_1020(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^ip[3])

rules.append(rule_1020)
names.append("rule_1020")
def rule_43350(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^ip[3])

rules.append(rule_43350)
names.append("rule_43350")
def rule_18504(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2]))

rules.append(rule_18504)
names.append("rule_18504")
def rule_58082(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2]))

rules.append(rule_58082)
names.append("rule_58082")
def rule_33924(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2]))

rules.append(rule_33924)
names.append("rule_33924")
def rule_11822(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2]))

rules.append(rule_11822)
names.append("rule_11822")
def rule_47288(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2]))

rules.append(rule_47288)
names.append("rule_47288")
def rule_4626(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2]))

rules.append(rule_4626)
names.append("rule_4626")
def rule_29812(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2]))

rules.append(rule_29812)
names.append("rule_29812")
def rule_57054(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2]))

rules.append(rule_57054)
names.append("rule_57054")
def rule_46920(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^ip[3])

rules.append(rule_46920)
names.append("rule_46920")
def rule_7650(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3])

rules.append(rule_7650)
names.append("rule_7650")
def rule_31620(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3])

rules.append(rule_31620)
names.append("rule_31620")
def rule_53550(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3])

rules.append(rule_53550)
names.append("rule_53550")
def rule_18360(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3])

rules.append(rule_18360)
names.append("rule_18360")
def rule_60690(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3])

rules.append(rule_60690)
names.append("rule_60690")
def rule_35700(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3])

rules.append(rule_35700)
names.append("rule_35700")
def rule_8670(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3])

rules.append(rule_8670)
names.append("rule_8670")
def rule_24672(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_24672)
names.append("rule_24672")
def rule_51914(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_51914)
names.append("rule_51914")
def rule_44204(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_44204)
names.append("rule_44204")
def rule_1542(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_1542)
names.append("rule_1542")
def rule_37008(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_37008)
names.append("rule_37008")
def rule_14906(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_14906)
names.append("rule_14906")
def rule_23644(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_23644)
names.append("rule_23644")
def rule_63222(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_63222)
names.append("rule_63222")
def rule_40800(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_40800)
names.append("rule_40800")
def rule_13770(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_13770)
names.append("rule_13770")
def rule_21420(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_21420)
names.append("rule_21420")
def rule_63750(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_63750)
names.append("rule_63750")
def rule_28560(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_28560)
names.append("rule_28560")
def rule_50490(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_50490)
names.append("rule_50490")
def rule_41820(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_41820)
names.append("rule_41820")
def rule_2550(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_2550)
names.append("rule_2550")
def rule_59624(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_59624)
names.append("rule_59624")
def rule_16962(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_16962)
names.append("rule_16962")
def rule_9252(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_9252)
names.append("rule_9252")
def rule_36494(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_36494)
names.append("rule_36494")
def rule_6168(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_6168)
names.append("rule_6168")
def rule_45746(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_45746)
names.append("rule_45746")
def rule_54484(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_54484)
names.append("rule_54484")
def rule_32382(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2]))

rules.append(rule_32382)
names.append("rule_32382")
def rule_6120(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_6120)
names.append("rule_6120")
def rule_48450(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_48450)
names.append("rule_48450")
def rule_56100(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_56100)
names.append("rule_56100")
def rule_29070(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_29070)
names.append("rule_29070")
def rule_59160(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_59160)
names.append("rule_59160")
def rule_19890(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_19890)
names.append("rule_19890")
def rule_11220(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_11220)
names.append("rule_11220")
def rule_33150(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3])

rules.append(rule_33150)
names.append("rule_33150")
def rule_43520(ip):
	return ((ip[0]&ip[3]))

rules.append(rule_43520)
names.append("rule_43520")
def rule_170(ip):
	return (ip[0]^(ip[0]&ip[3]))

rules.append(rule_170)
names.append("rule_170")
def rule_26316(ip):
	return (ip[1]^(ip[0]&ip[3]))

rules.append(rule_26316)
names.append("rule_26316")
def rule_52326(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[3]))

rules.append(rule_52326)
names.append("rule_52326")
def rule_23280(ip):
	return (ip[2]^(ip[0]&ip[3]))

rules.append(rule_23280)
names.append("rule_23280")
def rule_61530(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[3]))

rules.append(rule_61530)
names.append("rule_61530")
def rule_38460(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[3]))

rules.append(rule_38460)
names.append("rule_38460")
def rule_15510(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[3]))

rules.append(rule_15510)
names.append("rule_15510")
def rule_21760(ip):
	return (ip[3]^(ip[0]&ip[3]))

rules.append(rule_21760)
names.append("rule_21760")
def rule_65450(ip):
	return (ip[0]^ip[3]^(ip[0]&ip[3]))

rules.append(rule_65450)
names.append("rule_65450")
def rule_39372(ip):
	return (ip[1]^ip[3]^(ip[0]&ip[3]))

rules.append(rule_39372)
names.append("rule_39372")
def rule_13158(ip):
	return (ip[0]^ip[1]^ip[3]^(ip[0]&ip[3]))

rules.append(rule_13158)
names.append("rule_13158")
def rule_42480(ip):
	return (ip[2]^ip[3]^(ip[0]&ip[3]))

rules.append(rule_42480)
names.append("rule_42480")
def rule_3930(ip):
	return (ip[0]^ip[2]^ip[3]^(ip[0]&ip[3]))

rules.append(rule_3930)
names.append("rule_3930")
def rule_26940(ip):
	return (ip[1]^ip[2]^ip[3]^(ip[0]&ip[3]))

rules.append(rule_26940)
names.append("rule_26940")
def rule_50070(ip):
	return (ip[0]^ip[1]^ip[2]^ip[3]^(ip[0]&ip[3]))

rules.append(rule_50070)
names.append("rule_50070")
def rule_8840(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[3]))

rules.append(rule_8840)
names.append("rule_8840")
def rule_34850(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[3]))

rules.append(rule_34850)
names.append("rule_34850")
def rule_60996(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[3]))

rules.append(rule_60996)
names.append("rule_60996")
def rule_17646(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[3]))

rules.append(rule_17646)
names.append("rule_17646")
def rule_53880(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[3]))

rules.append(rule_53880)
names.append("rule_53880")
def rule_30930(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[3]))

rules.append(rule_30930)
names.append("rule_30930")
def rule_7860(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[3]))

rules.append(rule_7860)
names.append("rule_7860")
def rule_46110(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[3]))

rules.append(rule_46110)
names.append("rule_46110")
def rule_56712(ip):
	return ((ip[0]&ip[1])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_56712)
names.append("rule_56712")
def rule_30498(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_30498)
names.append("rule_30498")
def rule_4420(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_4420)
names.append("rule_4420")
def rule_48110(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_48110)
names.append("rule_48110")
def rule_11640(ip):
	return ((ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3]))

rules.append(rule_11640)
names.append("rule_11640")
def rule_34770(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3]))

rules.append(rule_34770)
names.append("rule_34770")
def rule_57780(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3]))

rules.append(rule_57780)
names.append("rule_57780")
def rule_19230(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3]))

rules.append(rule_19230)
names.append("rule_19230")
def rule_2720(ip):
	return ((ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_2720)
names.append("rule_2720")
def rule_40970(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_40970)
names.append("rule_40970")
def rule_50796(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_50796)
names.append("rule_50796")
def rule_27846(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_27846)
names.append("rule_27846")
def rule_64080(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_64080)
names.append("rule_64080")
def rule_20730(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_20730)
names.append("rule_20730")
def rule_13980(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_13980)
names.append("rule_13980")
def rule_39990(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_39990)
names.append("rule_39990")
def rule_62880(ip):
	return ((ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_62880)
names.append("rule_62880")
def rule_24330(ip):
	return (ip[0]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_24330)
names.append("rule_24330")
def rule_14700(ip):
	return (ip[1]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_14700)
names.append("rule_14700")
def rule_37830(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_37830)
names.append("rule_37830")
def rule_1360(ip):
	return (ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_1360)
names.append("rule_1360")
def rule_45050(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_45050)
names.append("rule_45050")
def rule_51612(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_51612)
names.append("rule_51612")
def rule_25398(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_25398)
names.append("rule_25398")
def rule_33320(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_33320)
names.append("rule_33320")
def rule_10370(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_10370)
names.append("rule_10370")
def rule_20196(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_20196)
names.append("rule_20196")
def rule_58446(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_58446)
names.append("rule_58446")
def rule_29400(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_29400)
names.append("rule_29400")
def rule_55410(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_55410)
names.append("rule_55410")
def rule_48660(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_48660)
names.append("rule_48660")
def rule_5310(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_5310)
names.append("rule_5310")
def rule_32040(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_32040)
names.append("rule_32040")
def rule_55170(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_55170)
names.append("rule_55170")
def rule_45540(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_45540)
names.append("rule_45540")
def rule_6990(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_6990)
names.append("rule_6990")
def rule_36312(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_36312)
names.append("rule_36312")
def rule_10098(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_10098)
names.append("rule_10098")
def rule_16660(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_16660)
names.append("rule_16660")
def rule_60350(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_60350)
names.append("rule_60350")
def rule_27328(ip):
	return ((ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_27328)
names.append("rule_27328")
def rule_49258(ip):
	return (ip[0]^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_49258)
names.append("rule_49258")
def rule_42508(ip):
	return (ip[1]^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_42508)
names.append("rule_42508")
def rule_3238(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_3238)
names.append("rule_3238")
def rule_39472(ip):
	return (ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_39472)
names.append("rule_39472")
def rule_12442(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_12442)
names.append("rule_12442")
def rule_22268(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_22268)
names.append("rule_22268")
def rule_64598(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_64598)
names.append("rule_64598")
def rule_38336(ip):
	return ((ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_38336)
names.append("rule_38336")
def rule_16234(ip):
	return (ip[0]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_16234)
names.append("rule_16234")
def rule_22796(ip):
	return (ip[1]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_22796)
names.append("rule_22796")
def rule_62374(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_62374)
names.append("rule_62374")
def rule_25904(ip):
	return (ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_25904)
names.append("rule_25904")
def rule_53146(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_53146)
names.append("rule_53146")
def rule_43516(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_43516)
names.append("rule_43516")
def rule_854(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_854)
names.append("rule_854")
def rule_57928(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_57928)
names.append("rule_57928")
def rule_18658(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_18658)
names.append("rule_18658")
def rule_11908(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_11908)
names.append("rule_11908")
def rule_33838(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_33838)
names.append("rule_33838")
def rule_4792(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_4792)
names.append("rule_4792")
def rule_47122(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_47122)
names.append("rule_47122")
def rule_56948(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_56948)
names.append("rule_56948")
def rule_29918(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_29918)
names.append("rule_29918")
def rule_7496(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_7496)
names.append("rule_7496")
def rule_47074(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_47074)
names.append("rule_47074")
def rule_53636(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_53636)
names.append("rule_53636")
def rule_31534(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_31534)
names.append("rule_31534")
def rule_60856(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_60856)
names.append("rule_60856")
def rule_18194(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_18194)
names.append("rule_18194")
def rule_8564(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_8564)
names.append("rule_8564")
def rule_35806(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_35806)
names.append("rule_35806")
def rule_51808(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_51808)
names.append("rule_51808")
def rule_24778(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_24778)
names.append("rule_24778")
def rule_1708(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_1708)
names.append("rule_1708")
def rule_44038(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_44038)
names.append("rule_44038")
def rule_14992(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_14992)
names.append("rule_14992")
def rule_36922(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_36922)
names.append("rule_36922")
def rule_63068(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_63068)
names.append("rule_63068")
def rule_23798(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_23798)
names.append("rule_23798")
def rule_13664(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_13664)
names.append("rule_13664")
def rule_40906(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_40906)
names.append("rule_40906")
def rule_63916(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_63916)
names.append("rule_63916")
def rule_21254(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_21254)
names.append("rule_21254")
def rule_50576(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_50576)
names.append("rule_50576")
def rule_28474(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_28474)
names.append("rule_28474")
def rule_2396(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_2396)
names.append("rule_2396")
def rule_41974(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_41974)
names.append("rule_41974")
def rule_17128(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_17128)
names.append("rule_17128")
def rule_59458(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_59458)
names.append("rule_59458")
def rule_36388(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_36388)
names.append("rule_36388")
def rule_9358(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_9358)
names.append("rule_9358")
def rule_45592(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_45592)
names.append("rule_45592")
def rule_6322(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_6322)
names.append("rule_6322")
def rule_32468(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_32468)
names.append("rule_32468")
def rule_54398(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3]))

rules.append(rule_54398)
names.append("rule_54398")
def rule_48616(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_48616)
names.append("rule_48616")
def rule_5954(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_5954)
names.append("rule_5954")
def rule_28964(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_28964)
names.append("rule_28964")
def rule_56206(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_56206)
names.append("rule_56206")
def rule_19736(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_19736)
names.append("rule_19736")
def rule_59314(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_59314)
names.append("rule_59314")
def rule_33236(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_33236)
names.append("rule_33236")
def rule_11134(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3]))

rules.append(rule_11134)
names.append("rule_11134")
def rule_52224(ip):
	return ((ip[1]&ip[3]))

rules.append(rule_52224)
names.append("rule_52224")
def rule_26282(ip):
	return (ip[0]^(ip[1]&ip[3]))

rules.append(rule_26282)
names.append("rule_26282")
def rule_204(ip):
	return (ip[1]^(ip[1]&ip[3]))

rules.append(rule_204)
names.append("rule_204")
def rule_43622(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[3]))

rules.append(rule_43622)
names.append("rule_43622")
def rule_15600(ip):
	return (ip[2]^(ip[1]&ip[3]))

rules.append(rule_15600)
names.append("rule_15600")
def rule_38490(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[3]))

rules.append(rule_38490)
names.append("rule_38490")
def rule_61500(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[3]))

rules.append(rule_61500)
names.append("rule_61500")
def rule_23190(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[3]))

rules.append(rule_23190)
names.append("rule_23190")
def rule_13056(ip):
	return (ip[3]^(ip[1]&ip[3]))

rules.append(rule_13056)
names.append("rule_13056")
def rule_39338(ip):
	return (ip[0]^ip[3]^(ip[1]&ip[3]))

rules.append(rule_39338)
names.append("rule_39338")
def rule_65484(ip):
	return (ip[1]^ip[3]^(ip[1]&ip[3]))

rules.append(rule_65484)
names.append("rule_65484")
def rule_21862(ip):
	return (ip[0]^ip[1]^ip[3]^(ip[1]&ip[3]))

rules.append(rule_21862)
names.append("rule_21862")
def rule_50160(ip):
	return (ip[2]^ip[3]^(ip[1]&ip[3]))

rules.append(rule_50160)
names.append("rule_50160")
def rule_26970(ip):
	return (ip[0]^ip[2]^ip[3]^(ip[1]&ip[3]))

rules.append(rule_26970)
names.append("rule_26970")
def rule_3900(ip):
	return (ip[1]^ip[2]^ip[3]^(ip[1]&ip[3]))

rules.append(rule_3900)
names.append("rule_3900")
def rule_42390(ip):
	return (ip[0]^ip[1]^ip[2]^ip[3]^(ip[1]&ip[3]))

rules.append(rule_42390)
names.append("rule_42390")
def rule_17544(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[3]))

rules.append(rule_17544)
names.append("rule_17544")
def rule_60962(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[3]))

rules.append(rule_60962)
names.append("rule_60962")
def rule_34884(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[3]))

rules.append(rule_34884)
names.append("rule_34884")
def rule_8942(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[3]))

rules.append(rule_8942)
names.append("rule_8942")
def rule_46200(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[3]))

rules.append(rule_46200)
names.append("rule_46200")
def rule_7890(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[3]))

rules.append(rule_7890)
names.append("rule_7890")
def rule_30900(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[3]))

rules.append(rule_30900)
names.append("rule_30900")
def rule_53790(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[3]))

rules.append(rule_53790)
names.append("rule_53790")
def rule_48008(ip):
	return ((ip[0]&ip[1])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_48008)
names.append("rule_48008")
def rule_4386(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_4386)
names.append("rule_4386")
def rule_30532(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_30532)
names.append("rule_30532")
def rule_56814(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_56814)
names.append("rule_56814")
def rule_19320(ip):
	return ((ip[0]&ip[1])^ip[2]^ip[3]^(ip[1]&ip[3]))

rules.append(rule_19320)
names.append("rule_19320")
def rule_57810(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[1]&ip[3]))

rules.append(rule_57810)
names.append("rule_57810")
def rule_34740(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[1]&ip[3]))

rules.append(rule_34740)
names.append("rule_34740")
def rule_11550(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[1]&ip[3]))

rules.append(rule_11550)
names.append("rule_11550")
def rule_27808(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_27808)
names.append("rule_27808")
def rule_50698(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_50698)
names.append("rule_50698")
def rule_41068(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_41068)
names.append("rule_41068")
def rule_2758(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_2758)
names.append("rule_2758")
def rule_40016(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_40016)
names.append("rule_40016")
def rule_14074(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_14074)
names.append("rule_14074")
def rule_20636(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_20636)
names.append("rule_20636")
def rule_64054(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_64054)
names.append("rule_64054")
def rule_37792(ip):
	return ((ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_37792)
names.append("rule_37792")
def rule_14602(ip):
	return (ip[0]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_14602)
names.append("rule_14602")
def rule_24428(ip):
	return (ip[1]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_24428)
names.append("rule_24428")
def rule_62918(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_62918)
names.append("rule_62918")
def rule_25424(ip):
	return (ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_25424)
names.append("rule_25424")
def rule_51706(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_51706)
names.append("rule_51706")
def rule_44956(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_44956)
names.append("rule_44956")
def rule_1334(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_1334)
names.append("rule_1334")
def rule_58408(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_58408)
names.append("rule_58408")
def rule_20098(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_20098)
names.append("rule_20098")
def rule_10468(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_10468)
names.append("rule_10468")
def rule_33358(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_33358)
names.append("rule_33358")
def rule_5336(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_5336)
names.append("rule_5336")
def rule_48754(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_48754)
names.append("rule_48754")
def rule_55316(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_55316)
names.append("rule_55316")
def rule_29374(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_29374)
names.append("rule_29374")
def rule_6952(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_6952)
names.append("rule_6952")
def rule_45442(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_45442)
names.append("rule_45442")
def rule_55268(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_55268)
names.append("rule_55268")
def rule_32078(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_32078)
names.append("rule_32078")
def rule_60376(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_60376)
names.append("rule_60376")
def rule_16754(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_16754)
names.append("rule_16754")
def rule_10004(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_10004)
names.append("rule_10004")
def rule_36286(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_36286)
names.append("rule_36286")
def rule_3264(ip):
	return ((ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_3264)
names.append("rule_3264")
def rule_42602(ip):
	return (ip[0]^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_42602)
names.append("rule_42602")
def rule_49164(ip):
	return (ip[1]^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_49164)
names.append("rule_49164")
def rule_27302(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_27302)
names.append("rule_27302")
def rule_64560(ip):
	return (ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_64560)
names.append("rule_64560")
def rule_22170(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_22170)
names.append("rule_22170")
def rule_12540(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_12540)
names.append("rule_12540")
def rule_39510(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_39510)
names.append("rule_39510")
def rule_62400(ip):
	return ((ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_62400)
names.append("rule_62400")
def rule_22890(ip):
	return (ip[0]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_22890)
names.append("rule_22890")
def rule_16140(ip):
	return (ip[1]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_16140)
names.append("rule_16140")
def rule_38310(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_38310)
names.append("rule_38310")
def rule_816(ip):
	return (ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_816)
names.append("rule_816")
def rule_43418(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_43418)
names.append("rule_43418")
def rule_53244(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_53244)
names.append("rule_53244")
def rule_25942(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_25942)
names.append("rule_25942")
def rule_33864(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_33864)
names.append("rule_33864")
def rule_12002(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_12002)
names.append("rule_12002")
def rule_18564(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_18564)
names.append("rule_18564")
def rule_57902(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_57902)
names.append("rule_57902")
def rule_29880(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_29880)
names.append("rule_29880")
def rule_56850(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_56850)
names.append("rule_56850")
def rule_47220(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_47220)
names.append("rule_47220")
def rule_4830(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_4830)
names.append("rule_4830")
def rule_31560(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_31560)
names.append("rule_31560")
def rule_53730(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_53730)
names.append("rule_53730")
def rule_46980(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_46980)
names.append("rule_46980")
def rule_7470(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_7470)
names.append("rule_7470")
def rule_35768(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_35768)
names.append("rule_35768")
def rule_8466(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_8466)
names.append("rule_8466")
def rule_18292(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_18292)
names.append("rule_18292")
def rule_60894(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_60894)
names.append("rule_60894")
def rule_44128(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_44128)
names.append("rule_44128")
def rule_1738(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_1738)
names.append("rule_1738")
def rule_24748(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_24748)
names.append("rule_24748")
def rule_51718(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_51718)
names.append("rule_51718")
def rule_23696(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_23696)
names.append("rule_23696")
def rule_63034(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_63034)
names.append("rule_63034")
def rule_36956(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_36956)
names.append("rule_36956")
def rule_15094(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_15094)
names.append("rule_15094")
def rule_21344(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_21344)
names.append("rule_21344")
def rule_63946(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_63946)
names.append("rule_63946")
def rule_40876(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_40876)
names.append("rule_40876")
def rule_13574(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_13574)
names.append("rule_13574")
def rule_41872(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_41872)
names.append("rule_41872")
def rule_2362(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_2362)
names.append("rule_2362")
def rule_28508(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_28508)
names.append("rule_28508")
def rule_50678(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_50678)
names.append("rule_50678")
def rule_9448(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_9448)
names.append("rule_9448")
def rule_36418(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_36418)
names.append("rule_36418")
def rule_59428(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_59428)
names.append("rule_59428")
def rule_17038(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_17038)
names.append("rule_17038")
def rule_54296(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_54296)
names.append("rule_54296")
def rule_32434(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_32434)
names.append("rule_32434")
def rule_6356(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_6356)
names.append("rule_6356")
def rule_45694(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3]))

rules.append(rule_45694)
names.append("rule_45694")
def rule_56296(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_56296)
names.append("rule_56296")
def rule_28994(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_28994)
names.append("rule_28994")
def rule_5924(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_5924)
names.append("rule_5924")
def rule_48526(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_48526)
names.append("rule_48526")
def rule_11032(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_11032)
names.append("rule_11032")
def rule_33202(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_33202)
names.append("rule_33202")
def rule_59348(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_59348)
names.append("rule_59348")
def rule_19838(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3]))

rules.append(rule_19838)
names.append("rule_19838")
def rule_26112(ip):
	return ((ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_26112)
names.append("rule_26112")
def rule_52394(ip):
	return (ip[0]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_52394)
names.append("rule_52394")
def rule_43724(ip):
	return (ip[1]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_43724)
names.append("rule_43724")
def rule_102(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_102)
names.append("rule_102")
def rule_38640(ip):
	return (ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_38640)
names.append("rule_38640")
def rule_15450(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_15450)
names.append("rule_15450")
def rule_23100(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_23100)
names.append("rule_23100")
def rule_61590(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_61590)
names.append("rule_61590")
def rule_39168(ip):
	return (ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_39168)
names.append("rule_39168")
def rule_13226(ip):
	return (ip[0]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_13226)
names.append("rule_13226")
def rule_21964(ip):
	return (ip[1]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_21964)
names.append("rule_21964")
def rule_65382(ip):
	return (ip[0]^ip[1]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_65382)
names.append("rule_65382")
def rule_27120(ip):
	return (ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_27120)
names.append("rule_27120")
def rule_50010(ip):
	return (ip[0]^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_50010)
names.append("rule_50010")
def rule_42300(ip):
	return (ip[1]^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_42300)
names.append("rule_42300")
def rule_3990(ip):
	return (ip[0]^ip[1]^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_3990)
names.append("rule_3990")
def rule_61064(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_61064)
names.append("rule_61064")
def rule_17442(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_17442)
names.append("rule_17442")
def rule_8772(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_8772)
names.append("rule_8772")
def rule_35054(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_35054)
names.append("rule_35054")
def rule_7800(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_7800)
names.append("rule_7800")
def rule_46290(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_46290)
names.append("rule_46290")
def rule_53940(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_53940)
names.append("rule_53940")
def rule_30750(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_30750)
names.append("rule_30750")
def rule_4488(ip):
	return ((ip[0]&ip[1])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_4488)
names.append("rule_4488")
def rule_47906(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_47906)
names.append("rule_47906")
def rule_56644(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_56644)
names.append("rule_56644")
def rule_30702(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_30702)
names.append("rule_30702")
def rule_57720(ip):
	return ((ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_57720)
names.append("rule_57720")
def rule_19410(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_19410)
names.append("rule_19410")
def rule_11700(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_11700)
names.append("rule_11700")
def rule_34590(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_34590)
names.append("rule_34590")
def rule_50848(ip):
	return ((ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_50848)
names.append("rule_50848")
def rule_27658(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_27658)
names.append("rule_27658")
def rule_2668(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_2668)
names.append("rule_2668")
def rule_41158(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_41158)
names.append("rule_41158")
def rule_13904(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_13904)
names.append("rule_13904")
def rule_40186(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_40186)
names.append("rule_40186")
def rule_64156(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_64156)
names.append("rule_64156")
def rule_20534(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_20534)
names.append("rule_20534")
def rule_14752(ip):
	return ((ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_14752)
names.append("rule_14752")
def rule_37642(ip):
	return (ip[0]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_37642)
names.append("rule_37642")
def rule_62828(ip):
	return (ip[1]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_62828)
names.append("rule_62828")
def rule_24518(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_24518)
names.append("rule_24518")
def rule_51536(ip):
	return (ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_51536)
names.append("rule_51536")
def rule_25594(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_25594)
names.append("rule_25594")
def rule_1436(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_1436)
names.append("rule_1436")
def rule_44854(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_44854)
names.append("rule_44854")
def rule_20008(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_20008)
names.append("rule_20008")
def rule_58498(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_58498)
names.append("rule_58498")
def rule_33508(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_33508)
names.append("rule_33508")
def rule_10318(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_10318)
names.append("rule_10318")
def rule_48856(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_48856)
names.append("rule_48856")
def rule_5234(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_5234)
names.append("rule_5234")
def rule_29204(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_29204)
names.append("rule_29204")
def rule_55486(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_55486)
names.append("rule_55486")
def rule_45352(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_45352)
names.append("rule_45352")
def rule_7042(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_7042)
names.append("rule_7042")
def rule_32228(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_32228)
names.append("rule_32228")
def rule_55118(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_55118)
names.append("rule_55118")
def rule_16856(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_16856)
names.append("rule_16856")
def rule_60274(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_60274)
names.append("rule_60274")
def rule_36116(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_36116)
names.append("rule_36116")
def rule_10174(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_10174)
names.append("rule_10174")
def rule_42688(ip):
	return ((ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_42688)
names.append("rule_42688")
def rule_3178(ip):
	return (ip[0]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_3178)
names.append("rule_3178")
def rule_27148(ip):
	return (ip[1]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_27148)
names.append("rule_27148")
def rule_49318(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_49318)
names.append("rule_49318")
def rule_22064(ip):
	return (ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_22064)
names.append("rule_22064")
def rule_64666(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_64666)
names.append("rule_64666")
def rule_39676(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_39676)
names.append("rule_39676")
def rule_12374(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_12374)
names.append("rule_12374")
def rule_22976(ip):
	return ((ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_22976)
names.append("rule_22976")
def rule_62314(ip):
	return (ip[0]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_62314)
names.append("rule_62314")
def rule_38156(ip):
	return (ip[1]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_38156)
names.append("rule_38156")
def rule_16294(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_16294)
names.append("rule_16294")
def rule_43312(ip):
	return (ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_43312)
names.append("rule_43312")
def rule_922(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_922)
names.append("rule_922")
def rule_26108(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_26108)
names.append("rule_26108")
def rule_53078(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_53078)
names.append("rule_53078")
def rule_11848(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_11848)
names.append("rule_11848")
def rule_34018(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_34018)
names.append("rule_34018")
def rule_57988(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_57988)
names.append("rule_57988")
def rule_18478(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_18478)
names.append("rule_18478")
def rule_57016(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_57016)
names.append("rule_57016")
def rule_29714(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_29714)
names.append("rule_29714")
def rule_4724(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_4724)
names.append("rule_4724")
def rule_47326(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_47326)
names.append("rule_47326")
def rule_53576(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_53576)
names.append("rule_53576")
def rule_31714(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_31714)
names.append("rule_31714")
def rule_7556(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_7556)
names.append("rule_7556")
def rule_46894(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_46894)
names.append("rule_46894")
def rule_8632(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_8632)
names.append("rule_8632")
def rule_35602(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_35602)
names.append("rule_35602")
def rule_60788(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_60788)
names.append("rule_60788")
def rule_18398(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_18398)
names.append("rule_18398")
def rule_1632(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_1632)
names.append("rule_1632")
def rule_44234(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_44234)
names.append("rule_44234")
def rule_51884(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_51884)
names.append("rule_51884")
def rule_24582(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_24582)
names.append("rule_24582")
def rule_63120(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_63120)
names.append("rule_63120")
def rule_23610(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_23610)
names.append("rule_23610")
def rule_14940(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_14940)
names.append("rule_14940")
def rule_37110(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_37110)
names.append("rule_37110")
def rule_63840(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_63840)
names.append("rule_63840")
def rule_21450(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_21450)
names.append("rule_21450")
def rule_13740(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_13740)
names.append("rule_13740")
def rule_40710(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_40710)
names.append("rule_40710")
def rule_2448(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_2448)
names.append("rule_2448")
def rule_41786(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_41786)
names.append("rule_41786")
def rule_50524(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_50524)
names.append("rule_50524")
def rule_28662(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_28662)
names.append("rule_28662")
def rule_36584(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_36584)
names.append("rule_36584")
def rule_9282(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_9282)
names.append("rule_9282")
def rule_16932(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_16932)
names.append("rule_16932")
def rule_59534(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_59534)
names.append("rule_59534")
def rule_32280(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_32280)
names.append("rule_32280")
def rule_54450(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_54450)
names.append("rule_54450")
def rule_45780(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_45780)
names.append("rule_45780")
def rule_6270(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_6270)
names.append("rule_6270")
def rule_29160(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_29160)
names.append("rule_29160")
def rule_56130(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_56130)
names.append("rule_56130")
def rule_48420(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_48420)
names.append("rule_48420")
def rule_6030(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_6030)
names.append("rule_6030")
def rule_33048(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_33048)
names.append("rule_33048")
def rule_11186(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_11186)
names.append("rule_11186")
def rule_19924(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_19924)
names.append("rule_19924")
def rule_59262(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3]))

rules.append(rule_59262)
names.append("rule_59262")
def rule_61440(ip):
	return ((ip[2]&ip[3]))

rules.append(rule_61440)
names.append("rule_61440")
def rule_23210(ip):
	return (ip[0]^(ip[2]&ip[3]))

rules.append(rule_23210)
names.append("rule_23210")
def rule_15564(ip):
	return (ip[1]^(ip[2]&ip[3]))

rules.append(rule_15564)
names.append("rule_15564")
def rule_38502(ip):
	return (ip[0]^ip[1]^(ip[2]&ip[3]))

rules.append(rule_38502)
names.append("rule_38502")
def rule_240(ip):
	return (ip[2]^(ip[2]&ip[3]))

rules.append(rule_240)
names.append("rule_240")
def rule_43610(ip):
	return (ip[0]^ip[2]^(ip[2]&ip[3]))

rules.append(rule_43610)
names.append("rule_43610")
def rule_52284(ip):
	return (ip[1]^ip[2]^(ip[2]&ip[3]))

rules.append(rule_52284)
names.append("rule_52284")
def rule_26262(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[2]&ip[3]))

rules.append(rule_26262)
names.append("rule_26262")
def rule_3840(ip):
	return (ip[3]^(ip[2]&ip[3]))

rules.append(rule_3840)
names.append("rule_3840")
def rule_42410(ip):
	return (ip[0]^ip[3]^(ip[2]&ip[3]))

rules.append(rule_42410)
names.append("rule_42410")
def rule_50124(ip):
	return (ip[1]^ip[3]^(ip[2]&ip[3]))

rules.append(rule_50124)
names.append("rule_50124")
def rule_26982(ip):
	return (ip[0]^ip[1]^ip[3]^(ip[2]&ip[3]))

rules.append(rule_26982)
names.append("rule_26982")
def rule_65520(ip):
	return (ip[2]^ip[3]^(ip[2]&ip[3]))

rules.append(rule_65520)
names.append("rule_65520")
def rule_21850(ip):
	return (ip[0]^ip[2]^ip[3]^(ip[2]&ip[3]))

rules.append(rule_21850)
names.append("rule_21850")
def rule_13116(ip):
	return (ip[1]^ip[2]^ip[3]^(ip[2]&ip[3]))

rules.append(rule_13116)
names.append("rule_13116")
def rule_39318(ip):
	return (ip[0]^ip[1]^ip[2]^ip[3]^(ip[2]&ip[3]))

rules.append(rule_39318)
names.append("rule_39318")
def rule_30856(ip):
	return ((ip[0]&ip[1])^(ip[2]&ip[3]))

rules.append(rule_30856)
names.append("rule_30856")
def rule_53794(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[2]&ip[3]))

rules.append(rule_53794)
names.append("rule_53794")
def rule_46148(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[2]&ip[3]))

rules.append(rule_46148)
names.append("rule_46148")
def rule_7918(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[2]&ip[3]))

rules.append(rule_7918)
names.append("rule_7918")
def rule_34936(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[2]&ip[3]))

rules.append(rule_34936)
names.append("rule_34936")
def rule_8914(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[2]&ip[3]))

rules.append(rule_8914)
names.append("rule_8914")
def rule_17588(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[2]&ip[3]))

rules.append(rule_17588)
names.append("rule_17588")
def rule_60958(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[2]&ip[3]))

rules.append(rule_60958)
names.append("rule_60958")
def rule_34696(ip):
	return ((ip[0]&ip[1])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_34696)
names.append("rule_34696")
def rule_11554(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_11554)
names.append("rule_11554")
def rule_19268(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_19268)
names.append("rule_19268")
def rule_57838(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_57838)
names.append("rule_57838")
def rule_30584(ip):
	return ((ip[0]&ip[1])^ip[2]^ip[3]^(ip[2]&ip[3]))

rules.append(rule_30584)
names.append("rule_30584")
def rule_56786(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[2]&ip[3]))

rules.append(rule_56786)
names.append("rule_56786")
def rule_48052(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[2]&ip[3]))

rules.append(rule_48052)
names.append("rule_48052")
def rule_4382(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[2]&ip[3]))

rules.append(rule_4382)
names.append("rule_4382")
def rule_20640(ip):
	return ((ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_20640)
names.append("rule_20640")
def rule_64010(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_64010)
names.append("rule_64010")
def rule_40044(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_40044)
names.append("rule_40044")
def rule_14022(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_14022)
names.append("rule_14022")
def rule_41040(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_41040)
names.append("rule_41040")
def rule_2810(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_2810)
names.append("rule_2810")
def rule_27804(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_27804)
names.append("rule_27804")
def rule_50742(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_50742)
names.append("rule_50742")
def rule_44960(ip):
	return ((ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_44960)
names.append("rule_44960")
def rule_1290(ip):
	return (ip[0]^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_1290)
names.append("rule_1290")
def rule_25452(ip):
	return (ip[1]^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_25452)
names.append("rule_25452")
def rule_51654(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_51654)
names.append("rule_51654")
def rule_24400(ip):
	return (ip[2]^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_24400)
names.append("rule_24400")
def rule_62970(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_62970)
names.append("rule_62970")
def rule_37788(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_37788)
names.append("rule_37788")
def rule_14646(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_14646)
names.append("rule_14646")
def rule_55336(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_55336)
names.append("rule_55336")
def rule_29314(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_29314)
names.append("rule_29314")
def rule_5348(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_5348)
names.append("rule_5348")
def rule_48718(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_48718)
names.append("rule_48718")
def rule_10456(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_10456)
names.append("rule_10456")
def rule_33394(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_33394)
names.append("rule_33394")
def rule_58388(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_58388)
names.append("rule_58388")
def rule_20158(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_20158)
names.append("rule_20158")
def rule_10024(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_10024)
names.append("rule_10024")
def rule_36226(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_36226)
names.append("rule_36226")
def rule_60388(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_60388)
names.append("rule_60388")
def rule_16718(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_16718)
names.append("rule_16718")
def rule_55256(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_55256)
names.append("rule_55256")
def rule_32114(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_32114)
names.append("rule_32114")
def rule_6932(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_6932)
names.append("rule_6932")
def rule_45502(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_45502)
names.append("rule_45502")
def rule_12480(ip):
	return ((ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_12480)
names.append("rule_12480")
def rule_39530(ip):
	return (ip[0]^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_39530)
names.append("rule_39530")
def rule_64524(ip):
	return (ip[1]^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_64524)
names.append("rule_64524")
def rule_22182(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_22182)
names.append("rule_22182")
def rule_49200(ip):
	return (ip[2]^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_49200)
names.append("rule_49200")
def rule_27290(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_27290)
names.append("rule_27290")
def rule_3324(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_3324)
names.append("rule_3324")
def rule_42582(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_42582)
names.append("rule_42582")
def rule_53184(ip):
	return ((ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_53184)
names.append("rule_53184")
def rule_25962(ip):
	return (ip[0]^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_25962)
names.append("rule_25962")
def rule_780(ip):
	return (ip[1]^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_780)
names.append("rule_780")
def rule_43430(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_43430)
names.append("rule_43430")
def rule_16176(ip):
	return (ip[2]^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_16176)
names.append("rule_16176")
def rule_38298(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_38298)
names.append("rule_38298")
def rule_62460(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_62460)
names.append("rule_62460")
def rule_22870(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_22870)
names.append("rule_22870")
def rule_47176(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_47176)
names.append("rule_47176")
def rule_4834(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_4834)
names.append("rule_4834")
def rule_29828(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_29828)
names.append("rule_29828")
def rule_56878(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_56878)
names.append("rule_56878")
def rule_18616(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_18616)
names.append("rule_18616")
def rule_57874(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_57874)
names.append("rule_57874")
def rule_33908(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_33908)
names.append("rule_33908")
def rule_11998(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_11998)
names.append("rule_11998")
def rule_18248(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_18248)
names.append("rule_18248")
def rule_60898(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_60898)
names.append("rule_60898")
def rule_35716(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_35716)
names.append("rule_35716")
def rule_8494(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_8494)
names.append("rule_8494")
def rule_47032(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_47032)
names.append("rule_47032")
def rule_7442(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_7442)
names.append("rule_7442")
def rule_31604(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_31604)
names.append("rule_31604")
def rule_53726(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_53726)
names.append("rule_53726")
def rule_36960(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_36960)
names.append("rule_36960")
def rule_15050(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_15050)
names.append("rule_15050")
def rule_23724(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_23724)
names.append("rule_23724")
def rule_62982(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_62982)
names.append("rule_62982")
def rule_24720(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_24720)
names.append("rule_24720")
def rule_51770(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_51770)
names.append("rule_51770")
def rule_44124(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_44124)
names.append("rule_44124")
def rule_1782(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_1782)
names.append("rule_1782")
def rule_28512(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_28512)
names.append("rule_28512")
def rule_50634(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_50634)
names.append("rule_50634")
def rule_41900(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_41900)
names.append("rule_41900")
def rule_2310(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_2310)
names.append("rule_2310")
def rule_40848(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_40848)
names.append("rule_40848")
def rule_13626(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_13626)
names.append("rule_13626")
def rule_21340(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_21340)
names.append("rule_21340")
def rule_63990(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_63990)
names.append("rule_63990")
def rule_6376(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_6376)
names.append("rule_6376")
def rule_45634(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_45634)
names.append("rule_45634")
def rule_54308(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_54308)
names.append("rule_54308")
def rule_32398(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_32398)
names.append("rule_32398")
def rule_59416(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_59416)
names.append("rule_59416")
def rule_17074(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_17074)
names.append("rule_17074")
def rule_9428(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_9428)
names.append("rule_9428")
def rule_36478(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[2]&ip[3]))

rules.append(rule_36478)
names.append("rule_36478")
def rule_59368(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_59368)
names.append("rule_59368")
def rule_19778(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_19778)
names.append("rule_19778")
def rule_11044(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_11044)
names.append("rule_11044")
def rule_33166(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_33166)
names.append("rule_33166")
def rule_5912(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_5912)
names.append("rule_5912")
def rule_48562(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_48562)
names.append("rule_48562")
def rule_56276(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_56276)
names.append("rule_56276")
def rule_29054(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[2]&ip[3]))

rules.append(rule_29054)
names.append("rule_29054")
def rule_23040(ip):
	return ((ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_23040)
names.append("rule_23040")
def rule_61610(ip):
	return (ip[0]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_61610)
names.append("rule_61610")
def rule_38604(ip):
	return (ip[1]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_38604)
names.append("rule_38604")
def rule_15462(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_15462)
names.append("rule_15462")
def rule_43760(ip):
	return (ip[2]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_43760)
names.append("rule_43760")
def rule_90(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_90)
names.append("rule_90")
def rule_26172(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_26172)
names.append("rule_26172")
def rule_52374(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_52374)
names.append("rule_52374")
def rule_42240(ip):
	return (ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_42240)
names.append("rule_42240")
def rule_4010(ip):
	return (ip[0]^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_4010)
names.append("rule_4010")
def rule_27084(ip):
	return (ip[1]^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_27084)
names.append("rule_27084")
def rule_50022(ip):
	return (ip[0]^ip[1]^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_50022)
names.append("rule_50022")
def rule_22000(ip):
	return (ip[2]^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_22000)
names.append("rule_22000")
def rule_65370(ip):
	return (ip[0]^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_65370)
names.append("rule_65370")
def rule_39228(ip):
	return (ip[1]^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_39228)
names.append("rule_39228")
def rule_13206(ip):
	return (ip[0]^ip[1]^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_13206)
names.append("rule_13206")
def rule_53896(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_53896)
names.append("rule_53896")
def rule_30754(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_30754)
names.append("rule_30754")
def rule_7748(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_7748)
names.append("rule_7748")
def rule_46318(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_46318)
names.append("rule_46318")
def rule_8824(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_8824)
names.append("rule_8824")
def rule_35026(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_35026)
names.append("rule_35026")
def rule_61108(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_61108)
names.append("rule_61108")
def rule_17438(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_17438)
names.append("rule_17438")
def rule_11656(ip):
	return ((ip[0]&ip[1])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_11656)
names.append("rule_11656")
def rule_34594(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_34594)
names.append("rule_34594")
def rule_57668(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_57668)
names.append("rule_57668")
def rule_19438(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_19438)
names.append("rule_19438")
def rule_56696(ip):
	return ((ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_56696)
names.append("rule_56696")
def rule_30674(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_30674)
names.append("rule_30674")
def rule_4532(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_4532)
names.append("rule_4532")
def rule_47902(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_47902)
names.append("rule_47902")
def rule_64160(ip):
	return ((ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_64160)
names.append("rule_64160")
def rule_20490(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_20490)
names.append("rule_20490")
def rule_13932(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_13932)
names.append("rule_13932")
def rule_40134(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_40134)
names.append("rule_40134")
def rule_2640(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_2640)
names.append("rule_2640")
def rule_41210(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_41210)
names.append("rule_41210")
def rule_50844(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_50844)
names.append("rule_50844")
def rule_27702(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_27702)
names.append("rule_27702")
def rule_1440(ip):
	return ((ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_1440)
names.append("rule_1440")
def rule_44810(ip):
	return (ip[0]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_44810)
names.append("rule_44810")
def rule_51564(ip):
	return (ip[1]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_51564)
names.append("rule_51564")
def rule_25542(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_25542)
names.append("rule_25542")
def rule_62800(ip):
	return (ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_62800)
names.append("rule_62800")
def rule_24570(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_24570)
names.append("rule_24570")
def rule_14748(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_14748)
names.append("rule_14748")
def rule_37686(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_37686)
names.append("rule_37686")
def rule_29224(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_29224)
names.append("rule_29224")
def rule_55426(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_55426)
names.append("rule_55426")
def rule_48868(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_48868)
names.append("rule_48868")
def rule_5198(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_5198)
names.append("rule_5198")
def rule_33496(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_33496)
names.append("rule_33496")
def rule_10354(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_10354)
names.append("rule_10354")
def rule_19988(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_19988)
names.append("rule_19988")
def rule_58558(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_58558)
names.append("rule_58558")
def rule_36136(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_36136)
names.append("rule_36136")
def rule_10114(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_10114)
names.append("rule_10114")
def rule_16868(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_16868)
names.append("rule_16868")
def rule_60238(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_60238)
names.append("rule_60238")
def rule_32216(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_32216)
names.append("rule_32216")
def rule_55154(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_55154)
names.append("rule_55154")
def rule_45332(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_45332)
names.append("rule_45332")
def rule_7102(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_7102)
names.append("rule_7102")
def rule_39616(ip):
	return ((ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_39616)
names.append("rule_39616")
def rule_12394(ip):
	return (ip[0]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_12394)
names.append("rule_12394")
def rule_22028(ip):
	return (ip[1]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_22028)
names.append("rule_22028")
def rule_64678(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_64678)
names.append("rule_64678")
def rule_27184(ip):
	return (ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_27184)
names.append("rule_27184")
def rule_49306(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_49306)
names.append("rule_49306")
def rule_42748(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_42748)
names.append("rule_42748")
def rule_3158(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_3158)
names.append("rule_3158")
def rule_26048(ip):
	return ((ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_26048)
names.append("rule_26048")
def rule_53098(ip):
	return (ip[0]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_53098)
names.append("rule_53098")
def rule_43276(ip):
	return (ip[1]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_43276)
names.append("rule_43276")
def rule_934(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_934)
names.append("rule_934")
def rule_38192(ip):
	return (ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_38192)
names.append("rule_38192")
def rule_16282(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_16282)
names.append("rule_16282")
def rule_23036(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_23036)
names.append("rule_23036")
def rule_62294(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_62294)
names.append("rule_62294")
def rule_4680(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_4680)
names.append("rule_4680")
def rule_47330(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_47330)
names.append("rule_47330")
def rule_56964(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_56964)
names.append("rule_56964")
def rule_29742(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_29742)
names.append("rule_29742")
def rule_58040(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_58040)
names.append("rule_58040")
def rule_18450(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_18450)
names.append("rule_18450")
def rule_11892(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_11892)
names.append("rule_11892")
def rule_34014(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_34014)
names.append("rule_34014")
def rule_60744(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_60744)
names.append("rule_60744")
def rule_18402(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_18402)
names.append("rule_18402")
def rule_8580(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_8580)
names.append("rule_8580")
def rule_35630(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_35630)
names.append("rule_35630")
def rule_7608(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_7608)
names.append("rule_7608")
def rule_46866(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_46866)
names.append("rule_46866")
def rule_53620(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_53620)
names.append("rule_53620")
def rule_31710(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_31710)
names.append("rule_31710")
def rule_14944(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_14944)
names.append("rule_14944")
def rule_37066(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_37066)
names.append("rule_37066")
def rule_63148(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_63148)
names.append("rule_63148")
def rule_23558(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_23558)
names.append("rule_23558")
def rule_51856(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_51856)
names.append("rule_51856")
def rule_24634(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_24634)
names.append("rule_24634")
def rule_1628(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_1628)
names.append("rule_1628")
def rule_44278(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_44278)
names.append("rule_44278")
def rule_50528(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_50528)
names.append("rule_50528")
def rule_28618(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_28618)
names.append("rule_28618")
def rule_2476(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_2476)
names.append("rule_2476")
def rule_41734(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_41734)
names.append("rule_41734")
def rule_13712(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_13712)
names.append("rule_13712")
def rule_40762(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_40762)
names.append("rule_40762")
def rule_63836(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_63836)
names.append("rule_63836")
def rule_21494(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_21494)
names.append("rule_21494")
def rule_45800(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_45800)
names.append("rule_45800")
def rule_6210(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_6210)
names.append("rule_6210")
def rule_32292(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_32292)
names.append("rule_32292")
def rule_54414(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_54414)
names.append("rule_54414")
def rule_16920(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_16920)
names.append("rule_16920")
def rule_59570(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_59570)
names.append("rule_59570")
def rule_36564(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_36564)
names.append("rule_36564")
def rule_9342(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_9342)
names.append("rule_9342")
def rule_19944(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_19944)
names.append("rule_19944")
def rule_59202(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_59202)
names.append("rule_59202")
def rule_33060(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_33060)
names.append("rule_33060")
def rule_11150(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_11150)
names.append("rule_11150")
def rule_48408(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_48408)
names.append("rule_48408")
def rule_6066(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_6066)
names.append("rule_6066")
def rule_29140(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_29140)
names.append("rule_29140")
def rule_56190(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_56190)
names.append("rule_56190")
def rule_15360(ip):
	return ((ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_15360)
names.append("rule_15360")
def rule_38570(ip):
	return (ip[0]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_38570)
names.append("rule_38570")
def rule_61644(ip):
	return (ip[1]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_61644)
names.append("rule_61644")
def rule_23142(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_23142)
names.append("rule_23142")
def rule_52464(ip):
	return (ip[2]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_52464)
names.append("rule_52464")
def rule_26202(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_26202)
names.append("rule_26202")
def rule_60(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_60)
names.append("rule_60")
def rule_43670(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_43670)
names.append("rule_43670")
def rule_49920(ip):
	return (ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_49920)
names.append("rule_49920")
def rule_27050(ip):
	return (ip[0]^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_27050)
names.append("rule_27050")
def rule_4044(ip):
	return (ip[1]^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_4044)
names.append("rule_4044")
def rule_42342(ip):
	return (ip[0]^ip[1]^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_42342)
names.append("rule_42342")
def rule_13296(ip):
	return (ip[2]^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_13296)
names.append("rule_13296")
def rule_39258(ip):
	return (ip[0]^ip[2]^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_39258)
names.append("rule_39258")
def rule_65340(ip):
	return (ip[1]^ip[2]^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_65340)
names.append("rule_65340")
def rule_21910(ip):
	return (ip[0]^ip[1]^ip[2]^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_21910)
names.append("rule_21910")
def rule_46216(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_46216)
names.append("rule_46216")
def rule_7714(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_7714)
names.append("rule_7714")
def rule_30788(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_30788)
names.append("rule_30788")
def rule_53998(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_53998)
names.append("rule_53998")
def rule_17528(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_17528)
names.append("rule_17528")
def rule_61138(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_61138)
names.append("rule_61138")
def rule_34996(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_34996)
names.append("rule_34996")
def rule_8734(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_8734)
names.append("rule_8734")
def rule_19336(ip):
	return ((ip[0]&ip[1])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_19336)
names.append("rule_19336")
def rule_57634(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_57634)
names.append("rule_57634")
def rule_34628(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_34628)
names.append("rule_34628")
def rule_11758(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_11758)
names.append("rule_11758")
def rule_47992(ip):
	return ((ip[0]&ip[1])^ip[2]^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_47992)
names.append("rule_47992")
def rule_4562(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_4562)
names.append("rule_4562")
def rule_30644(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_30644)
names.append("rule_30644")
def rule_56606(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_56606)
names.append("rule_56606")
def rule_40096(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_40096)
names.append("rule_40096")
def rule_13834(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_13834)
names.append("rule_13834")
def rule_20588(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_20588)
names.append("rule_20588")
def rule_64198(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_64198)
names.append("rule_64198")
def rule_27728(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_27728)
names.append("rule_27728")
def rule_50938(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_50938)
names.append("rule_50938")
def rule_41116(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_41116)
names.append("rule_41116")
def rule_2614(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_2614)
names.append("rule_2614")
def rule_25504(ip):
	return ((ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_25504)
names.append("rule_25504")
def rule_51466(ip):
	return (ip[0]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_51466)
names.append("rule_51466")
def rule_44908(ip):
	return (ip[1]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_44908)
names.append("rule_44908")
def rule_1478(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_1478)
names.append("rule_1478")
def rule_37712(ip):
	return (ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_37712)
names.append("rule_37712")
def rule_14842(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_14842)
names.append("rule_14842")
def rule_24476(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_24476)
names.append("rule_24476")
def rule_62774(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_62774)
names.append("rule_62774")
def rule_5160(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_5160)
names.append("rule_5160")
def rule_48770(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_48770)
names.append("rule_48770")
def rule_55524(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_55524)
names.append("rule_55524")
def rule_29262(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_29262)
names.append("rule_29262")
def rule_58584(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_58584)
names.append("rule_58584")
def rule_20082(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_20082)
names.append("rule_20082")
def rule_10260(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_10260)
names.append("rule_10260")
def rule_33470(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_33470)
names.append("rule_33470")
def rule_60200(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_60200)
names.append("rule_60200")
def rule_16770(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_16770)
names.append("rule_16770")
def rule_10212(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_10212)
names.append("rule_10212")
def rule_36174(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_36174)
names.append("rule_36174")
def rule_7128(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_7128)
names.append("rule_7128")
def rule_45426(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_45426)
names.append("rule_45426")
def rule_55060(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_55060)
names.append("rule_55060")
def rule_32190(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_32190)
names.append("rule_32190")
def rule_64704(ip):
	return ((ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_64704)
names.append("rule_64704")
def rule_22122(ip):
	return (ip[0]^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_22122)
names.append("rule_22122")
def rule_12300(ip):
	return (ip[1]^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_12300)
names.append("rule_12300")
def rule_39590(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_39590)
names.append("rule_39590")
def rule_3120(ip):
	return (ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_3120)
names.append("rule_3120")
def rule_42650(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_42650)
names.append("rule_42650")
def rule_49404(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_49404)
names.append("rule_49404")
def rule_27222(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_27222)
names.append("rule_27222")
def rule_960(ip):
	return ((ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_960)
names.append("rule_960")
def rule_43370(ip):
	return (ip[0]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_43370)
names.append("rule_43370")
def rule_53004(ip):
	return (ip[1]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_53004)
names.append("rule_53004")
def rule_26022(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_26022)
names.append("rule_26022")
def rule_62256(ip):
	return (ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_62256)
names.append("rule_62256")
def rule_22938(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_22938)
names.append("rule_22938")
def rule_16380(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_16380)
names.append("rule_16380")
def rule_38230(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_38230)
names.append("rule_38230")
def rule_29768(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_29768)
names.append("rule_29768")
def rule_57058(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_57058)
names.append("rule_57058")
def rule_47236(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_47236)
names.append("rule_47236")
def rule_4654(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_4654)
names.append("rule_4654")
def rule_33976(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_33976)
names.append("rule_33976")
def rule_11794(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_11794)
names.append("rule_11794")
def rule_18548(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_18548)
names.append("rule_18548")
def rule_58078(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_58078)
names.append("rule_58078")
def rule_35656(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_35656)
names.append("rule_35656")
def rule_8674(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_8674)
names.append("rule_8674")
def rule_18308(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_18308)
names.append("rule_18308")
def rule_60718(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_60718)
names.append("rule_60718")
def rule_31672(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_31672)
names.append("rule_31672")
def rule_53522(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_53522)
names.append("rule_53522")
def rule_46964(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_46964)
names.append("rule_46964")
def rule_7646(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_7646)
names.append("rule_7646")
def rule_23648(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_23648)
names.append("rule_23648")
def rule_63178(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_63178)
names.append("rule_63178")
def rule_37036(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_37036)
names.append("rule_37036")
def rule_14854(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_14854)
names.append("rule_14854")
def rule_44176(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_44176)
names.append("rule_44176")
def rule_1594(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_1594)
names.append("rule_1594")
def rule_24668(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_24668)
names.append("rule_24668")
def rule_51958(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_51958)
names.append("rule_51958")
def rule_41824(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_41824)
names.append("rule_41824")
def rule_2506(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_2506)
names.append("rule_2506")
def rule_28588(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_28588)
names.append("rule_28588")
def rule_50438(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_50438)
names.append("rule_50438")
def rule_21392(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_21392)
names.append("rule_21392")
def rule_63802(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_63802)
names.append("rule_63802")
def rule_40796(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_40796)
names.append("rule_40796")
def rule_13814(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_13814)
names.append("rule_13814")
def rule_54504(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_54504)
names.append("rule_54504")
def rule_32322(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_32322)
names.append("rule_32322")
def rule_6180(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_6180)
names.append("rule_6180")
def rule_45710(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_45710)
names.append("rule_45710")
def rule_9240(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_9240)
names.append("rule_9240")
def rule_36530(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_36530)
names.append("rule_36530")
def rule_59604(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_59604)
names.append("rule_59604")
def rule_17022(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_17022)
names.append("rule_17022")
def rule_11240(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_11240)
names.append("rule_11240")
def rule_33090(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_33090)
names.append("rule_33090")
def rule_59172(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_59172)
names.append("rule_59172")
def rule_19854(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_19854)
names.append("rule_19854")
def rule_56088(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_56088)
names.append("rule_56088")
def rule_29106(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_29106)
names.append("rule_29106")
def rule_6100(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_6100)
names.append("rule_6100")
def rule_48510(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_48510)
names.append("rule_48510")
def rule_38400(ip):
	return ((ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_38400)
names.append("rule_38400")
def rule_15530(ip):
	return (ip[0]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_15530)
names.append("rule_15530")
def rule_23244(ip):
	return (ip[1]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_23244)
names.append("rule_23244")
def rule_61542(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_61542)
names.append("rule_61542")
def rule_26352(ip):
	return (ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_26352)
names.append("rule_26352")
def rule_52314(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_52314)
names.append("rule_52314")
def rule_43580(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_43580)
names.append("rule_43580")
def rule_150(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_150)
names.append("rule_150")
def rule_26880(ip):
	return (ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_26880)
names.append("rule_26880")
def rule_50090(ip):
	return (ip[0]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_50090)
names.append("rule_50090")
def rule_42444(ip):
	return (ip[1]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_42444)
names.append("rule_42444")
def rule_3942(ip):
	return (ip[0]^ip[1]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_3942)
names.append("rule_3942")
def rule_39408(ip):
	return (ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_39408)
names.append("rule_39408")
def rule_13146(ip):
	return (ip[0]^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_13146)
names.append("rule_13146")
def rule_21820(ip):
	return (ip[1]^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_21820)
names.append("rule_21820")
def rule_65430(ip):
	return (ip[0]^ip[1]^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_65430)
names.append("rule_65430")
def rule_7816(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_7816)
names.append("rule_7816")
def rule_46114(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_46114)
names.append("rule_46114")
def rule_53828(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_53828)
names.append("rule_53828")
def rule_30958(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_30958)
names.append("rule_30958")
def rule_61048(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_61048)
names.append("rule_61048")
def rule_17618(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_17618)
names.append("rule_17618")
def rule_8884(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_8884)
names.append("rule_8884")
def rule_34846(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_34846)
names.append("rule_34846")
def rule_57736(ip):
	return ((ip[0]&ip[1])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_57736)
names.append("rule_57736")
def rule_19234(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_19234)
names.append("rule_19234")
def rule_11588(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_11588)
names.append("rule_11588")
def rule_34798(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_34798)
names.append("rule_34798")
def rule_4472(ip):
	return ((ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_4472)
names.append("rule_4472")
def rule_48082(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_48082)
names.append("rule_48082")
def rule_56756(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_56756)
names.append("rule_56756")
def rule_30494(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_30494)
names.append("rule_30494")
def rule_13984(ip):
	return ((ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_13984)
names.append("rule_13984")
def rule_39946(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_39946)
names.append("rule_39946")
def rule_64108(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_64108)
names.append("rule_64108")
def rule_20678(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_20678)
names.append("rule_20678")
def rule_50768(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_50768)
names.append("rule_50768")
def rule_27898(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_27898)
names.append("rule_27898")
def rule_2716(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_2716)
names.append("rule_2716")
def rule_41014(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_41014)
names.append("rule_41014")
def rule_51616(ip):
	return ((ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_51616)
names.append("rule_51616")
def rule_25354(ip):
	return (ip[0]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_25354)
names.append("rule_25354")
def rule_1388(ip):
	return (ip[1]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_1388)
names.append("rule_1388")
def rule_44998(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_44998)
names.append("rule_44998")
def rule_14672(ip):
	return (ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_14672)
names.append("rule_14672")
def rule_37882(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_37882)
names.append("rule_37882")
def rule_62876(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_62876)
names.append("rule_62876")
def rule_24374(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_24374)
names.append("rule_24374")
def rule_48680(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_48680)
names.append("rule_48680")
def rule_5250(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_5250)
names.append("rule_5250")
def rule_29412(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_29412)
names.append("rule_29412")
def rule_55374(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_55374)
names.append("rule_55374")
def rule_20184(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_20184)
names.append("rule_20184")
def rule_58482(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_58482)
names.append("rule_58482")
def rule_33300(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_33300)
names.append("rule_33300")
def rule_10430(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_10430)
names.append("rule_10430")
def rule_16680(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_16680)
names.append("rule_16680")
def rule_60290(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_60290)
names.append("rule_60290")
def rule_36324(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_36324)
names.append("rule_36324")
def rule_10062(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_10062)
names.append("rule_10062")
def rule_45528(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_45528)
names.append("rule_45528")
def rule_7026(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_7026)
names.append("rule_7026")
def rule_32020(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_32020)
names.append("rule_32020")
def rule_55230(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_55230)
names.append("rule_55230")
def rule_22208(ip):
	return ((ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_22208)
names.append("rule_22208")
def rule_64618(ip):
	return (ip[0]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_64618)
names.append("rule_64618")
def rule_39436(ip):
	return (ip[1]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_39436)
names.append("rule_39436")
def rule_12454(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_12454)
names.append("rule_12454")
def rule_42544(ip):
	return (ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_42544)
names.append("rule_42544")
def rule_3226(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_3226)
names.append("rule_3226")
def rule_27388(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_27388)
names.append("rule_27388")
def rule_49238(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_49238)
names.append("rule_49238")
def rule_43456(ip):
	return ((ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_43456)
names.append("rule_43456")
def rule_874(ip):
	return (ip[0]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_874)
names.append("rule_874")
def rule_25868(ip):
	return (ip[1]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_25868)
names.append("rule_25868")
def rule_53158(ip):
	return (ip[0]^ip[1]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_53158)
names.append("rule_53158")
def rule_22832(ip):
	return (ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_22832)
names.append("rule_22832")
def rule_62362(ip):
	return (ip[0]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_62362)
names.append("rule_62362")
def rule_38396(ip):
	return (ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_38396)
names.append("rule_38396")
def rule_16214(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_16214)
names.append("rule_16214")
def rule_56904(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_56904)
names.append("rule_56904")
def rule_29922(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_29922)
names.append("rule_29922")
def rule_4740(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_4740)
names.append("rule_4740")
def rule_47150(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_47150)
names.append("rule_47150")
def rule_11960(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_11960)
names.append("rule_11960")
def rule_33810(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_33810)
names.append("rule_33810")
def rule_57972(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_57972)
names.append("rule_57972")
def rule_18654(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_18654)
names.append("rule_18654")
def rule_8520(ip):
	return ((ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_8520)
names.append("rule_8520")
def rule_35810(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_35810)
names.append("rule_35810")
def rule_60804(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_60804)
names.append("rule_60804")
def rule_18222(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_18222)
names.append("rule_18222")
def rule_53688(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_53688)
names.append("rule_53688")
def rule_31506(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_31506)
names.append("rule_31506")
def rule_7540(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_7540)
names.append("rule_7540")
def rule_47070(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_47070)
names.append("rule_47070")
def rule_63072(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_63072)
names.append("rule_63072")
def rule_23754(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_23754)
names.append("rule_23754")
def rule_15020(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_15020)
names.append("rule_15020")
def rule_36870(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_36870)
names.append("rule_36870")
def rule_1680(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_1680)
names.append("rule_1680")
def rule_44090(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_44090)
names.append("rule_44090")
def rule_51804(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_51804)
names.append("rule_51804")
def rule_24822(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_24822)
names.append("rule_24822")
def rule_2400(ip):
	return ((ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_2400)
names.append("rule_2400")
def rule_41930(ip):
	return (ip[0]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_41930)
names.append("rule_41930")
def rule_50604(ip):
	return (ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_50604)
names.append("rule_50604")
def rule_28422(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_28422)
names.append("rule_28422")
def rule_63888(ip):
	return (ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_63888)
names.append("rule_63888")
def rule_21306(ip):
	return (ip[0]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_21306)
names.append("rule_21306")
def rule_13660(ip):
	return (ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_13660)
names.append("rule_13660")
def rule_40950(ip):
	return (ip[0]^ip[1]^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_40950)
names.append("rule_40950")
def rule_32488(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_32488)
names.append("rule_32488")
def rule_54338(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_54338)
names.append("rule_54338")
def rule_45604(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_45604)
names.append("rule_45604")
def rule_6286(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_6286)
names.append("rule_6286")
def rule_36376(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_36376)
names.append("rule_36376")
def rule_9394(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_9394)
names.append("rule_9394")
def rule_17108(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_17108)
names.append("rule_17108")
def rule_59518(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_59518)
names.append("rule_59518")
def rule_33256(ip):
	return ((ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_33256)
names.append("rule_33256")
def rule_11074(ip):
	return (ip[0]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_11074)
names.append("rule_11074")
def rule_19748(ip):
	return (ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_19748)
names.append("rule_19748")
def rule_59278(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_59278)
names.append("rule_59278")
def rule_28952(ip):
	return ((ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_28952)
names.append("rule_28952")
def rule_56242(ip):
	return (ip[0]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_56242)
names.append("rule_56242")
def rule_48596(ip):
	return (ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_48596)
names.append("rule_48596")
def rule_6014(ip):
	return (ip[0]^ip[1]^(ip[0]&ip[1])^ip[2]^(ip[0]&ip[2])^(ip[1]&ip[2])^ip[3]^(ip[0]&ip[3])^(ip[1]&ip[3])^(ip[2]&ip[3]))

rules.append(rule_6014)
names.append("rule_6014")

def return_rules():
    return rules,names
