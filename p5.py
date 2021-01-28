#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 23:45:47 2020

@author: carrot
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections as cl

dir_ = '~/Documents/python/stadistics/'
name_ = 'survey_results_public.csv'
file = dir_ + name_

data = pd.read_csv(file)

devtype = data['DevType']

#Unique DevTypes
aux = []
for d in devtype:
    if not pd.isnull(d):
        if ';' in d:
            a = d.split(';')
            for i in a:
                aux.append(i)
        else:
            aux.append(d)
            
dev = list(set(aux))
count = []

for d in dev:
    i = 0
    for dt in devtype:
        if not pd.isnull(dt):
            if d in dt:
                i = i +1
    count.append(i)

plt.barh(np.arange(len(dev)), count, align='center', alpha=0.5)
plt.yticks(np.arange(len(dev)), dev)
plt.xlabel('Count')
plt.title('Developer type count')
plt.show()