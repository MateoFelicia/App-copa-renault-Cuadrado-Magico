from flask import render_template, Blueprint
from database import get_db

sponsors_bp = Blueprint('sponsors',__name__)

@sponsors_bp.route("/sponsors", methods=["GET"]) # get, delete, upgrade
def sponsor():
    db = get_db()
    datos = db.execute("SELECT * FROM sponsors").fetchall()
    return render_template("sponsors.html", sponsors=datos)