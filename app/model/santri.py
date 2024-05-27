from app import db
import string

def generate_nos():
    # digits = string.digits
    prefix = "STRI-"
    current_id = Santri.query.order_by(Santri.id.desc()).first()
    if current_id:
        current_id = int(current_id.nos.replace(prefix, "")) + 1
    else:
        current_id = 1
    random_digits = str(current_id).zfill(3)
    return prefix + random_digits

class Santri(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nos = db.Column(db.String(5), unique=True, default=generate_nos())
    nama = db.Column(db.String(50))
    ttl = db.Column(db.String(50))
    alamat = db.Column(db.String(200))
    no_hp = db.Column(db.String(50))
    email = db.Column(db.String(50))
    username = db.Column(db.String(10))
    password = db.Column(db.String(10))
    id_pendaftaran = db.Column(db.String(10))

    def __repr__(self):
        return '<Santri {}>'.format(self.nama)