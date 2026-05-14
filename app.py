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
    sponsors = [
        "https://cdn.iconscout.com/icon/free/png-256/free-coca-cola-logo-icon-svg-download-png-1579762.png",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS8il-Fph_iLce9tKXGbAh978ujKjX1ivZvZg&s",
        "https://upload.wikimedia.org/wikipedia/commons/b/b9/Sprite_Logo.svg"
    ] # Obtener desde la Base de Datos las imagenes de los sponsor
    noticias = [
        {
            "id": 1,
            "titulo": "Resultados de la jornada 2",
            "descripcion": "Repasá todos los goles, posiciones y figuras destacadas del fin de semana.",
            "fecha": "12 Jun 2025",
            "imagen": "https://example.com/foto1.jpg"
        },
        {
            "id": 2,
            "titulo": "Convocatoria para la jornada 3",
            "descripcion": "Ya están confirmados los horarios y canchas para el próximo fin de semana.",
            "fecha": "10 Jun 2025",
            "imagen": "https://example.com/foto2.jpg"
        },
    ] # Obtener desde la Base de Datos las noticias ordenadas desde la mas reciente a la mas antigua
    return render_template("inicio.html", noticias=noticias, sponsors=sponsors)

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

@app.route("/cantina")
def cantina():
    return render_template("cantina.html")

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