a=int(input())
b=[]
for i in range(a):
        b=b+[i]*i
print(*b[0:a])

a=int(input())
b=[]
for i in range(a):
        b=b+[i]*i
b=b[0:a]
for j in b:
    print(j,end = " ")
    
    
    a=int(input())
b=[]
for i in range(a):
        b=b+[i]*i
b=b[0:a]
for j in b:
    print(int(j),end = " ")
