#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np
from scipy import optimize
from matplotlib import pylab as plt
from math import *
from scipy import linalg

def f(x):
     return sin(x/5.0) * exp(x / 10.0) + 5.0 * exp(-x / 2.0)


# In[6]:


solve=[]
for i in range(30):
    solve.append(f(i))
solve = np.array(solve)


# In[56]:


def h(x):
       return int(f(x))


# In[7]:


print(solve)


# In[12]:


z=np.arange(1,30,0.1)
ylist = [f(x) for x in z]
plt.plot(z,ylist)
plt.show()


# In[42]:


x_min = optimize.minimize(f,1)
print(x_min)


# In[ ]:





# In[ ]:





# In[ ]:





# In[43]:


x_min = optimize.minimize(f,15)
print(x_min)


# In[47]:


x_min = optimize.minimize(f,2,method='BFGS')
print(x_min)


# In[48]:


x_min = optimize.minimize(f,30,method='BFGS')
print(x_min)


# In[55]:


x_min = optimize.differential_evolution(f,[(1,30)])
print(x_min)


# In[57]:


z=np.arange(1,30,0.1)
ylist = [h(x) for x in z]
plt.plot(z,ylist)
plt.show()


# In[60]:


x_min = optimize.minimize(h,30,method='BFGS')
print(x_min)


# In[61]:


x_min = optimize.differential_evolution(h,[(1,30)])
print(x_min)


# In[ ]:




