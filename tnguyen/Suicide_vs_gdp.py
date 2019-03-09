#!/usr/bin/env python
# coding: utf-8

# In[19]:


#Dependencies
import requests
import json
from matplotlib import pyplot as plt
from scipy.stats import linregress
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[20]:


# The path to our CSV file
file_gdp = "suicides_vs_gdp_o.csv"

# Read Suicide Data our Kickstarter data into pandas
su_vs_gdp_o_df = pd.read_csv(file_gdp)
su_vs_gdp_o_df.head()


# In[21]:


su_vs_gdp_o_df.columns


# In[22]:


su_vs_gdp_o_df.info()


# In[23]:


su_vs_gdp_df = su_vs_gdp_o_df.groupby('country-year').agg({'country':'first', 'year':'first', 
                                                           'suicides_no':'sum','population':'sum', 
                                                           'suicides/100k pop':'sum',
                                                           'year_gdp':'first',
                                                           'gdp_per_capita ($)':'first'}).reset_index()
su_vs_gdp_df.head()


# In[24]:


su_vs_gdp_df.to_csv('cleaned_su_vs_gdp.csv')


# In[25]:


# The path to our CSV file
file_gdp2 = "cleaned_su_vs_gdp.csv"

# Read Suicide Data our Kickstarter data into pandas
su_vs_gdp_c_df = pd.read_csv(file_gdp2)
su_vs_gdp_c_df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




