from app import db

class Santri(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no_daftar = db.Column(db.String(10), nullable=False)
    no_santri = db.Column(db.String(10))
    nama_santri = db.Column(db.String(50), nullable=False)
    tmpt_lahir_santri = db.Column(db.String(20), nullable=False)
    tgl_lahir_santri = db.Column(db.Date, nullable=False)
    nama_ayah = db.Column(db.String(50), nullable=False)
    pekerjaan_ayah = db.Column(db.String(20), nullable=False)
    nama_ibu = db.Column(db.String(50), nullable=False)
    pekerjaan_ibu = db.Column(db.String(20), nullable=False)
    jk_santri = db.Column(db.String(10), nullable=False)
    alamat_santri = db.Column(db.String(100), nullable=False)
    jadwal = db.Column(db.String(10), nullable=False)
    no_hp = db.Column(db.String(15), nullable=False)
    tahunan = db.Column(db.String(10), nullable=False)
    spp = db.Column(db.String(10), nullable=False)
    kartu_keluarga = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Santri {}>'.format(self.nama_santri)