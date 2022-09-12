import requests as req
from flask import Flask, render_template

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     resp = req.request(method='GET', url="https://ganjgah.ir/api/ganjoor/poem/random")
#     json_respond = resp.json()
#     print(resp.json())
#     print(json_respond['htmlText'])
#     html_respond = json_respond['htmlText']
#     return html_respond


@app.route('/')
def main():
    resp = req.request(method='GET', url="https://ganjgah.ir/api/ganjoor/poem/random?poetId=39024")
    json_respond = resp.json()
    html_respond = json_respond['htmlText']
    plain_text_respond = json_respond['plainText']
    new_plain_text = plain_text_respond.replace('\n', '<br>')
    poem_info = json_respond['fullTitle']
    return render_template('index.html', info=poem_info, poem=new_plain_text)
