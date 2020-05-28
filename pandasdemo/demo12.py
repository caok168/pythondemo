# 导入和保存数据
import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
ts = ts.cumsum()
df = pd.DataFrame(np.random.randn(1000,4),index=ts.index,
                  columns=['A','B','C','D'])

print(np.random.randn(1000,4))

df.to_csv('foo.csv')
data = pd.read_csv('foo.csv')
# print(data)

df.to_hdf('foo.h5','df')
data = pd.read_hdf('foo.h5','df')
print(data)

df.to_excel('foo.xlsx',sheet_name="Sheet1")
data = pd.read_excel('foo.xlsx','Sheet1',index_col=None,na_values=['NA'])
print(data)