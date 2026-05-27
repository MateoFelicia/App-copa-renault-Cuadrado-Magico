from flask import Blueprint, render_template
from database import get_db

noticias_bp = Blueprint('noticias', __name__)

@noticias_bp.route("/noticias", methods=["GET"])
def noticias():
    db = get_db()
    datos = []
    for doc in db.collection("noticias").stream():
        noticia = doc.to_dict()
        noticia['id'] = doc.id
        datos.append(noticia)
    return render_template("noticias.html", noticias=datos)