
﻿from flask import Flask, jsonify, request

from collections import OrderedDict

app = Flask(__name__)


@app.route('/api/policeaffairs/search', methods=['GET','POST'])
def search():
    informations = request.json['informations']
    topN = request.json["topN"]

    res = {
        "code": 0,
        "message": "",
        "data": {},
    }

    try:
        datas = []
        for index in informations:
            id = index["id"]
            lines = index["lines"]
            # if len(lines) < 9 :
            #     res['code'] =10000
            #     res['message']='lines count should be more than 9'
            data = OrderedDict([('id', id),
                                ('address', OrderedDict([('001', 0.9103), ('002', 0.7305), ('003', 0.7246), ('004', 0.6537), ('005', 0.6426)])),
                                ('type1', {"001": 0.9999}),
                                ('type2', OrderedDict([('002', 0.9999), ('003', 0.0), ('004', 0.0), ('005', 0.0), ('006', 0.0)])),
                                ('type3', OrderedDict([('007', 1.9509), ('008', 0.6186), ('009', 0.5807)])),
                                ('type3', OrderedDict([('', "")])),
                                ('type4', OrderedDict([('', "")]))])


            datas.append(data)
        res["data"] = datas
    except Exception as e:
        res['code'] = 10000
        res['message'] = e
        return jsonify(res)
    finally:
        return jsonify(res)

    return jsonify(res)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)


