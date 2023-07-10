#!/usr/bin/env python
# coding: utf-8

# #### Create a function that takes in a current mood and return a sentence in the following format: “Today, I am feeling {mood}”. However, if no argument is passed, return “Today, I am feeling neutral”.

# In[14]:


def generate_mood(feeling='neutral'):
    return 'Today, I am feeling {}'.format(feeling)
    


# In[15]:


generate_mood('happy')


# In[16]:


generate_mood()


# In[ ]:




