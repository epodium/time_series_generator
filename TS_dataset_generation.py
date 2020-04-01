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

n_samples = 1000
random_seed = 1098
ignore_noise = True
X_data, y_data = TSgen.generate_dataset(
    TS_classes,
    n_samples,
    random_seed = random_seed,
    ignore_noise = ignore_noise)


# In[8]:


X_data.shape


# In[9]:


list(set(y_data))


# In[10]:


y_data[:10]


# In[Save dataset]:

np.save(f"y_data_s{n_samples}_n{int(not ignore_noise)}.npy", y_data)
np.save(f"x_data_s{n_samples}_n{int(not ignore_noise)}.npy", X_data)
