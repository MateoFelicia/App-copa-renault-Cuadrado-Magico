from flask import Flask, render_template, request
import sqlite3

from flask import redirect, url_for

app = Flask(__name__)

@app.route("/usuarios", methods=["GET"])
def usuarios():
    

    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    cursor.execute(f"SELECT * FROM usuarios")
    datos = cursor.fetchall()

    conexion.close()

    return render_template("usuarios.html", usuarios=datos)