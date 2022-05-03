# -*- encoding: utf-8 -*-
"""
@File : app.py
@Time : 2022/5/3 22:20
@Author : Linleil
"""


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to My Watchlist'
