from flask import Flask, render_template, request
import database
from routes.noticias import noticias
from flask import redirect, url_for

app = Flask(__name__)
database.init_app(app)
# Ruta principal
@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)