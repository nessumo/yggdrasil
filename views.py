__author__ = 'nessumo'

from flask import render_template

from yggdrasil import app


@app.route('/')
def home():
    return render_template("page.html")
