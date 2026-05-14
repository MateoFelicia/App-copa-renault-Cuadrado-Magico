from flask import Flask, render_template, request
import sqlite3

from flask import redirect, url_for

app = Flask(__name__)

# # Ruta principal
# @app.route("/")
# def inicio():
#     return render_template("index.html")

@app.route("/")
def inicio_():
    return render_template("inicio.html")
@app.route("/fixture_y_partidos")
def fixture_y_partidos():
    return render_template("fixture_y_partidos.html")
@app.route("/")
def mapa():
    return render_template("mapa.html")
@app.route("/")
def noticias():
    return render_template("noticias.html")
@app.route("/mas")
def mas():
    return render_template("mas.html")

# @app.route("/registro", methods=["POST"])
# def registro():
#     nombre = request.form["nombre"]
#     email = request.form["email"]
#     password = request.form["password"]

#     conexion = sqlite3.connect("database.db")
#     cursor = conexion.cursor()

#     cursor.execute(
#         "INSERT INTO usuarios (nombre, email, password) VALUES (?, ?, ?)",
#         (nombre, email, password)
#     )

#     conexion.commit()
#     conexion.close()

#     from flask import redirect, url_for

#     return redirect(url_for("usuarios"))

# @app.route("/usuarios")
# def usuarios():
#     import sqlite3

#     conexion = sqlite3.connect("database.db")
#     cursor = conexion.cursor()

#     cursor.execute("SELECT * FROM usuarios")
#     datos = cursor.fetchall()

#     conexion.close()

#     return render_template("usuarios.html", usuarios=datos)




if __name__ == "__main__":
    app.run(debug=True, port=5001)