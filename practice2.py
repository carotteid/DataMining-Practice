# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:28:31 2020

@author: harpn
"""

import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import collections as col

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

column = 'Ethnicity'
values = data[column].tolist()
n = len(values)

man = 0
woman = 0

list_man = []
list_woman = []



datos = dict(col.Counter(values)) 
d_datos = datos.keys()
dates = d_datos.tolist()

#for index, row in data.iterrows():
#    if row['ConvertedComp']:
#        survived += 1
#        
#        if row['Sex'] == 'male':
#            mens_s += 1
#        else:
#            womens_s += 1
#    else:
#        deaths += 1
#        
#        if row['Sex'] == 'male':
#            mens_d += 1
#        else:
#            womens_d += 1