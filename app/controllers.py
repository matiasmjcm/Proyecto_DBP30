from flask import Flask, request, render_template, redirect, url_for
from configuration import app, db
from models import *

@app.route("/")
def home():
    return render_template('home.html')
