#!/usr/bin/env python3

import pandas as pd

data = pd.read_csv('data/diabetes.data', sep='\\s+', header=0)

#print(data.to_string())

print('Print all the women data having age more than 30 :')
print(data[ (data['SEX'] == 2) & (data['AGE'] > 30) ] )


print( '\nCorrelations on the dataset: ' )
print(data.corr())