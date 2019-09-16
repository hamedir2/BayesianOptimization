import numpy as np
import sys
import math
import time
import numpy as np
import random

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
def Oracle(x):
  return 2*gaussian(x[0],12,10)+3*gaussian(x[1],19,10)+4*gaussian(x[2],17,7)
def branin(x):
  # time.sleep(1000000)
  return -Oracle(x)+4*random.random()-2
# Write a function like this called 'main'
def main(job_id, params):
  print 'Anything printed here will end up in the output directory for job #:', str(job_id)
  print params
  return branin(params['X'])
