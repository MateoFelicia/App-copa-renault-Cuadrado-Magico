from flask import Blueprint, render_template
from database import get_db

usuarios_bp = Blueprint('usuarios',__name__)

@usuarios_bp.route("/usuarios", methods=["GET"])
def usuarios():
    db = get_db()
    datos = db.execute("SELECT * FROM usuarios").fetchall()
    return render_template("usuarios.html", usuarios=datos)