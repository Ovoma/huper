file=open('E:\Downloads\dataset_3363_3 (2).txt',"r")
maxslovo=""
count=0
spisok=file.read().lower().split()
dlina=len(spisok)
spisok.sort()
print(spisok)
bukv={}
for i in spisok:
    if i in bukv:
        bukv[i]+=1
    else:
        bukv[i]=1
for j in sorted(bukv.items(),key=lambda para:(para[1])):
    print(j)
