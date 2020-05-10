# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:07:50 2020

@author: harpn
"""

import pandas as pd
import matplotlib.pyplot as plt
import math as mt
import collections as col
import operator as op

w_d = 'C:/Users/harpn/OneDrive - Universidad de Guanajuato/Mineria/practice/'
i_f = w_d+'survey_results_public.csv'

data = pd.read_csv(i_f, encoding = 'utf-8')
values = data['DevType']

datos = dict(col.Counter(values)) 
maxi = max(datos.items(), key=op.itemgetter(1))[0]

plt.bar(range(len(datos)), datos.values(), align='center')
plt.xticks(range(len(datos)), list(datos.keys()))

plt.show()
