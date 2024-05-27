from app import db
import string

def generate_id():
    digits = string.digits
    prefix = "DFT-"
    random_digits = "".join([digits[0] for _ in range(4)])
    return prefix + random_digits

class Pendaftaran(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_pendaftar = db.Column(db.String(10), nullable=False, unique=True, default=generate_id)
    nama = db.Column(db.String(50), nullable=False)
    tmpt_lahir = db.Column(db.String(20), nullable=False)
    tgl_lahir = db.Column(db.Date, nullable=False)
    ayah = db.Column(db.String(50), nullable=False)
    job_ayah = db.Column(db.String(20), nullable=False)
    ibu = db.Column(db.String(50), nullable=False)
    job_ibu = db.Column(db.String(20), nullable=False)
    jenis_kelamin = db.Column(db.String(10), nullable=False)
    jadwal = db.Column(db.String(10), nullable=False)
    no_hp = db.Column(db.String(15), nullable=False)
    alamat = db.Column(db.String(100), nullable=False)
    tahunan = db.Column(db.String(10), nullable=False)
    spp = db.Column(db.String(10), nullable=False)
    kartu_keluarga = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Pendaftaran {}>'.format(self.nama) 