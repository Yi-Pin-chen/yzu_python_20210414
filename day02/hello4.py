# -*-coding:UTF-8 -*-
account =10000000 #帳戶資金
stock = "台積電" #標的
price= 590.5 #成交價
amount = 5432 #股數
tax_ratio=1.425/1000
fee_ratio=3/1000
#買入成本
cost= price*amount*(1+tax_ratio)
#帳戶剩餘資金
account=account-cost
print(cost,account) #預設sep=" ";預設end="/n"
print("成本",cost,sep="=",end=";")
#%f(浮點數);%d(整數);%s(字串)
print("成本:%.1f"%cost)
#買進 台積電 5432股 花費成本 $3212166.8 帳戶餘額 $6787833.1
print("買進 %s %d 股 花費成本 $ %.1f 帳戶餘額 $ %.1f"%(stock,amount,cost,account))
print("買進 %s %d 股 花費成本 $ %.1f 帳戶餘額 $ %s"%(stock,amount,cost,format(account,",")))
print("帳戶餘額 $ %s" %(format(int(account*10)/10,",")))

txt="a={},b={}".format(1234,6789)
print(txt)
txt="a={:,},b={}".format(1234,6789)
print(txt)
#不足補0
rate1 =3.321
print("%07.3f"% rate1)