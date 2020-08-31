#!/usr/bin/env python
# coding: utf-8

# In[15]:


lst = []
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        lst.append(i)
print(lst)
  

        


# In[12]:


first_name = input("Please enter your first name ")
last_name = input("Please enter your last name ")
print("User name is",last_name, first_name)


# In[13]:


import math
dia_cm = 12
rad_cm = dia_cm / 2
rad_m = rad_cm / 100.0     #converted radius in metre
Volume = (4/3 * math.pi * rad_m**3)
Volume


# In[ ]:




