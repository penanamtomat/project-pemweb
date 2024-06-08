from app.model.user import User
from app import response, app, db
from flask import request
from flask_jwt_extended import *
from datetime import timedelta

def buatAkun():
    try:
        username = request.form['username']
        password = request.form['password']
        # id_user_level = 1

        users = User(username=username, password=password)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success('', "Akun berhasil dibuat")
    except Exception as e:
        print(e)

def tampilAkun(data):
    data = {
        'id_user': data.id_user,
        'nama_user': data.nama_user,
        'username': data.username,
        # 'password': data.password,
        'id_level_user': data.id_level_user
    }

    return data

def login():
    try:
        username = request.form.get('username')
        password = request.form.get('password')

        users = User.query.filter_by(username=username).first()

        if not users:
           return response.failure([], "Invalid username")
        
        if not users.checkPassword(password):
            return response.failure([], "Invalid password")

        data = tampilAkun(users)
        expires_session = timedelta(minutes=1)
        expires_refresh = timedelta(minutes=1)

        accessToken = create_access_token(data, fresh=True, expires_delta=expires_session)
        refreshToken = create_refresh_token(data, expires_delta=expires_refresh)

        return response.success({
            'data': data,
            'accessToken': accessToken,
            'refreshToken': refreshToken
        }, "Sukses Login")
    except Exception as e:
        print(e)