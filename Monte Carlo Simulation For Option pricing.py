#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math
import numpy as np
import pandas as pd
import datetime
import scipy.stats as stats
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr


# In[9]:


# initial derivative parameters
S = 101.15          #stock price
K = 98.01           #strike price
vol = 0.0991        #volatility (%)(Implied volitility)
r = 0.01            #risk-free rate (%)
N = 10              #number of time steps
M = 10000            #number of simulations

market_value = 3.86 #market price of option
#time in years

T = ((datetime.date(2022,3,17)-datetime.date(2022,1,17)).days+1)/365    
#here we have put the specific date but we can have today date
#also and calculate accordigly

print(T)



# In[16]:


# now we have to go to the basic underlying progression equation
# so for that we have to focus on underlying dynamics
# the randomness comes from the dynamics of underlying on the given 
# implied volatility and rate of return and given time and
# all given parameters.

# normal constant
dt = T/N
nudt = (r-0.5*vol**2)*dt
volsdt = vol*np.sqrt(dt)
lnS = np.log(S)

# come initiation 

sum_CT = 0
sum_CT2 = 0


# Monte Carlo Method

for i in range(M):
    lnSt = lnS
    for i in  range(N):
        lnSt = lnSt + nudt + volsdt*np.random.normal()
        
    ST= np.exp(lnSt)
    CT = max(0,ST-K)
    sum_CT  = sum_CT + CT
    sum_CT2 = sum_CT2 + (CT*CT)
    
# compute Expectation and se

C0  = np.exp(-r*T)*sum_CT/M
sigma = np.sqrt((sum_CT2 - sum_CT*sum_CT/M)*np.exp(-2*r*T)/ (M-1))
SE = sigma/np.sqrt(M)


print("Call Value is ${0} with SE +/- {1}". format(np.round(C0,2),np.round(SE,2)))

print(" difference ${0}",(market_value-C0))


# In[ ]:





# In[ ]:




