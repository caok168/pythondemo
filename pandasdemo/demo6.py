# 分组
import pandas as pd
import numpy as np

# l  （Splitting）按照一些规则将数据分为不同的组；
# l  （Applying）对于每组数据分别执行一个函数；
# l  （Combining）将结果组合到一个数据结构中；

df = pd.DataFrame({
    'A':['foo','bar','foo','bar','foo','bar','foo','foo'],
    'B':['one','one','two','three','two','two','one','three'],
    'C':np.random.randn(8),
    'D':np.random.randn(8)})

print(df)

# 1. 分组并对每个分组执行sum函数
print(df.groupby('A').sum())

# 2. 通过多个列进行分组形成一个层次索引，然后执行函数
print(df.groupby(['A','B']).sum())