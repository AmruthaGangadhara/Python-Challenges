#!/usr/bin/env python
# coding: utf-8

# Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.

# In[18]:


def calc_discount(a,b):
    discount=(a-((b/100)*a))
    return 'discount price is $' +str(round(discount,2))


# In[19]:


#test case 1
calc_discount(1799,50)


# In[20]:


#test case 2
calc_discount(2799,30)


# Create a function that takes the age in years and returns the age in days.

# In[21]:


def age(a):
    return 'current age in days is '+str(a*365)


# In[22]:


#tess case 1
age(28)


# In[23]:


#test case 2
age(35)


# In[24]:


#test case 2
age(45)


# Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.

# In[25]:


import math
# formula to calculate angle in degrees:
#Angle in Radians × 180°/π = Angle in Degrees

def radian_to_angle(a):
    degree=(a*(180/math.pi)) 
    return round(degree,1)


# In[26]:


#test case 1
radian_to_angle(5)


# In[27]:


#test case 2
radian_to_angle(25)


# Create a function, get_days, that takes two dates and returns the number of days between the first and second date. 
# 

# In[36]:


from datetime import datetime
def get_days(startdate,enddate):
    d1=datetime.fromisoformat(startdate)  #fromisoformat converst string obj into date format
    d2=datetime.fromisoformat(enddate)
    difference=d2-d1
    return difference.days               #you can choose how you want the difference.(seconds/macroseconds/etc.)


# In[37]:


#test case 1
get_days('2022-02-20', '2022-03-01')


# In[38]:


#test case 1
get_days('2022-02-25', '2022-03-25')


# In[ ]:




