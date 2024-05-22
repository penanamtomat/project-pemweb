from app import db
import string

def generate_id():
    digits = string.digits
    prefix = "DFT-"
    random_digits = "".join([digits[0] for _ in range(4)])
    return prefix + random_digits

class Pendaftaran(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_pendaftar = db.Column(db.String(10), unique=True, default=generate_id)
    nama = db.Column(db.String(50))
    ttl = db.Column(db.String(50))
    ayah = db.Column(db.String(50))
    job_ayah = db.Column(db.String(50))
    ibu = db.Column(db.String(50))
    job_ibu = db.Column(db.String(50))
    jenis_kelamin = db.Column(db.String(50))
    jadwal = db.Column(db.String(50))
    no_hp = db.Column(db.String(50))
    alamat = db.Column(db.String(200))
    tahunan = db.Column(db.String(50))
    spp = db.Column(db.String(50))
    kartu_keluarga = db.Column(db.String(50))

    def __repr__(self):
        return '<Pendaftaran {}>'.format(self.nama)