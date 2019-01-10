from flask import (Blueprint, request, render_template, flash, redirect,
                   url_for, jsonify)

rue = Blueprint('core',__name__)

@rue.route('/')
@rue.route('/index.html')
def index():
    print("accessed root")
    return "<h1>Hello World</h1>"
