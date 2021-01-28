#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:37:24 2020

@author: carrot
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import collections as cl

def AndMore(data_):
    if data_ == []:
        result = 0
    else:
        data = sorted(data_)
        n = len(data)
        
        if n%2:
            q2 = data[int(np.floor(n/2))]
        else:
            if n == 1:
                q2 = data[0]
            else:
                nn = int(n/2)
                q2 = (data[nn] + data[nn-1]) / 2
        
        #Mean & Standard Desviation
        m = np.mean(data)
        stdd = np.std(data)
        
        result = [q2, m, stdd, data]
    
    return result

def Results(result, country):
    if result == 0:
        print('\n', country, " doesn't have values")
    else:
        print('\n', country)
        print('*******************************************')
        print('Median: ', result[0])
        print('Mean: ', result[1])
        print('Standar Desviation: ', result[2])
        print('*******************************************')
        fig = plt.figure()
        fig.suptitle(country + ' salary at year', fontsize=14, fontweight='bold')
        plt.boxplot(result[3])
        plt.show()

dir_ = '~/Documents/python/stadistics/'
name_ = 'survey_results_public.csv'
file = dir_ + name_

data = pd.read_csv(file)

country = data['Country']
salary = data['ConvertedComp']
    
countries_ = list(set(country))
countries = countries_[1:]
salaries = []

for cc in countries:
    aux = []
    for c, s in zip(country, salary):
        if not pd.isnull(c):
            if cc == c:
                if not pd.isnull(s):
                    aux.append(s)
    salaries.append(aux)

for c, s in zip(countries, salaries):
    Results(AndMore(s), c)
