import os
import requests as req
from flask import Flask, render_template, send_file
from html2image import Html2Image

photos_folder = os.path.join('static', 'photos')
print(photos_folder)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = photos_folder


@app.route('/', methods=['GET', 'POST'])
def main():
    resp = req.request(method='GET', url="https://ganjgah.ir/api/ganjoor/poem/random?poetId=39024")
    json_respond = resp.json()
    html_respond = json_respond['htmlText']
    plain_text_respond = json_respond['plainText']
    new_plain_text = plain_text_respond.replace('\n', '<br>')
    poem_info = json_respond['fullTitle']

    return render_template('index.html', info=poem_info, poem=new_plain_text)


def take_photo():
    hti = Html2Image(output_path=photos_folder)
    hti.screenshot(
        url='http://127.0.0.1:5000/',
        save_as='preview.png',
        size=(500, 650)
    )


@app.route('/photos')
def show_image():
    take_photo()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'preview.png')
    return send_file(full_filename, mimetype='image/png')
