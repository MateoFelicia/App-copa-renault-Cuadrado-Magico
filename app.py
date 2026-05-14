from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route("/")
def inicio():
    return render_template("inicio.html")


# Fixture y partidos
@app.route("/fixture_y_partidos")
def fixture_y_partidos():
    return render_template("fixture_y_partidos.html")


# Mapa
@app.route("/mapa")
def mapa():
    return render_template("mapa.html")


# Noticias
@app.route("/noticias")
def noticias():
    return render_template("noticias.html")


# Más
@app.route("/mas")
def mas():
    return render_template("mas.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)