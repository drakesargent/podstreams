from flask import (Blueprint, request, render_template, flash, redirect,
                   url_for, jsonify)

rue = Blueprint('core',__name__)

@rue.route('/')
@rue.route('/index.html')
def index():
    print("accessed root")
    return "<h1>Hello World</h1>"

@rue.route('/a/')
def auth():
    print("authorized")
    return "<h1>Authorized</h1>"

@rue.route('/a/add/')
def add():
    print("add")
    return "<h1>Add Form</h1>"

@rue.route('/a/update/')
def update():
    print("update")
    return "<h1>Update</h1>"

@rue.route('/a/delete/')
def delete():
    print("delete")
    return "<h1>Delete</h1>"