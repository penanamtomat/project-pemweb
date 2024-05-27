from app import app
from app.controller import calonSantriController
from flask import render_template

@app.route('/')
def index():
    return render_template('landingpage.html')

@app.route('/pendaftaran')
def calonPendaftar():
    return render_template('pendaftaran.html')

@app.route('/antrian')
def antrian():
    return render_template('antrian.html')

@app.route('/login')
def login():
    return render_template('login.html')