import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

Ourdf = pd.read_csv('SalesScenario1.csv')




plt.figure(figsize=(12,8))
ax = sns.pointplot(y='Total Sales', x='Course spend', hue='Salesperson',data=Ourdf)
ax.grid(b=True, which='major', color='#d3d3d3', linewidth=1.0)
ax.grid(b=True, which='minor', color='#d3d3d3', linewidth=0.5)
plt.show()