n1=0
n2=1
print(n1,end=",")
print(n2,end=",")
for i in range(0,20):
    tmp=n1+n2
    print(tmp,end=",")
    n1=n2
    n2=tmp
