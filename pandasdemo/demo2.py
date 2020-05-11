# 查看数据
import pandas as pd
import numpy as np

# 1. 查看frame中头部和尾部的行
dates = pd.date_range('20130101',periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))

print(df.head(2))

print(df.tail(3))
print('============================')

# 2. 显示索引、列和底层的numpy数据
print(df.index)
print(df.columns)
print(df.values)
print('============================')

# 3. describe()函数对于数据的快速统计汇总
print(df.describe())
print('============================')

# 4. 对数据的转置
print(df.T)
print('========================================================')

# 5. 按轴进行排序
print(df.sort_index(axis=1,ascending=False))
print('========================================================')

# 6. 按值进行排序
# print(df.sort(columns='B'))


