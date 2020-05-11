import pandas as pd

def combine_excel(file_path1,file_path2,target_path):
    # 文件读入
    data1 = pd.read_excel(file_path1)
    data2 = pd.read_excel(file_path2)
    result = pd.ExcelWriter(target_path)

    data1.to_excel(result,sheet_name='sheetname1',index=False)
    data2.to_excel(result,sheet_name='sheetname2',index=False)
    newResult = pd.concat([data1,data2])
    newResult.to_excel(result,sheet_name='sheetname3',index=False)

    return result

if __name__=='__main__':
    result = combine_excel('./files/data1.xlsx','./files/data2.xlsx','./files/merge.xlsx')
    result.save()
