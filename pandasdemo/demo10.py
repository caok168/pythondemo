# Categorical
# pandas可以在DataFrame中支持Categorical类型的数据

import pandas as pd
import numpy as np

df = pd.DataFrame({"id":[1,2,3,4,5,6],"raw_grade":['a','b','b','a','a','e']})
print(df)

# 1. 将原始的grade转换为Categorical数据类型
df["grade"] = df["raw_grade"].astype("category")
print(df["grade"])
print('========================================')

# 2. 将Categorical类型数据重命名为更有意义的名称
df["grade"].cat.categories = ['very good','good','very bad']
print(df)
print('========================================')

# 3. 对类别进行重新排序，增加缺失的类别
df["grade"] = df["grade"].cat.set_categories(["very bad","bad","medium","goo"])
print(df["grade"])
print('========================================')

# 4. 排序是按照Categorical的顺序进行的而不是按照字典顺序进行
# print(df.sort("grade"))
# print('========================================')

# 5. 对Categorical列进行排序时存在空的类别
print(df.groupby("grade").size())