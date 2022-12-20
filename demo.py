# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 11:21:37 2022

@author: Kalal
"""

import pandas as pd

print(pd.__version__);

data = pd.read_csv('heart.csv')
# print(data.columns)
# print(data.dtypes)
# print(data.select_dtypes('O'))


# data.rename(columns= {'age': 'ages'}, inplace= True)
# df = data['sex']

# adults = data.loc[data['ages']>18]

# max_ages = data.ages.max()
# min_ages = data.ages.min()

# mean_ages = data.ages.mean()
# median_ages = data.ages.median()

# a = {'age':21, 'name': 'abc', 'marrital_status': 'single'}
# print(a.keys())
# print(a.items())
# print(a.values())

# _____________________________________________________________________________

print(data.dtypes)
def age_count(df):
    if df.age>=18 and df.age<60:
        return 'junior'
    else:
        return 'senior citizen'
    
data['age_group'] = data.apply(age_count, axis=1)

data.to_csv('a.csv', index= False)

age_count = data.groupby('age', as_index= False)['chol'].count()
thal_count = data.groupby('thal').agg({'age': 'count'})

thal_count.to_excel('abc.xlsx')

# ___________________________________________________________________________

a = data.sort_values('age', ascending= False)