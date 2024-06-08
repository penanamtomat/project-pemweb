from app import app, response
from flask import render_template, redirect, url_for, request, session
from datetime import timedelta
from app.controller import userController
from app.controller import santriController
# from app.model import user_level
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

# app.secret_key = "hello"
# app.permanent_session_lifetime = timedelta(minutes=1)

@app.route('/')
def landingpage():
    return render_template('landingpage.html')

@app.route('/pendaftaran')
def pendaftaran():
    # return santriController.daftarSantri()
    return render_template('pendaftaran.html')

@app.route('/pendaftaran/save', methods=['POST'])
def pendaftaran_save():
    return santriController.daftarSantri()
    # if request.method == 'GET':
    #     return render_template('pendaftaran.html')
    # else:
    #     return santriController.daftarSantri()

@app.route('/antrian')
def antrian():
    return render_template('antrian.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         session.permanent = True
#         username = request.form['username']
#         password = request.form['password']
#         session["user"] = username, password
#         return redirect(url_for('dashboard'))
#     else:
#         if "user" in session:
#             return redirect(url_for('user'))
        
#         return render_template('login.html')

# @app.route('/login', methods=['POST'])
# def account():
#     return userController.buatAkun()

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        pengguna = userController.login()
        if pengguna:
            aktor = pengguna.get('id_level_user')
            if aktor == '1':
                return redirect('/dashboard')
            elif aktor == '2':
                return redirect('/dashboardGuru')
            else:
                return
    else:
        return render_template('login.html')
        # return userController.login()
    # return render_template('login.html')

@app.route('/aman', methods=['GET'])
@jwt_required()
def aman():
    curr_user = get_jwt_identity()
    return response.success(curr_user, "sukses aman")

@app.route('/dashboard')
def dashboard():
    # if "user" in session:
    #     user = session["user"]
    return render_template('dashboard.html')
    # else:
    #     return redirect(url_for('login'))

# @app.route("/logout")
# def logout():
#     session.pop("user", None)
#     return redirect(url_for('login'))

