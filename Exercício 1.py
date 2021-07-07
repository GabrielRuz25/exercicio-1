#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np 
import matplotlib.pyplot as plt 

x=np.logspace(1, 9, num=20, base=6)
print (x) 
y=x+1/x
print (y)



plt.plot(y,x,)
plt.xlabel('eixo X')
plt.ylabel('eixo Y')
plt.title('Grafico Exercício')
plt.show 


# In[ ]:




