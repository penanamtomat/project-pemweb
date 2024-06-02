from app import db
from app.model.guru import Guru

class Kehadiran(db.Model):
    id_kehadiran = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tgl_kehadiran = db.Column(db.Date, nullable=False)
    id_guru = db.Column(db.Integer, db.ForeignKey(Guru.id_guru))

    def __repr__(self):
        return '<Kehadiran {}>'.format(self.tgl_kehadiran)