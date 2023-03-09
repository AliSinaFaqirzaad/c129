import pandas as pd
import csv

data1=[]
data2=[]

with open("bright_stars.csv",'r',encoding='utf8') as f:
    stars= csv.reader(f)
    for i in stars:
        data1.append(i)

with open("sky.csv",'r',encoding='utf8') as f:
    stars= csv.reader(f)
    for i in stars:
     data2.append(i)

header1=data1[0]
header2=data2[0]
header=header1+header2

starData1=data1[1:]
starData2=data2[1:]
starData = []

for i in starData1:
   starData.append(i)

for i in starData2:
   starData.append(i)

with open("total_stars.csv",'w',encoding='uft8') as f:
    stars= csv.writer(f)
    stars.writerow(header)
    stars.writerows(starData)

