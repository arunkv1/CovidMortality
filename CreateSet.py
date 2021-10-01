#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 11:31:43 2020

@author: arunkrishnavajjala
"""

import pandas as pd


covid = pd.read_csv('/Users/arunkrishnavajjala/Documents/GMU/URA/project/CountryCodes.csv', sep=',')

two5 = pd.read_csv('/Users/arunkrishnavajjala/Documents/GMU/URA/project/EXP_PM2_5_09082020173536735.csv', delimiter=',')


df_filtered = two5[two5['Unit'] == "Micrograms per cubic metre"] 

print(df_filtered.shape)

merged_inner = pd.merge(left=covid, right=two5, left_on='COU', right_on='COU')

merged_inner = merged_inner.drop_duplicates(subset=['COU'])

print(merged_inner.shape)

merged_inner.to_csv('out.csv', index=False)  

#%%
import pycountry

covidCol = pd.DataFrame()
for i in covid.iterrows():
    
    mapping = {country.name: country.alpha_3 for country in pycountry.countries}
    val = mapping.get(i[1][0])
    
    print(val)
    
    

