# -*- coding: utf-8 -*-
"""
Created on Wed May  6 02:34:23 2020

@author: IdAvila
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math as mt
import seaborn as sns

def quartile(lista, percentile):
    q = (len(lista)-1)*percentile
    pl = mt.floor(q)
    pu = mt.ceil(q)
    
    return lista[pl]+(lista[pu]-lista[pl])*percentile

def fiveNumbers(lista):
    lista.sort()
    
    n = len(lista)

    min_number = lista[0]
    max_number = lista[n-1]
    q1 = quartile(lista, 0.25)
    q2 = quartile(lista, 0.5)
    q3 = quartile(lista, 0.75)
    mean = sum(lista)/n
    
    s = sum([(d-q2) **2 for d in lista])
        
    v = s/(n-1)
    de = v**(1/2)
    
    print('Min:',str(min_number))
    print('Max:',str(max_number))
    print('1st Quartile:',str(q1)) 
    print('2st Quartile (Median):',str(q2))
    print('3st Quartile:',str(q3))
    print('Mean:',str(mean))
    print('Desviación estandar:', str(de))

w_d = 'C:/Users/harpn/OneDrive - Universidad de Guanajuato/Mineria/practice/'
i_f = w_d+'survey_results_public.csv'

data = pd.read_csv(i_f, encoding = 'utf-8')

column = 'ConvertedComp'
values = data[column].tolist()
n = len(values)

man = 0
woman = 0

list_man = []
list_woman = []

"""
for val in values:
    if not mt.isnan(val):
        if data['Gender'] == 'Man':
            list_man.append(val)
        elif data['Gender'] == 'Woman':
            list_woman.append(val)
"""

for index, row in data.iterrows():
    cost = row[column]
    
    if not mt.isnan(cost):
        if cost == 0:
            continue
        else:
            if (row['Gender'] == 'Man'):
                list_man.append(cost)
            elif (row['Gender'] == 'Woman'):
                list_woman.append(cost)
    
"""
for val in values:
    if val == 'Man': 
        list_.append(val)
        man+=1
    elif val == 'Woman':
        list_.append(val)
        woman+=1
"""
    

#plt.boxplot(list_man)
#print('hello')
print('Man salaries: \n')
fiveNumbers(list_man)
print('\nWoman salaries: \n')
fiveNumbers(list_woman)

fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].boxplot(list_man)
axes[1].boxplot(list_woman)
plt.show()