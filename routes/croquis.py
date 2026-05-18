from flask import Flask, render_template, request
import sqlite3

from flask import redirect, url_for

app = Flask(__name__)

@app.route("/croquis", methods=["GET"])
def croquis():
    return render_template("croquis.html")