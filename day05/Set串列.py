import random as r
lotto = set() #不重複串列
lotto.add(10)
lotto.add(20)
lotto.add(10)
print(len(lotto),lotto)

#今彩539電腦選號1~39 取出任意5個不重複的號碼
lotto=set()
while len(lotto)<5:
  n= r.randint(1,39)
  lotto.add(n)
  print("n=",n)
print(lotto)
