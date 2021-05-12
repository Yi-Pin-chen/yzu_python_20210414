#dict = key + value
salary ={'John':50000,'Mary':68000}
#salary ={'John'---Key :50000---value,'Mary':68000}
print(salary)
print("John 's salary is ", salary["John"])

for key in salary:
    print("%s 的薪資 %d "%(key,salary[key]))
# 新增元素
salary.setdefault("Bob",70000)
print(salary)

#求薪資總和
TotalSalary = 0
for key in salary:
    TotalSalary = TotalSalary + salary[key]
print("薪資總和:", TotalSalary )
