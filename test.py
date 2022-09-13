import requests as req
resp = req.request(method='GET', url="https://ganjgah.ir/api/ganjoor/poem/random")
print(resp)
json_respond = resp.json()
html_respond = json_respond['htmlText']
plain_text_respond = json_respond['plainText']