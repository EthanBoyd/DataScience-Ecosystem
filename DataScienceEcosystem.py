#!/usr/bin/env python
# coding: utf-8

# # Data Science Tools and Ecosystem

# In this notebook, Data Science Tools and Ecosystem are summarized.

# **Objectives:**
#     
#     - List some of the popular languages that Data Scientists use
#     - List some of the commonly used libraries in Data Science
#     - Write a function to convert minutes to hours

# In[ ]:


Some of the popular languages that Data Scientists use are:

    1. Python
    2. R
    3. Julia
    4. SQL


# Some of the commonly used libraries used by Data Scientists include:
#     
#     1. Pandas
#     2. NumPy
#     3. TensorFlow
#     4. SciKit-Learn

# | Data Science Tools |
# | - |
# | Jupyter Notebooks |
# | Zeppelin Notebooks |
# | R Studio |

# ### Below are a few examples of evaluating arithmetic expressions in Python:
# 

# This a simple arithmetic expression to mutiply then add integers:

# In[8]:


(3*4)+5


# This will convert 200 minutes to hours by diving by 60

# In[10]:


total_minutes = 200

# Get hours with floor division
hours = total_minutes // 60

# Get additional minutes with modulus
minutes = total_minutes % 60

# Create time as a string
time_string = "{}:{}".format(hours, minutes)

print(time_string)

    


# ## Author
# 
# Ethan Boyd

# In[ ]:




