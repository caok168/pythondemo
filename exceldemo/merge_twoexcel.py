
import pandas as pd

df1 = pd.read_excel('./files/excel-comp-data.xlsx')
df2 = pd.read_excel('./files/excel-comp-data.xlsx')

frames = [df1,df2]
result = pd.concat(frames)
print(result)

result.to_excel('./files/merge.xlsx',index=False)
