import requests as req
from flask import Flask, render_template, send_file

app = Flask(__name__)


@app.route('/', methods=['GET'])
def random():
    resp = req.request(method='GET', url="https://ganjgah.ir/api/ganjoor/poem/random")
    json_respond = resp.json()
    plain_text_respond = json_respond['plainText']
    new_plain_text = plain_text_respond.replace('\n', '<br>')
    poem_info = json_respond['fullTitle']

    return render_template('index.html', title= "شعر تصادفی", info=poem_info, poem=new_plain_text)


@app.route('/faal', methods=['GET'])
def faal():
    resp = req.request(method='GET', url="https://ganjgah.ir/api/ganjoor/hafez/faal")
    json_respond = resp.json()
    plain_text_respond = json_respond['plainText']
    new_plain_text = plain_text_respond.replace('\n', '<br>')
    poem_info = json_respond['fullTitle']

    return render_template('index.html', title= "فال حافظ", info=poem_info, poem=new_plain_text)

