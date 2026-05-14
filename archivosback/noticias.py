from flask import Flask, render_template, request
import sqlite3

from flask import redirect, url_for

app = Flask(__name__)

@app.route("/noticias", methods=["GET"]) # get, delete, upgrade
def noticias():
    import sqlite3

    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM noticias")
    datos = cursor.fetchall()

    conexion.close()

    return render_template("noticias.html", noticias=datos)