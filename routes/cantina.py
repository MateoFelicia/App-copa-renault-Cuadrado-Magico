from flask import Flask, render_template, request
import sqlite3

from flask import redirect, url_for

app = Flask(__name__)

@app.route("/cantina", methods=["GET"])
def cantina():
    try:
        conexion = sqlite3.connect("database.db")
        cursor = conexion.cursor()
        
        cursor.execute(f"SELECT * FROM cantina")
        datos = cursor.fetchall()
        
        conexion.close()
        
        return render_template("cantina.html", cantina=datos)
        
    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
        return "Error al cargar los datos de la cantina", 500