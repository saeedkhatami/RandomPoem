import requests as req
from flask import Flask, render_template, send_file
from take_screenshot import take_ss

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    resp = req.request(method='GET', url="https://ganjgah.ir/api/ganjoor/poem/random?poetId=39024")
    json_respond = resp.json()
    html_respond = json_respond['htmlText']
    plain_text_respond = json_respond['plainText']
    new_plain_text = plain_text_respond.replace('\n', '<br>')
    poem_info = json_respond['fullTitle']

    return render_template('index.html', info=poem_info, poem=new_plain_text)


@app.route('/photos')
def show_image():
    take_ss()

    return send_file("screenshots/screenshot.jpeg", mimetype='image/jpeg')
