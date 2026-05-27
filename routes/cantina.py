from flask import Blueprint, render_template
from database import get_db

cantina_bp = Blueprint('cantina', __name__)

@cantina_bp.route("/cantina", methods=["GET"])
def cantina():
    db = get_db()

    # Traemos categorías ordenadas
    categorias = []
    for doc in db.collection("categorias_cantina").order_by("orden").stream():
        cat = doc.to_dict()
        cat['id'] = doc.id

        # Productos de cada categoría
        cat['productos'] = []
        for pdoc in db.collection("categorias_cantina").document(doc.id).collection("productos").stream():
            p = pdoc.to_dict()
            p['id'] = pdoc.id
            cat['productos'].append(p)

        categorias.append(cat)

    return render_template("cantina.html", categorias=categorias)