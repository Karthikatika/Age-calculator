#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import date
y=date.today().year
m=date.today().month
d=date.today().day
print(date.today())

from datetime import date
def calculateAge(birthDate):
    days_in_year = 365   
    age = int((date.today() - birthDate).days / days_in_year)
    return age
         
print(calculateAge(date(2001,11, 30)), "years")


# In[ ]:





# In[ ]:





# In[ ]:




