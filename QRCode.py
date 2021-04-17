import pyqrcode
from pyqrcode import QRCode

code = "https://www.github.com"

url = pyqrcode.create(code)

url.svg("githubqrcode.svg", scale = 8)
