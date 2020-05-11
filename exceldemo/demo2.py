import pandas as pd
import numpy as np

df1 = pd.read_excel("./files/excel-comp-data.xlsx")
print(df1)
print('---------------------')
print(df1['city'])
print('---------------------')
print(df1.city)

df1['Total'] = df1['Jan'] + df1['Feb'] + df1['Mar']
print('**********************')
print(df1['Jan'],df1['Feb'],df1['Mar'],df1['Total'])

print('**********************')

df1['category'] = np.where(df1['Total'] > 200000,'A','B')
df1.head()

df1.to_excel('./files/excel-comp-data-new.xlsx',sheet_name='test')
