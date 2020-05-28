import urllib.request as urllib2
import json
import pandas as pd


def get_datas(filename):
    df = pd.read_excel(filename, 'Sheet1')

    nrows = df.shape[0]
    ncols = df.columns.size
    print('Max Rows:' + str(nrows))
    print('Max Columns:' + str(ncols))
    # 遍历全部内容
    list = []
    for iRow in range(nrows):
        if iRow >= 0:
            a = {
                "num": df.iloc[iRow, 0],
                "title": df.iloc[iRow, 4],
                "content": df.iloc[iRow, 5],
                "feedback": df.iloc[iRow, 6],
                "branch": df.iloc[iRow, 9]
            }

            list.append(a)
    return list


def requestApi(datas):
    api = "http://127.0.0.1:9999/api/policeaffairs/search"

    results = []
    result_keys = []
    result_values = []

    for i in range(0, len(datas)):
        num = datas[i]['num']
        print(type(num))
        title = datas[i]['title']
        content = datas[i]['content']
        feedback = datas[i]['feedback']
        branch = datas[i]['branch']
        data = {
            "informations": [
                {
                    "id": str(num),
                    "lines": [str(num), "", "", "", title, content, feedback, "", "", branch, "", ""]
                }
            ],
            "topN": 1
        }
        res = requestApi_single(api, data)
        res_dict = json.loads(res)
        print(res_dict)
        type2 = res_dict["data"][0]['type2']
        type2_key = list(type2.keys())[0]
        type2_value = list(type2.values())[0]
        type2_list = []
        type2_list.append(type2_key)
        type2_list.append(type2_value)
        results.append(type2_list)
        result_keys.append(str(type2_key))
        result_values.append(str(type2_value))
    return results, result_keys, result_values


def requestApi_single(api, data):
    headers = {"Content-Type": "application/json"}

    req = urllib2.Request(url=api, headers=headers, data=json.dumps(data).encode('utf-8'))
    print(req)

    res_data = urllib2.urlopen(req)
    res = res_data.read().decode('utf-8')
    return res


def save_result(filename, sheet_name, datas):
    df = pd.DataFrame(datas, columns=['type2', 'values'])
    df.to_excel(filename, sheet_name=sheet_name, index=None)


if __name__ == '__main__':
    filename = 'test.xls'
    datas = get_datas(filename)
    results, keys, values = requestApi(datas)
    print(results)
    # save_result('./results.xls', 'Sheet1', keys)
    # save_result('./results.xls', 'Sheet2', values)
    save_result('./results.xls', 'Sheet2', results)
