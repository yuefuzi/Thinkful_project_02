# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 21:10:41 2016

@author: Chang
"""

import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

s=[]
data = data.split('\n')
for i in data:
    i=i.split(",")
    s.append(i)

df = pd.DataFrame(s[1::],columns=s[0])
df.Alcohol=df.Alcohol.astype(float)
df.Tobacco=df.Tobacco.astype(float)
print("The mean of the Alcohol dataset is %.2f" % (df.Alcohol.mean()))
print("The mean of the Tobacco dataset is %.2f" % (df.Tobacco.mean()))
print("The median of the Alcohol dataset is %s" % (str(df.Alcohol.median())))
print("The median of the Tobacco dataset is %s" % (str(df.Tobacco.median())))
print("The mode(s) of the Alcohol dataset: %s" % (str(stats.mode(df.Alcohol))))
print("The mode(s) of the Tobacco dataset: %s" % (str(stats.mode(df.Tobacco))))
print("The range of the Alcohol dataset is %s" % (str(max(df.Alcohol)-min(df.Alcohol))))
print("The range of the Tobacco dataset is %s" % (str(max(df.Tobacco)-min(df.Tobacco))))
print("The standard deviation of the Alcohol dataset is %.2f" % (df.Alcohol.std()))
print("The standard deviation of the Tobacco dataset is %.2f" % (df.Tobacco.std()))
print("The variance of the Alcohol dataset is %.2f" % (df.Alcohol.var()))
print("The variance of the Tobacco dataset is %.2f" % (df.Tobacco.var()))

