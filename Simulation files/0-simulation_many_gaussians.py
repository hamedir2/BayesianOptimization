import subprocess
import csv
import numpy as np
import sys
import math
import os
import time
import random
#returns the result sampled from a gaussian distribution at point x with the average mu and standard deviation of sig
def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
#This function gets X as an input and returns y as an output, basically performing the function of experiment
def Oracle(x):
  return a1*gaussian(x[0],mu1,sig1)+a2*gaussian(x[1],mu2,sig2)+a3*gaussian(x[2],mu3,sig3)
#this loop generates 100 random gaussian mixture models and tries to find their maximum.
result=[]
for k in range(101):
#generating a GMM
	[a1, a2, a3, mu1, mu2, mu3, sig1, sig2, sig3]= [random.random()*24, random.random()*24, random.random()*24, random.random()*24, random.random()*24, random.random()*24, random.random()*24, random.random()*24, random.random()*24]

	max=0
	#brute force search to find the maximum. The absolute maximum may not be found in some cases becasue the inputs are discrete.
	for i in range(0,24):
		for j in range(0,24):
			for l in range(0,24):
				current_val=Oracle([i,j,l])
				if current_val>max:
					max=current_val
	#Spearmint by default finds the minimum and not maximum. We will change the sign of the maximum to and also the oracle
	min=-max
	
	NotFoundMin=True
	counter =0
	#starts with very large numbers and change it when the first time 95% or 99% of the maximum is found
	first95=10000
	first99=10000
	while NotFoundMin:
		counter=counter+1
		#this function calls the spearmint code.
		subprocess.call(["python", "spearmint-lite.py", "braninpy", "--method=GPEIOptChooser", "--method-args=noiseless=1" ])
		#this function reads the results from the spearmint output. i.e. the next points to evaluate
		with open('braninpy/Results.dat','r') as f:
		    reader = csv.reader(f, delimiter=" ")
		    temp = list(reader)
		f.close
		# This part finds the pending evaluations that start with letter "P"
		for i in range(0,len(temp)):
			if temp[i][0]=="P":
				temp[i][1]=0
				X=[int(temp[i][2]),int(temp[i][3]), int(temp[i][4])]
				#run the oracle to "perform an experiment". Note the negative sign
				temp[i][0]=-Oracle(X)
				#updates the housekeeping files if the max, 99% of max or 95% of max are found.
				if temp[i][0]<=0.98*min:
					NotFoundMin=False
				if temp[i][0]<=min*0.99:
					if counter<first99:
						first99=counter
				if temp[i][0]<=min*0.95:
					if counter<first95:
						first95=counter
		#writes the result in the results file
		with open("braninpy/Results.dat", "wb") as f:
		    writer = csv.writer(f, delimiter=" ")
		    temp = [temp[i].replace(',', ' ').strip('\"') for i in range(len(temp))]
		    writer.writerows(temp)
		f.close
		#stops the loop if the final result is not found after 400 trials.
		if counter>400:
			break
	#This is a cleanup code, deleting the Results and the Gaussian Process files before running the next optimization on the next GMM
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

#The results from the last random GMM was used for all the future optimization simulations
print [a1, a2, a3, mu1, mu2, mu3, sig1, sig2, sig3]
