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


data_set_1 = randn(100)
data_set_2 = randn(200)

hist1= plt.hist(data_set_1, 
         color='indianred', 
         normed=True, 
         alpha=0.5, 
         bins=20)

hist2= plt.hist(data_set_2, 
#         color='indianred', 
         normed=True,   
         alpha=0.2, 
         bins=20)


data1 = randn(1000)
data2 = randn(1000)

sns.jointplot(data1, data2, kind='hex')









