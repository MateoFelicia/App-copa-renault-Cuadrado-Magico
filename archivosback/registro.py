from flask import Flask, render_template, request
import sqlite3

from flask import redirect, url_for

app = Flask(__name__)

@app.route("/registro", methods=["POST"])
def registro():
    nombre = request.form["nombre"]
    email = request.form["email"]
    password = request.form["password"]

    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)",
        (nombre, email, password)
    )

    conexion.commit()
    conexion.close()


    from flask import redirect, url_for

    return redirect(url_for("usuarios"))