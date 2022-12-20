# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:21:37 2022

@author: Kalal
"""

import pandas as pd

print(pd.__version__);

data = pd.read_csv('heart.csv')
print(data.columns)
print(data.dtypes)
print(data.select_dtypes('O'))


data.rename(columns= {'age': 'ages'}, inplace= True)
df = data['sex']

adults = data.loc[data['ages']>18]

max_ages = data.ages.max()
min_ages = data.ages.min()

mean_ages = data.ages.mean()
median_ages = data.ages.median()

a = {'age':21, 'name': 'abc', 'marrital_status': 'single'}
print(a.keys())
print(a.items())
print(a.values())