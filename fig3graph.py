# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 13:26:25 2019

@author: scott
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import csv

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
x=[]
y=[]
z=[]
with open('R3new.csv', encoding='UTF-8') as csvfile:
    dataread=csv.reader(csvfile)
    for row in dataread:
        print(row[0])
        print(row[1])
        print(row[2])
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))

#x = np.random.standard_normal(100)
#y = np.random.standard_normal(100)
#z = np.random.standard_normal(100)
d = np.random.standard_normal(48)
a = '#FF0000'
b = '#00FF00'
c = '#FFA500'

ax.scatter(x[:46], y[:46], z[:46])#, c=d, cmap=plt.get_cmap('binary'),depthshade=False)
#ax.scatter(x[48:96],y[48:96],z[48:96],c=a,depthshade=False,marker='.')
#ax.scatter(x[96:144],y[96:144],z[96:144],c=b,depthshade=False,marker='.')
#ax.scatter(x[144:192],y[144:192],z[144:192],c=c,depthshade=False,marker='.')
ax.set_xlabel('Promoter 1',fontname='Arial')
ax.set_ylabel('Promoter 2',fontname='Arial')
ax.set_zlabel('Promoter 3',fontname='Arial')
ax.set_xlim(0,25)
ax.set_ylim(0,25)
ax.set_zlim(0,25)
ax.set_title('Round 3',fontname='Arial')
plt.savefig('R3new.svg')
plt.show()
