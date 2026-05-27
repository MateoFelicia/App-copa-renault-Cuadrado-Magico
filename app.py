import database
from flask import Flask

app = Flask(__name__)
database.init_app(app)

from routes.inicio import inicio_bp
from routes.noticias import noticias_bp
from routes.cantina import cantina_bp
from routes.croquis import croquis_bp
from routes.sponsors import sponsors_bp
from routes.usuarios import usuarios_bp
from routes.registros import registro_bp
from routes.partidos import partidos_bp

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