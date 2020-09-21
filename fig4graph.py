import matplotlib.pyplot as plt
import numpy as np
import csv

R1=[]
R2=[]
R3=[]
R46=[]
R136=[]

with open('fig4data.csv', encoding='UTF-8') as csvfile:
    dataread=csv.reader(csvfile)
    for row in dataread:
        R1.append(row[0])
        R2.append(row[1])
        R3.append(row[2])
        R46.append(row[3])
        R136.append(row[4])

R1=R1[:46]
R2=R2[:45]
R3=R3[:45]
R46=R46[:46]

for i in range(len(R1)):
    R1[i]=float(R1[i])

for i in range(len(R2)):
    R2[i]=float(R2[i])
    
for i in range(len(R3)):
    R3[i]=float(R3[i])
    
for i in range(len(R46)):
    R46[i]=float(R46[i])
    
for i in range(len(R136)):
    R136[i]=float(R136[i])

data=[]
data.append(R1)
data.append(R2)
data.append(R3)
data.append(R46)
data.append(R136)
       
fig, ax = plt.subplots()
box = plt.boxplot(data,0,flierprops=dict(marker='D',markerfacecolor='black',markersize=5,linestyle='none'),medianprops=dict(color='black'),patch_artist=True)
colors = ['mediumblue', 'lightseagreen', 'limegreen','darkorange','orangered']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
ax.set_xticklabels(['Round 1','Round 2','Round 3','Random 46','Random 136'],fontname='Arial')
ax.set_ylabel('mg/gCDW',fontname='Arial')
plt.savefig('fig4.svg')
plt.show()
