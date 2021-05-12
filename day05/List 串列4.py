# List 串列與Tuple 元祖
a = [1,2,3,4,5] #可修改
b=(1,2,3,4,5) #不可修改
print(type(a),a)
print(type(b),b)

#轉換

a = tuple(a) #List 轉 Tuple
print(type(a),a)

b= list(b) #Tuple轉 List
print(type(b),b)