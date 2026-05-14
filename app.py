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

@app.route("/partidos", defaults={"categoria": "Todas", "deporte": "Todos", "genero": "Todos"})
@app.route("/partidos/<categoria>/<deporte>/<genero>")
def partidos(categoria, deporte, genero):

    todos = [
    {
        "hora": "16:30",
        "equipo_local": "Renault B",
        "equipo_visitante": "San Martín",
        "categoria": "Menor",
        "genero": "Masculino",
        "deporte": "Fútbol",
        "estado": "live",
        "goles_local": 2,
        "goles_visitante": 1
    },

    {
        "hora": "18:00",
        "equipo_local": "Renault A",
        "equipo_visitante": "Godoy Cruz",
        "categoria": "Mayor",
        "genero": "Femenino",
        "deporte": "Fútbol",
        "estado": "prox"
    },

    {
        "hora": "19:00",
        "equipo_local": "Renault C",
        "equipo_visitante": "Huracán",
        "categoria": "Menor",
        "genero": "Mixto",
        "deporte": "Básquet",
        "estado": "terminado",
        "goles_local": 88,
        "goles_visitante": 74
    },
]

    filtrados = []

    for p in todos:
        if (categoria == "Todas" or p["categoria"] == categoria):
            if (deporte == "Todos" or p["deporte"] == deporte):
                if (genero == "Todos" or p["genero"] == genero):
                    filtrados.append(p)

    return render_template(
        "partidos.html",
        partidos=filtrados,
        categoria_activa=categoria,
        deporte_activo=deporte,
        genero_activo=genero
    )

@app.route("/fixture")
def fixture():
    return render_template("fixture.html")

@app.route("/mapa")
def mapa():
    return render_template("mapa.html")

@app.route("/noticias")
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