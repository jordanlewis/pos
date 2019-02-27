#!/usr/bin/env python3

from flask import Flask
from flask import request
from escpos.printer import Usb

app = Flask(__name__)

p = Usb(0x04b8, 0x0e15, 0)

@app.route("/", methods=['GET', 'POST'])
def receipt():
    if request.method == 'GET':
        return """<html>
Type some stuff into this box and press enter
<form>
<textarea name="data"></textarea>
<input type="submit"/>
</form>
</html>"""

    text = request.form['data']
    p.text(text)
    p.cut()
    return "printed " + text
