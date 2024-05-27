from app import app
# from app.controller import calonSantri
from flask import render_template

@app.route('/')
def index():
    return render_template('landingpage.html')
    # return 'Hello TPQ' 

# app.route('/pendaftaran', methods=['GET'])
# def calonPendaftar():
#     return calonSantri.index()

if __name__ == "__main__":
    app.run(debug=True, port=5002)