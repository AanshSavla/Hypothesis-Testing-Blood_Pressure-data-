# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:52:01 2020

@author: User
"""

import  pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests

df = pd.read_csv(r"D:\AanshFolder\datasets\blood_pressure.csv")
#print(df.head())

ttest,pval = stats.ttest_rel(df['bp_before'],df['bp_after'])
print(pval)

if(pval < 0.05):
    print("Reject null hypothesis")
else:
    print("Accept null hypothesis")
    
ztest,pval1 = stests.ztest(df['bp_before'],df['bp_after'],value=0,alternative='two-sided')
print(float(pval1))

df_anova = pd.read_csv(r"D:\AanshFolder\datasets\PlantGrowth.csv")
df_anova = df_anova[['weight','group']]

grps = pd.unique(df_anova.group.values)
print(grps)
d_data = {grp:df_anova['weight'][df_anova.group == grp] for grp in grps}

F,p = stats.f_oneway(d_data['ctrl'],d_data['trt1'],d_data['trt2'])
print("p-value for significance is:",p)
if p< 0.05:
    print("Reject null hypothesis.")
else:
    print("Accept null hypothesis.")
    
df_chi = pd.read_csv(r"D:\AanshFolder\datasets\chi-test.csv")

contingency_table = pd.crosstab(df_chi['Gender'],df_chi['Like Shopping?'])
print("Contingency table:-\n",contingency_table)

Observed_Values = contingency_table.values
print("Observed Values:-\n",Observed_Values)

b=stats.chi2_contingency(contingency_table)
Expected_Values = b[3]
print("Expected Values: -\n",Expected_Values)

no_of_rows = len(contingency_table.iloc[0:2,0])
no_of_columns = len(contingency_table.iloc[0,0:2])
df11 = (no_of_rows-1)*(no_of_columns-1)
print("Degree of freedom:",df)
alpha=0.05

from scipy.stats import chi2
chi_square = sum([(o-e)**2./e for o,e in zip(Observed_Values,Expected_Values)])
chi_square_statistics = chi_square[0]+chi_square[1]
print("chi-square statistics:",chi_square_statistics)
    
    