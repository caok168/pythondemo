# Reshaping
import pandas as pd
import numpy as np

# 1. Stack
tuples = list(zip(*[['bar','bar','baz','baz','foo','foo','qux','qux'],
                    ['one','two','one','two','one','two','one','two']]))
index = pd.MultiIndex.from_tuples(tuples,names=['first','second'])
df = pd.DataFrame(np.random.randn(8,2),index=index,columns=['A','B'])
print(df)
df2 = df[:4]
print(df2)
print("===========================")

stacked = df2.stack()
print(stacked)
print("===========================")

print(stacked.unstack())
print(stacked.unstack(1))
