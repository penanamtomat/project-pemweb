from app import db

class Honor(db.Model):
    id_honor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tgl_pembayaran = db.Column(db.Date, nullable=False)
    honor_kehadiran = db.Column(db.Integer, nullable=False)
    jumlah_kehadiran = db.Column(db.Integer, nullable=False)
    total_honor = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Honor {}>'.format(self.tgl_pembayaran)