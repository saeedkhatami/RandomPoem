import requests as req

resp = req.request(method='GET', url="https://ganjgah.ir/api/ganjoor/poem/random")
json_respond = resp.json()
html_respond = json_respond['htmlText']
plain_text_respond = json_respond['plainText']
verses = json_respond['verses']

for i in verses:
    print(i['text'])

print(json_respond)
print(json_respond['fullTitle'])
print(type(plain_text_respond))