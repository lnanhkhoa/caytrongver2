# coding=utf-8
from apps import app
from flask import render_template

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/chart")
def chart_check():
    return render_template('line-stacked-area.html')

@app.route("/test")
def test():
    return render_template("test.html")