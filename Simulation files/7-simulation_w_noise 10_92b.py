import subprocess
import csv
import numpy as np
import sys
import math
import os
import time
import random
#This function gets X as an input and returns y as an output, basically performing the function of experiment


def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
def Oracle(x):
  no_error=a1*gaussian(x[0],mu1,sig1)+a2*gaussian(x[1],mu2,sig2)+a3*gaussian(x[2],mu3,sig3)
  with_error=no_error*(1+(random.random()-0.5)/5)
  return with_error

result=[]
[a1, a2, a3, mu1, mu2, mu3, sig1, sig2, sig3]= [13.711405957015819, 13.036115828943784, 6.742839345189473, 18.057531204319893, 1.0200066313062184, 14.64093591042004, 9.153419205289197, 20.6676324903278, 18.33180805140832]
print max
max=0

print range(1,25)
for i in range(1,25):
	for j in range(1,25):
		for k in range(1,25):
			current_val=Oracle([i,j,k])
			if current_val>max:
				max=current_val
min=-max
print max
for k in range(100):
	print min
	NotFoundMin=True
	counter =0
	first95=10000
	first99=10000
	while NotFoundMin:
		counter=counter+92
		for q in range(92):
			subprocess.call(["python", "spearmint-lite.py", "braninpy", "--method=GPEIOptChooser", "--method-args=noiseless=0" ])

		with open('braninpy/Results.dat','r') as f:
		    reader = csv.reader(f, delimiter=" ")
		    temp = list(reader)
		f.close
		# print temp
		for i in range(0,len(temp)):
			if temp[i][0]=="P":
				temp[i][1]=0
				X=[int(temp[i][2]),int(temp[i][3]), int(temp[i][4])]
				temp[i][0]=-Oracle(X)
				if temp[i][0]<=0.98*min:
					NotFoundMin=False
				if temp[i][0]<=min*0.99:
					if counter<first99:
						first99=counter
				if temp[i][0]<=min*0.95:
					if counter<first95:
						first95=counter
		with open("braninpy/Results.dat", "wb") as f:
		    writer = csv.writer(f, delimiter=" ")
		    # temp = [temp[i].replace(',', ' ').strip('\"') for i in range(len(temp))]
		    writer.writerows(temp)
		f.close
		if counter>400:
			break
	os.remove("braninpy/Results.dat")
	try: 
		os.remove("braninpy/chooser.GPEIOptChooser.pkl")
	except:
		pass
	try: 
		os.remove("braninpy/chooser.GPEIOptChooser_hyperparameters.txt")
	except:
		pass
	result.append([counter, -min, first95, first99])

print result

