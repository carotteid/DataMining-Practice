#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:36:40 2020

@author: carrot editada 25/02/2021
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

def Results(result, gender):
    print('\n', gender)
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
    fig.suptitle(gender + ' salary at year', fontsize=14, fontweight='bold')
    plt.boxplot(result[7])
    plt.show()

dir_ = '~/Documents/python/stadistics/'
name_ = 'survey_results_public.csv'
file = dir_ + name_

data = pd.read_csv(file)

gender = data['Gender']
salary = data['ConvertedComp']

aux_m = []
aux_w = []
aux_n = []

for g, s in zip(gender, salary):
    if not pd.isnull(g):
        if 'Man' in g and not np.isnan(s):
            aux_m.append(s)
        if 'Woman' in g and not np.isnan(s):
            aux_w.append(s)
        if 'Non-binary, genderqueer, or gender non-conforming' in g and not np.isnan(s):
            aux_n.append(s)

#Woman
Results(FiveSummaryAndMore(aux_w), 'Woman')

#Man
Results(FiveSummaryAndMore(aux_m), 'Man')

#Non-Binary
Results(FiveSummaryAndMore(aux_n), 'Non-Binary')


