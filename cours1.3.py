#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np

from matplotlib import pylab as plt
from math import *
from scipy import linalg
def f(x):
     return sin(x/5.0) * exp(x / 10.0) + 5.0 * exp(-x / 2.0)

solve = np.array([f(1),f(15)])
a = np.array([[1, 1], [1, 15]])
otvet = linalg.solve(a, solve)
print(otvet)


# In[ ]:





# In[46]:


z=np.arange(1,15,0.1)
y=otvet[0]+otvet[1]*z
plt.plot(z,y)
plt.show()


# In[47]:


import numpy as np
z=np.arange(1,15,0.1)
ylist = [f(x) for x in z]
plt.plot(z,ylist)
plt.show()


# In[4]:



# !!! Создадим список координат по оси X на отрезке [-xmin; xmax], включая концы
xlist = mlab.frange (xmin, xmax, dx)

# Вычислим значение функции в заданных точках
ylist = [func (x) for x in xlist]

# !!! Нарисуем одномерный график
pylab.plot (xlist, ylist)

# !!! Покажем окно с нарисованным графиком
pylab.show()


# In[5]:


a2 = np.array([[1, 1,1], [1, 8,64], [1, 15,225]])


# In[36]:


f(1)


# In[41]:


solve2 = np.array([f(1),f(8),f(15)])


# In[31]:


print(a2)


# In[42]:


print(solve2)


# In[43]:


otvet2 = linalg.solve(a2, solve2)
print(otvet2)


# In[44]:


z=np.arange(1,15,0.1)
y=otvet2[0]+otvet2[1]*z+otvet2[2]*z*z
plt.plot(z,y)
plt.show()


# In[11]:


a3= np.array([[1, 1,1,1],[1,4,16,64],[1,10,100,1000],[1,15,225,3375]])


# In[53]:


solve3 = np.array([f(1),f(4),f(10),f(15)])


# In[49]:


print(a3)


# In[54]:


print(solve3)


# In[55]:


otvet3 = linalg.solve(a3, solve3)
print(otvet3)


# In[56]:


z=np.arange(1,15,0.1)
y=otvet3[0]+otvet3[1]*z+otvet3[2]*z*z+otvet3[3]*z*z*z
plt.plot(z,y)
plt.show()


# In[57]:


f = open(r'C:\Users\Арсений\Desktop\кошки.txt', 'w')
for col in range(len(otvet3)):
    otvet[col]=str(otvet[col])
f.write(otvet3)
f.close()


# In[18]:


otvet4 = linalg.solve(a3, otvet3)


# In[19]:


print(otvet4)


# In[20]:


print(a3.dot(otvet3))


# In[58]:


print('{:.2f}'.format(otvet3[0])+' '+'{:.2f}'.format(otvet3[1])+' '+'{:.2f}'.format(otvet3[2])+' '+'{:.2f}'.format(otvet3[3]))


# In[ ]:




