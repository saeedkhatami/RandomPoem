import requests as req
from urllib.parse import urlencode
from urllib.request import urlretrieve

resp = req.request(method='GET', url="https://ganjgah.ir/api/ganjoor/poem/random")
print(resp)
json_respond = resp.json()
html_respond = json_respond['htmlText']
plain_text_respond = json_respond['plainText']

params = urlencode(dict(access_key="48a1a46259524cd0bb49cc15a907358a",
                        url="https://random-poem.iran.liara.run",
                        width=750))
urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, "screenshots/screenshot.jpeg")
