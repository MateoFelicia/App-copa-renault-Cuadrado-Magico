from flask import Blueprint, render_template

croquis_bp = Blueprint('croquis', __name__)

@croquis_bp.route("/mapa", methods=["GET"])
def mapa():
    return render_template("mapa.html")