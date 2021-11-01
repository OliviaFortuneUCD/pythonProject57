import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats

Ourdf = pd.read_csv('SalesScenario1.csv')




x=Ourdf['Course spend']
y=Ourdf['Total Sales']

corr = stats.pearsonr(x, y)
print("All salespersons" ,corr)


x1=Ourdf.loc[Ourdf['Salesperson'] == 1, 'Course spend']
y1=Ourdf.loc[Ourdf['Salesperson'] == 1, 'Total Sales']

corr1 = stats.pearsonr(x1, y1)
print("salesperson 1" ,corr1)


x2=Ourdf.loc[Ourdf['Salesperson'] == 2, 'Course spend']
y2=Ourdf.loc[Ourdf['Salesperson'] == 2, 'Total Sales']

corr2 = stats.pearsonr(x2, y2)
print("salesperson 2" ,corr2)

x3=Ourdf.loc[Ourdf['Salesperson'] == 3, 'Course spend']
y3=Ourdf.loc[Ourdf['Salesperson'] == 3, 'Total Sales']

corr3 = stats.pearsonr(x3, y3)
print("salesperson 3" ,corr3)


x4=Ourdf.loc[Ourdf['Salesperson'] == 4, 'Course spend']
y4=Ourdf.loc[Ourdf['Salesperson'] == 4, 'Total Sales']

corr4 = stats.pearsonr(x4, y4)
print("salesperson 4" ,corr4)

