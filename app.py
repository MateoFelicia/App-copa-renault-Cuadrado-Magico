from flask import Flask, render_template

app = Flask(__name__)

# Página principal
@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/partidos")   
def partidos():
    return render_template("partidos.html")

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


if __name__ == "__main__":
    app.run(debug=True, port=5001)