import pandas as pd

file1 = './files/data1.xlsx'
file2 = './files/data2.xlsx'

file = [file1,file2]
li = []
for i in file:
    li.append(pd.read_excel(i))

writer = pd.ExcelWriter('./files/merge.xlsx')
pd.concat(li).to_excel(writer,'Sheet1',index=False)

writer.save()
