import sqlite3
from flask import g, current_app

def get_db():
    # g es un objeto especial de Flask que dura exactamente un request
    if 'db' not in g:
        g.db = sqlite3.connect(
            "database.db",
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row  # permite acceder columnas por nombre
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)  # cierra la conexión al final de cada request