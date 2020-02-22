#!/usr/bin/env python3

import pandas as pd

### 1

### 2
print('\n#2')

data = pd.read_csv('data/insurance.csv', sep=',', header=0)
#print(data.to_string())
#print(data.columns)
print(data.index)
print(data.dtypes)
print(data.shape)
print(data.info())
print(data.describe())



### 3
print('\n#3')
print(data['age'])



### 4
print('\n#4')
print(data[['age', 'children', 'charges']])



### 5
print('\n#5')
print(data[['age', 'children', 'charges']].head(5))



### 6
print('\n#6')
print('AVG: ', data['charges'].mean())
print('MIN: ', data['charges'].min())
print('MAX: ', data['charges'].max())



### 7
print('\n#7')
print(data[data['charges'] == 10797.3362][['age', 'sex']])
print('Was he/she a smoker? ', data[data['charges'] == 10797.3362][['smoker']])



### 8
print('\n#8')
max_charges = data['charges'].max()
print(data[data['charges'] == max_charges]['age'])



### 9
print('\n#9')
#print(data['region'])
print(data['region'].value_counts())



# 10
print('\n#10')
print('Numer of children :', data['children'].sum())


#11-12
print('\n#11-12')
print(data[['charges', 'age', 'bmi', 'children']].corr())