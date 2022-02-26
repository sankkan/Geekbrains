#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt


# In[14]:


x=np.linspace(0,10,100)
plt.plot(x,x,x,np.cos(3*x))


# In[ ]:




