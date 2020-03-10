from scipy.spatial import distance
import numpy as np
import re
f = open(r'C:\Users\Арсений\Desktop\кошки.txt', 'r')
dict={}
countsent=0
countslov=0
predl=[]
for line in f:
    lowline=line.lower()
    line=re.split('[^a-z]', lowline)
    countsent+=1
    predl.append(line)
    for slovo in line:
        if slovo!="":
            if slovo not in dict:
                countslov += 1
                dict[slovo] = countslov

matrix=np.ones((countsent,countslov))

for i in range(len(predl)):
    for key in dict:
        count=0
        for j in range(len(predl[i])):
            #print(range(len(predl[i])))
            if predl[i][j]==key:
                count+=1
        matrix[i,(dict[key]-1)]=count
minimums=[]
for nomer in range(countsent):
    data=distance.cosine(matrix[0, :], matrix[nomer, :])
    minimums.append(data)
min1=1
min2=minimums[0]
indmin1=0
minimums=minimums[1:]
for mm in range(len(minimums)):
    if minimums[mm]<=min1:
        min2=min1
        indmin2 =indmin1
        min1=minimums[mm]
        indmin1=mm
    elif minimums[mm]>min1 and minimums[mm]<=min2:
        min2=minimums[mm]
        indmin2 = mm
min1=str(indmin1+1)
min2=str(indmin2+1)
print(minimums)
f = open(r'C:\Users\Арсений\Desktop\кошки.txt', 'w')
f.write(min1+' '+min2)
f.close()
