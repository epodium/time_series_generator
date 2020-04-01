#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import sys
import numpy as np
from scipy import signal as scipysig
from matplotlib import pyplot as plt


# In[2]:


ROOT = os.path.abspath(os.pardir)
# sys.path.insert(0, ROOT)

import TS_generator as TSgen


# ## Simple test example

# In[3]:


TS_def = {'class_name' : 'Simple example',
          'n_timepoints' : 400,
          'n_channels' : 6,
          'signal_defs' : [{'peaks_per_ch' : 1,
                           'channels' : [3,4,5],
                           'n_ch' : [2, 3],
                           'length' : [50,80],
                           'position' : [50,160],
                           'extra_shift' : [-10,10],
                           'amp' : [0.7,1],
                           'sign' : 1,
                           'signal_type' : 'peak_exponential'
                         }],
          'noise_defs' : [{'channels' : 'all',
                           'noise_amp' : [0.05,0.06],
                          'noise_type' : 'gaussian'
                         },
                         {'channels' : 'all',
                          'noise_amp' : [0.018,0.022],
                          'noise_type' : 'random_walk'
                         }]
          }

TS_def['noise_defs'][0]


# In[4]:


X = TSgen.generate_TS(TS_def,
                random_seed = None,
                ignore_noise = True)

TSgen.plot_TS(X, TS_def)


# # General workflow:
# ## 1) Import time series classes from yaml files

# In[5]:


PATH_classes = os.path.join(ROOT, 'TS_types')
filename = os.path.join(PATH_classes, 'TS_type_show_variety.yaml')

TS_def = TSgen.load_TS_class(filename)


# In[6]:


TS_def


# ## 2) Generate time series based on class definition

# In[7]:


X = TSgen.generate_TS(TS_def,
                random_seed = None,
                ignore_noise = True)

TSgen.plot_TS(X, TS_def)


# In[8]:


X = TSgen.generate_TS(TS_def,
                random_seed = None)

TSgen.plot_TS(X, TS_def)


# ## 3) Generate entire data set

# In[9]:


X_data, y_data = TSgen.generate_dataset([filename],
                                      200,
                                      random_seed = None)


# In[10]:


X_data.shape


# In[11]:


list(set(y_data))


# In[ ]:




