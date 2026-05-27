from flask import Blueprint, render_template
from database import get_db

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route("/usuarios", methods=["GET"])
def usuarios():
    db = get_db()
    datos = []
    for doc in db.collection("usuarios").stream():
        usuario = doc.to_dict()
        usuario['id'] = doc.id
        datos.append(usuario)
    return render_template("usuarios.html", usuarios=datos)