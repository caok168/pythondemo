import pandas as pd

def readExcelByPandas(excelFile):
    df = pd.read_excel(excelFile,sheet_name=1)

    nrows = df.shape[0]
    ncols = df.columns.size
    print('Max Rows:'+str(nrows))
    print('Max Columns:'+str(ncols))
    # 遍历全部内容
    list = []
    for iRow in range(nrows):
        if iRow > 0:
            date1 = pd.to_datetime(df.iloc[iRow,1])
            a = {
                "name": df.iloc[iRow,0],
                "time": date1,
                "state": df.iloc[iRow,2],
                "camera": df.iloc[iRow,3],
            }

            b =(
                df.iloc[iRow, 0],
                date1,
                df.iloc[iRow, 2],
                df.iloc[iRow, 3],
            )

            list.append(a)

    l = sorted(list, key=lambda x:(x['name'], x['time']))

    for i in l:
        print(i)

if __name__ == "__main__":
    readExcelByPandas("./files/demo.xlsx")
