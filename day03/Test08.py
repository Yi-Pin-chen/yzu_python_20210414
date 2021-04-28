# 雞兔同籠

def getCheckenAndRabbit(sum,feet):
    """
    :param sum: 
    :param feet: 
    :return: 
    """
    if feet/4 <= sum <= feet/2:
        Rabbit=(feet-(sum*2))/2
        Chicken = sum-Rabbit
        return Rabbit,Chicken
    else:
        print("無法計算")
        return 0,0
print(getCheckenAndRabbit(83,240))

c,r = getCheckenAndRabbit(83,240)
print(c,r)