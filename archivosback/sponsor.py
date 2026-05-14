from flask import Flask, render_template, request
import sqlite3

from flask import redirect, url_for

app = Flask(__name__)

@app.route("/sponsors", methods=["GET"]) # get, delete, upgrade
def sponsor():
    import sqlite3

    conexion = sqlite3.connect("database.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM sponsors")
    datos = cursor.fetchall()

    conexion.close()

    return render_template("sponsors.html", sponsor=datos)