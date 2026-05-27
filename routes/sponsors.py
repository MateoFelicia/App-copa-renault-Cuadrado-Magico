from flask import render_template, Blueprint
from database import get_db

sponsors_bp = Blueprint('sponsors', __name__)

@sponsors_bp.route("/sponsors", methods=["GET"])
def sponsor():
    db = get_db()
    datos = []
    for doc in db.collection("sponsors").stream():
        sponsor = doc.to_dict()
        sponsor['id'] = doc.id
        datos.append(sponsor)
    return render_template("sponsors.html", sponsors=datos)