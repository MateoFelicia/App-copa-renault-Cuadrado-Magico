from flask import Blueprint, render_template, request, redirect, url_for
from database import get_db

registro_bp = Blueprint('registros', __name__)

@registro_bp.route("/registros", methods=["POST"])
def registro():
    nombre = request.form["nombre"]
    email = request.form["email"]
    password = request.form["password"]

    db = get_db()
    db.collection("usuarios").add({
        "nombre": nombre,
        "email": email,
        "password": password
    })

    return redirect(url_for("usuarios.usuarios"))