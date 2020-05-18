import urllib.request as urllib2
import json

api = "http://127.0.0.1:5000/api/policeaffairs/search"
request = urllib2.Request(api)

data = {
    "information": [
        {
            "id": "1111",
            "lines": ["", ""]
        }
    ],
    "topN": 5
}
headers = {"Content-Type": "application/json"}

req = urllib2.Request(url= api, headers=headers, data= json.dumps(data).encode('utf-8'))
print(req)

res_data = urllib2.urlopen(req)
res = res_data.read().decode('utf-8')
print(res)
