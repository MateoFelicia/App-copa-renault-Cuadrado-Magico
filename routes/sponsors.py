from flask import Blueprint, render_template
from database import get_db

sponsors_bp = Blueprint('sponsors', __name__)

# Esta ruta no tiene template propio; los sponsors se muestran en inicio.
# La dejamos por si se quiere una página dedicada en el futuro.
@sponsors_bp.route("/sponsors", methods=["GET"])
def sponsors():
    db = get_db()
    datos = []
    for doc in db.collection("sponsors").stream():
        s = doc.to_dict()
        s['id'] = doc.id
        datos.append(s)
    return render_template("inicio.html", sponsors=datos, noticias=[])