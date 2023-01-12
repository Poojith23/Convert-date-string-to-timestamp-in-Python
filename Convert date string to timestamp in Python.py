#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Python program to convert 
# date to timestamp
  
  
  
import time
import datetime
  
  
string = "20/01/2020"
  
element = datetime.datetime.strptime(string,"%d/%m/%Y")
  
tuple = element.timetuple()
timestamp = time.mktime(tuple)
  
print(timestamp)


# In[ ]:




