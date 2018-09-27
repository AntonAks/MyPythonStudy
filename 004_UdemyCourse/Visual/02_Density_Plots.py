#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 15:59:54 2018

@author: antonaks
"""
# Standard imports

import numpy as np
import pandas as pd
from numpy.random import randn

# Stats
from scipy import stats

# Plotting
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

dataset = randn(25)

sns.rugplot(dataset)
plt.ylim(0,1)


plt.hist(dataset
         ,alpha=0.3
         ,)
sns.rugplot(dataset)

sns.rugplot(dataset)

x_min=dataset.min() - 2
x_max=dataset.max() + 2

x_axix = np.linspace(x_min, x_max, 100)

bandwith = ((4*dataset.std()**5) / (3*len(dataset))) ** 0.2
bandwith 


kernel_list = []

for data_point in dataset:
    # Create a kernel for each point and append it to the list
    kernel = stats.norm(data_point, bandwith).pdf(x_axix)
    kernel_list.append(kernel)
    
    # Scale for ploting    
    kernel = kernel / kernel.max()
    kernel = kernel * 0.4
    
    plt.plot(x_axix,kernel,color='grey',alpha=0.5)

plt.ylim(0,1)



sum_of_kde = np.sum(kernel_list, axis=0)
fig = plt.plot(x_axix, sum_of_kde, color='indianred')



sns.kdeplot(dataset)
sns.rugplot(dataset, color='black')
for bw in np.arange(0.5, 2, 0.25):
    sns.kdeplot(dataset, bw=bw, lw=1.0, label = bw)
    
    

    
    
    