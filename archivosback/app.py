from flask import Flask, render_template, request
import sqlite3

from flask import redirect, url_for

app = Flask(__name__)

# Ruta principal
@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)