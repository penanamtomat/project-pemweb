from app.model.pendaftaran import Pendaftaran
from app import response, app, db
from flask import request

def index():
    try:
        calonSantri = Pendaftaran.query.all()
        data = formatArray(calonSantri)
        return response.success(data, "success")
    except Exception as e:
        print(e)

def formatArray(datas):
    array = []

    for i in datas:
        array.append(tampilObject(i))
    
    return array

def tampilObject(data):
    data = {
        'id' : data.id,
        'id_pendaftar' : data.id_pendaftar,
        'nama' : data.nama,
        'tmpt_lahir' : data.tmpt_lahir,
        'tgl_lahir' : data.tgl_lahir,
        'ayah' : data.ayah,
        'job_ayah' : data.job_ayah,
        'ibu' : data.ibu,
        'job_ibu' : data.job_ibu,
        'jenis_kelamin' : data.jenis_kelamin,
        'jadwal' : data.jadwal,
        'no_hp' : data.no_hp,
        'alamat' : data.alamat,
        'tahunan' : data.tahunan,
        'spp' : data.spp,
        'kartu_keluarga' : data.kartu_keluarga
    }

    return data