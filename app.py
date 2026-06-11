import database
from flask import Flask
import firebase_admin
from firebase_admin import credentials, auth

app = Flask(__name__)
app.secret_key = "cuadradomagicoamaDios"
database.init_app(app)

cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)

from routes.inicio import inicio_bp
from routes.noticias import noticias_bp
from routes.cantina import cantina_bp
from routes.croquis import croquis_bp
from routes.sponsors import sponsors_bp
from routes.usuarios import usuarios_bp
from routes.registros import registro_bp
from routes.partidos import partidos_bp
from routes.admin import admin_bp
<<<<<<< HEAD
from routes.admin_login import login_bp
=======
from routes.auth import auth_bp
>>>>>>> 951f1c87a68f56aa5ecbc3b8530a23a1978b0eb7

app.register_blueprint(admin_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(inicio_bp)
app.register_blueprint(noticias_bp)
app.register_blueprint(cantina_bp)
app.register_blueprint(croquis_bp)
app.register_blueprint(sponsors_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(registro_bp)
app.register_blueprint(partidos_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5001)