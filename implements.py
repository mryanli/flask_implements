#!/usr/bin/python
# -*- coding:UTF-8 -*-

from   datetime import datetime

from flask import Flask,current_app,Response,make_response,redirect,abort,\
    render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from    flask_wtf import Form
from wtforms import StringField,SelectField





app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)



@app.route('/index')
def index():
    return render_template('index.html',current_time = datetime.utcnow())


@app.route('/user/<path:name>')
def user(name):
    print(name)
    return render_template("user.html",name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.app_context()
    manager.run()