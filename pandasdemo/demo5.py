# 合并
import pandas as pd
import numpy as np
# 1.Concat
df = pd.DataFrame(np.random.randn(10,4))
print(df)

pieces = [df[:3],df[3:7],df[7:]]
df11 = pd.concat(pieces)
print(df11)
print('=============================================')

# 2.Join 类似于SQL类型的合并
left = pd.DataFrame({'key':['foo','foo'],'lval':[1,2]})
right = pd.DataFrame({'key':['foo','foo'],'rval':[4,5]})
print(left)
print(right)
new = pd.merge(left,right,on='key')
print(new)

# 3.Append 将一行连接到一个DataFrame上
df = pd.DataFrame(np.random.randn(8,4),columns=['A','B','C','D'])
print(df)
s = df.iloc[3]
df11 = df.append(s,ignore_index=True)
print(df11)
