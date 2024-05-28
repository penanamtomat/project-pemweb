from app import db
from app.model.santri import Santri

class spp(db.Model):
    id_spp = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bayar_daftar = db.Column(db.String(10), nullable=False)
    bayar_tahun = db.Column(db.String(10), nullable=False)
    bayar_bulan = db.Column(db.String(10), nullable=False)
    id_santri = db.Column(db.Integer, db.ForeignKey(Santri.id_santri))

    def __repr__(self):
        return '<spp {}>'.format(self.id_spp)