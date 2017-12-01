from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'emailvaliddb')

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route('/')
def index():
    return "hit index route"
    # data?
    # render
@app.route('/registeration', methods=["POST"])
def registeration():
    return "hit registration route"
    # handle data
    # go to database
    # redirect 
@app.route('/invalid')
def invalid():
    return "hit invalid route"
    # handle data
    # go to database
    # redirect 
@app.route('/success')
def success():
    return "hit success route"

app.run(debug=True)
