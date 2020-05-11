# 创建对象
import pandas as pd
import numpy as np

# 1. 可以通过传递一个list对象来创建一个Series，pandas会默认创建整型索引
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
print('============================')

# 2. 通过传递一个numpy array，时间索引以及列标签来创建一个DataFrame
dates = pd.date_range('20130101',periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print(df)
print('============================')

# 3. 通过传递一个能够被转换成类似序列结构的字典对象来创建一个DataFrame
df2 = pd.DataFrame({'A':1.,
                    'B':pd.Timestamp('20130102'),
                    'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D':np.array([3] * 4,dtype='int32'),
                    'E':pd.Categorical(["test","train","test","train"]),
                    'F':'foo' })
print(df2)
print('============================')

# 4. 查看不同列的数据类型
print(df2.dtypes)
print('============================')
