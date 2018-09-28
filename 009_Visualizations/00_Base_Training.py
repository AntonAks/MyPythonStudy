"""
Created on Thu Sep 27 23:10:44 2018

@author: antonaks
"""
import seaborn as sns
import pandas as pd
import numpy as np

from pandas import DataFrame

path = '/home/antonaks/PythonProjects/MyPythonStudy/010_Data/'
file_name = 'countries of the world.csv'
df = pd.read_csv(str(path + file_name),sep = ',')

# observing columns in data frame
df.columns

# add new column
df['new col'] = None

# delete column
del df['new col']

# create new data frame from exist
df_new = DataFrame(df, columns=['Country','Region','Population','Industry','Deathrate'])


# replace "," with "." for convert string values to numeric
df_new['Industry'] = df_new['Industry'].str.replace(',','.')
df_new['Industry'] = pd.to_numeric(df_new['Industry'])

df_new['Deathrate'] = df_new['Deathrate'].str.replace(',','.')
df_new['Deathrate'] = pd.to_numeric(df_new['Deathrate'])

df_new['Deathrate'] = df_new['Deathrate'].str.replace(',','.')
df_new['Deathrate'] = pd.to_numeric(df_new['Deathrate'])



# add column with random values
df_new['Random_Value'] = np.random.randn(len(df_new['Industry']))


# example of selecting data from dataframe by conditions
df_new[df_new['Deathrate']>20]
df_new[(df_new['Industry']==0.24) & (df_new['Deathrate']>20)]   
df_new[(df_new['Industry']<=0.1) | (df_new['Deathrate']<10)]   


# group by statement 
grouped_df = df_new.groupby('Region').mean()

 
# scater plot
sns.scatterplot(data=df_new, x='Deathrate', y='Industry')


# pairplot
sns.pairplot(data=df_new, kind='reg')


