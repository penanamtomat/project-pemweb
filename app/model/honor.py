from app import db
from app.model.guru import Guru

class Honor(db.Model):
    id_honor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    no_guru = db.Column(db.String(5), db.ForeignKey(Guru.nog))
    jumlah_honor = db.Column(db.String(10), nullable=False)
    tgl_honor = db.Column(db.Date, nullable=False)
    nominal_honor = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return 'Honor {}>'.format(self.no_guru)