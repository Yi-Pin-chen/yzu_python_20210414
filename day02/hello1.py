# -*-coding:UTF-8 -*-
import keyword
print(keyword.kwlist)

print("我是中文")

"""註解三個雙引號"""
score = 80
if score>=60:
    print(score,"Pass")
else:
    print(score,"No Pass")
# 整數 8 ,10,16 進位
#0o表8進位;0x表16進位

a=12   #10 進位
b=0o12  #8進位
c=0x12  #16進位
print(a,b,c)

#浮點數
a=3.14
b=3.14e2 #科學記號:3.14e2->3.14*10^2
c=1000e-2 #科學記號:1000e-2 ->1000 * 1/(10**2)
print(a,b,c)

#賦值(=)
name,h,w,age,isPass="John",170.5,60,18,True
print(name,h,w,age,isPass)

#資料型態(Type)
print(name,type(name))
print(h,type(h))
print(w,type(w))
print(isPass,type(isPass))


#刪除變數
money=1000
print(money)
del money
print(money)

