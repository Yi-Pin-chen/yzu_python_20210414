# -*-coding:UTF-8 -*-
import math

#隨堂練習
x1,y1 = 10,20
x2,y2 = 15,45
#求兩點間的距離d=?

d=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
print("d距離為%.1f" %d)
d1=math.sqrt((x1-x2)**2+(y1-y2)**2)
print("d1距離為%.1f" %d1)

#老師的答案
x=math.pow(x1-x2,2)
y=math.pow(y1-y2,2)
d2=math.sqrt(x+y)
print("d2距離為%.1f" %d2)