from app.model.santri import Santri
from app import response, app, db
from flask import request
import uuid
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def daftarSantri():
    try:
        # nama_santri = request.form['nama']
        # tmpt_lahir_santri = request.form['ttl']
        # tgl_lahir_santri = request.form['tgl']
        # nama_ayah = request.form['dadname']
        # pekerjaan_ayah = request.form['dadkerja']
        # nama_ibu = request.form['momname']
        # pekerjaan_ibu = request.form['momwork']
        # jk_santri = request.form['jk']
        # alamat_santri = request.form['alamat']
        # jadwal = request.form['jadwal']
        # no_hp = request.form['nohp']
        # tahunan = request.form['tahunan']
        # spp = request.form['spp']
        # kartu_keluarga = request.files['kk']

        #menerima data dari request
        nama_santri = request.form.get('nama')
        tmpt_lahir_santri = request.form.get('ttl')
        tgl_lahir_santri = request.form.get('tgl')
        nama_ayah = request.form.get('dadname')
        pekerjaan_ayah = request.form.get('dadkerja')
        nama_ibu = request.form.get('momname')
        pekerjaan_ibu = request.form.get('momwork')
        jk_santri = request.form.get('jk')
        alamat_santri = request.form.get('alamat')
        jadwal = request.form.get('jadwal')
        no_hp = request.form.get('nohp')
        tahunan = request.form.get('tahunan')
        spp = request.form.get('spp')
        kartu_keluarga = request.files['kk']

        if kartu_keluarga and allowed_file(kartu_keluarga.filename):
            filename = secure_filename(kartu_keluarga.filename)
            kartu_keluarga.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            santri = Santri()
            santri.nama_santri = nama_santri
            santri.tmpt_lahir_santri = tmpt_lahir_santri
            santri.tgl_lahir_santri = tgl_lahir_santri
            santri.nama_ayah = nama_ayah
            santri.pekerjaan_ayah = pekerjaan_ayah
            santri.nama_ibu = nama_ibu
            santri.pekerjaan_ibu = pekerjaan_ibu
            santri.jk_santri = jk_santri
            santri.alamat_santri = alamat_santri
            santri.jadwal = jadwal
            santri.no_hp = no_hp
            santri.tahunan = tahunan
            santri.spp = spp
            santri.kartu_keluarga = 'app/static/uploads/' + filename

            db.session.add(santri)
            db.session.commit()

            return response.success('', 'Data santri berhasil ditambahkan')
        else:
            return response.failure([], 'Format kartu keluarga tidak sesuai')
    except Exception as e:
        print(e)