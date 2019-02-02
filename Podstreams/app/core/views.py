from flask import (Blueprint, request, render_template, flash, redirect,
                   url_for, jsonify)

rue = Blueprint('core',__name__)

@rue.route('/')
@rue.route('/index.html')
def index():
    print("home")
    return render_template("home.html")

# Show CRUD Routes
@rue.route('/addShow/')
def addShow():
    print("add Show")
    return render_template("newShow.html")

@rue.route('/updateShow/')
def updateShow():
    print("update")
    return render_template("updateShow.html")

@rue.route('/deleteShow/')
def deleteShow():
    print("delete show")
    return render_template("deleteShow.html")

# Type CRUD Routes
@rue.route('/addType/')
def addType():
    print("add Type")
    return render_template("newType.html")

@rue.route('/updateType/')
def updateType():
    print("update Type")
    return render_template("updateType.html")

@rue.route('/deleteType/')
def deleteType():
    print("delete Type")
    return render_template("deleteType.html")