#!/usr/bin/env python
# coding: utf-8

# Write a function that takes in an integer, minutes, and converts it into seconds

# In[5]:


def min_to_sec(a):
    return str(a*60) +' Seconds'


# In[6]:


#test case 1
min_to_sec(10)


# In[7]:


#test case 2
min_to_sec(2)


# Write a function that takes two numbers as arguments and returns their sum.

# In[24]:


def sum_numbers(a,b):
    return 'The sum of '+str(a)+' and '+str(b)+' is '+str(a+b)


# In[25]:


#test case 1
sum_numbers(5,10)


# In[26]:


#test case 2
um_numbers(15,10)


# Create a function that takes a string and returns the number (count) of vowels contained within it.

# In[37]:


def count_vowel(text):
    count=0
    for i in range(len(text)):
        if text[i].lower() in ['a','e','i','o','u']: #added lower here as my list contained lower case vowels
            count+=1
        else:
            i+=1
    return count


# In[38]:


#test case 1
count_vowel('It is a windy day here in the city')


# In[39]:


#test case 2
count_vowel('I love Modern Family. It is an amazing show')


# Create a function that takes a number as an argument and returns "Fizz", "Buzz" or "FizzBuzz".
# If the number is a multiple of 3 the output should be "Fizz".
# If the number given is a multiple of 5, the output should be "Buzz".
# If the number given is a multiple of both 3 and 5, the output should be "FizzBuzz".
# If the number is not a multiple of either 3 or 5, the number should be output on its own as shown in the examples below.
# The output should always be a string even if it is not a multiple of 3 or 5. 
# 

# In[41]:


def fizz_buzz(a):
    if a%3==0 and a%5==0:
        return 'FizzBuzz'
    if a%5==0:
        return 'Buzz'
    if a%3==0:
        return 'Fizz'
    else:
        return str(a)


# In[48]:


#test case 1 a multiple of 5 only!
fizz_buzz(10)


# In[49]:


#test case 2 a multiple of 3 only!
fizz_buzz(18)


# In[50]:


#test case 3 a multiple of both 5 and 3!
fizz_buzz(15)


# In[51]:


#test case 4 a number which is not a multiple of either!
fizz_buzz(28)


# In[ ]:




