from flask import Blueprint, render_template

cantina_bp = Blueprint('cantina', __name__)

@cantina_bp.route("/cantina", methods=["GET"])
def cantina():
    return render_template("cantina.html")