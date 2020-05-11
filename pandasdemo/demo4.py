# 相关操作
import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))

# 1.统计（相关操作通常情况下不包括缺失值）
# 1.1 执行描述性统计
print(df.mean)
print('=============================================')

# 1.2 在其他轴上进行相同的操作
print(df.mean(1))
print('=============================================')

# 1.3 对于拥有不同维度，需要对齐的对象进行操作。Pandas会自动的沿着指定的维度进行广播
s = pd.Series([1,3,5,np.nan,6,8],index=dates).shift(2)
print(s)
print(df)
df11 = df.sub(s,axis='index')
print(df11)
print('=============================================')

# 2.Apply
# 2.1 对数据应用函数
df11 = df.apply(np.cumsum)
print(df11)
df11 = df.apply(lambda x:x.max() - x.min())
print(df11)
print('=============================================')

# 3.直方图
s = pd.Series(np.random.randint(0,7,size=10))
print(s)
print(s.value_counts())
print('=============================================')

# 4.字符串方法
s = pd.Series(['A','B','C','Aaba','Baca',np.nan,'CABA','dog','cat'])
print(s)
s = s.str.lower()
print(s)
