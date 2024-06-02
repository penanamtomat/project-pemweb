from app import app
from flask import render_template

@app.route('/')
def landingpage():
    return render_template('landingpage.html')

@app.route('/pendaftaran')
def pendaftaran():
    return render_template('pendaftaran.html')

@app.route('/login')
def login():
    return render_template('login.html')