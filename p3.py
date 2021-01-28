#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:29:03 2020

@author: carrot
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections as cl

def FiveSummaryAndMore(data_):
    data = sorted(data_)
    n = len(data)
    
    #Five summary
    mini = data[0]
    q1 = data[int((n+1)*1/4)]
    q2 = data[int((n+1)*2/4)]
    q3 = data[int((n+1)*3/4)]
    maxi = data[-1]
    
    #Mean & Standard Desviation
    m = np.mean(data)
    stdd = np.std(data)
    
    result = [mini, q1, q2, q3, maxi, m, stdd, data]
    
    return result

def Results(result, devtype):
    print('\n', devtype)
    print('*******************************************')
    print('Min: ', result[0])
    print('Max: ', result[4])
    print('1st Quartile: ', result[1])
    print('1st Quartile: ', result[2])
    print('3rd Quartile: ', result[3])
    print('Mean: ', result[5])
    print('Standar Desviation: ', result[6])
    print('*******************************************')
    fig = plt.figure()
    fig.suptitle(devtype + ' salary at year', fontsize=14, fontweight='bold')
    plt.boxplot(result[7])
    plt.show()

dir_ = '~/Documents/python/stadistics/'
name_ = 'survey_results_public.csv'
file = dir_ + name_

data = pd.read_csv(file)

devtype = data['DevType']
salary = data['ConvertedComp']
    
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
salaries = []

for i in range(len(dev)):
    a = []
    for d, s in zip(devtype, salary):        
        if not pd.isnull(d):
            if dev[i] in d:
                if not pd.isnull(s):
                    a.append(s)
    salaries.append(a)
    
for d, s in zip(dev, salaries):
    Results(FiveSummaryAndMore(s), d)
        