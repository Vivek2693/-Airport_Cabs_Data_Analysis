#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[6]:


taxi_data = np.genfromtxt('C:\\Users\\Vivek\\Downloads\\nyc_taxis.csv',delimiter = ",",skip_header=1 )


# In[14]:


speed = taxi_data[:,7]/(taxi_data[:,8]/3600)


# # Q1. Average speed of all the cabs

# In[44]:


mean_speed = speed.mean()   # in mph
print(mean_speed)


# ## Q2. Total Rides in Feb

# In[19]:


Rides_feb = taxi_data[taxi_data[:,1]==2,1]


# In[23]:


Rides_feb.shape[0]


# ## Q3. Calculate the number of rides with tip greter than $50

# In[41]:


tips = taxi_data[taxi_data[:,12]>50,-3]


# In[42]:


Tips.shape[0]


# In[43]:


(taxi_data[taxi_data[:,12]>50,-3].shape[0])


# ## Q4. Calculate the Number of rides where the drop was Jfk airport, Location code = 2

# In[46]:


taxi_data[taxi_data[:,6] == 2,6].shape[0]


# In[ ]:





# In[ ]:





# In[ ]:




