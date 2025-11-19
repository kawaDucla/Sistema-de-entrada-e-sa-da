from flask import render_template, redirect, url_for, request
from app import app, db
from app.model import User, Livro

@app.route('/')
def homepage():
    return render_template('index.html')