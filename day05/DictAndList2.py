e1={"name":"John","salary":50000,'program':['Html','JS']}
e2={"name":"Mary","salary":60000,'program':['Html','python']}
e3={"name":"Bob","salary":70000,'program':['Java','python','C#']}
# 請求出會python 的員工人名, 並將其放入 names =[] 中
emplyee = [e1,e2,e3]
names=[]
for i in emplyee:
    for j in emplyee['program']:
        if emplyee['program'] == 'python':
            print(emplyee["name"],emplyee['program'])
            names.append(emplyee["name"])



