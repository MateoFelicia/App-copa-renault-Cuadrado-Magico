from flask import Blueprint, render_template
from database import get_db

inicio_bp = Blueprint('inicio', __name__)

@inicio_bp.route("/", methods=["GET"])
def inicio():
    db = get_db()

    # Sponsors
    sponsors = []
    for doc in db.collection("sponsors").stream():
        s = doc.to_dict()
        s['id'] = doc.id
        sponsors.append(s)

    # Últimas 2 noticias
    noticias = []
    for doc in db.collection("noticias").order_by("fecha", direction="DESCENDING").limit(2).stream():
        n = doc.to_dict()
        n['id'] = doc.id
        noticias.append(n)

    return render_template("inicio.html", noticias=noticias, sponsors=sponsors)