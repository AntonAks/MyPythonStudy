"""
Created on Thu Sep 27 23:10:44 2018

@author: antonaks
"""
import seaborn as sns
import pandas as pd
import numpy as np

from pandas import DataFrame, Series

path = '/home/antonaks/PythonProjects/MyPythonStudy/010_Data/'
file_name = 'countries of the world.csv'
df = pd.read_csv(str(path + file_name),sep = ',')

# observing columns in data frame
df.columns




