import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sns

Ourdf = pd.read_csv('SalesScenario1.csv')

x1=Ourdf.loc[Ourdf['Salesperson'] == 4, 'Course spend']
y1=Ourdf.loc[Ourdf['Salesperson'] == 4, 'Total Sales']
sns.regplot(x1, y1)
# to show
plt.show()


