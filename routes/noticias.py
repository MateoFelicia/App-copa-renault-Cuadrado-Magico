from flask import Blueprint, render_template
from database import get_db

noticias_bp = Blueprint('noticias', __name__)

@noticias_bp.route("/noticias", defaults={"id": ""}, methods=["GET"])
@noticias_bp.route("/noticias/<id>", methods=["GET"])
def noticias(id):
    db = get_db()
    datos = []
    for doc in db.collection("noticias").order_by("fecha", direction="DESCENDING").stream():
        n = doc.to_dict()
        n['id'] = doc.id
        datos.append(n)
    return render_template("noticias.html", noticias=datos, id=id)