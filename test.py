import requests as req
from urllib.parse import urlencode
from urllib.request import urlretrieve

resp = req.request(method='GET', url="https://ganjgah.ir/api/ganjoor/hafez/faal")
json_respond = resp.json()
print(json_respond)
