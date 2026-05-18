from flask import Flask, render_template, request
import sqlite3

from flask import redirect, url_for

app = Flask(__name__)

@app.route("/noticias", methods=["GET"]) # get, delete, upgrade
def noticias():

    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    cursor.execute(f"SELECT * FROM noticias")
    datos = cursor.fetchall()

    conexion.close()

    return render_template("noticias.html", noticias=datos)