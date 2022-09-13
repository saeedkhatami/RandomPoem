from urllib.parse import urlencode
from urllib.request import urlretrieve
import os

full_file_name = os.path.join("screenshots", "screenshot.jpeg")


def take_ss():
    params = urlencode(dict(access_key="API_KEY",
                            url="URL",
                            width=750,
                            fresh=True))
    urlretrieve("https://api.apiflash.com/v1/urltoimage?" + params, full_file_name)
