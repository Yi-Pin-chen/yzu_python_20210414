import math
"""
170,60
180,70
160,60
"""
import math
def GetBMI(h,w):
 bmi = w/math.pow(h/100,2)
 result ="Too Thin"
    #result = "Too Fat" if bmi>23 else "Too Thin" if bmi <=18 else "正常"
        if 18 < bmi < 23:
            result="Regular"
        else:
            result="Too Fat"

print("h=%.1f w=%.1f bmi=%.2f result=%s" % (h, w, bmi,result))
GetBMI(170,50)
GetBMI(180,70)
GetBMI(160,60)