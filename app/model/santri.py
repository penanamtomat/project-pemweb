from app import db
from app.model.calon_santri import daftarCalonSantri

def generate_nos():
    last_number = 0
    prefix = "STRI-"
    last_number += 1
    return prefix + str(last_number)

class Santri(db.Model):
    __tablename__ = "santri"
    id_santri = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no_santri = db.Column(db.String(5), unique=True, default=generate_nos())
    nama_santri = db.Column(db.String(50))
    tmpt_lahir_santri = db.Column(db.String(20))
    tgl_lahir_santri = db.Column(db.Date, nullable=False)
    jns_klmn_santri = db.Column(db.String(10))
    alamat = db.Column(db.String(100))
    no_hp_santri = db.Column(db.String(50))
    id_calon_santri = db.Column(db.Integer, db.ForeignKey(daftarCalonSantri.id))

    def __repr__(self):
        return '<Santri {}>'.format(self.nama_santri)

    def create_tables(): db.create_all()
    if __name__=="main": create_tables()