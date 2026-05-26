from flask import Blueprint, render_template, request, redirect, url_for
from database import get_db

registro_bp = Blueprint('registros',__name__)

@registro_bp.route("/registros", methods=["POST"]) # get, delete, upgrade
def registro():
    nombre = request.form["nombre"]
    email = request.form["email"]
    password = request.form["password"]

    db = get_db()
    db.execute(
        "INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)",
        (nombre, email, password)
    )
    db.commit()

    return redirect(url_for("usuarios.usuarios"))