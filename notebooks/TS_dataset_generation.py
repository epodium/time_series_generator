#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys
import numpy as np
from scipy import signal as scipysig
from matplotlib import pyplot as plt


# In[2]:


ROOT = ROOT = 'C:\\OneDrive - Netherlands eScience Center\\Project_ePodium\\time_series_generator'
sys.path.insert(0, ROOT)

import TS_generator as TSgen


# # General workflow:
# ## 1) Import time series classes from yaml files

# In[17]:


PATH_classes = os.path.join(ROOT, 'TS_types')
filename = os.path.join(PATH_classes, 'TS_type_test001.yaml')

TS_def = TSgen.load_TS_class(filename)


# In[18]:


X = TSgen.generate_TS(TS_def,
                    random_seed = None)

TSgen.plot_TS(X, TS_def)


# In[19]:


filename = os.path.join(PATH_classes, 'TS_type_test002.yaml')
TS_def = TSgen.load_TS_class(filename)
X = TSgen.generate_TS(TS_def,
                    random_seed = None)

TSgen.plot_TS(X, TS_def)


# In[12]:


filename = os.path.join(PATH_classes, 'TS_type_test003.yaml')
TS_def = TSgen.load_TS_class(filename)
X = TSgen.generate_TS(TS_def,
                    random_seed = None)

TSgen.plot_TS(X, TS_def)


# ## Generate entire data set

# In[6]:


TS_classes = []
for filename in ['TS_type_test000.yaml', 'TS_type_test001.yaml', 'TS_type_test002.yaml', 'TS_type_test003.yaml']:
    TS_classes.append(os.path.join(PATH_classes, filename))


# In[7]:


X_data, y_data = TSgen.generate_dataset(TS_classes,
                                      200,
                                      random_seed = None)


# In[8]:


X_data.shape


# In[9]:


list(set(y_data))


# In[10]:


y_data[:10]

