from flask import Blueprint, render_template
from database import get_db

partidos_bp = Blueprint('partidos', __name__)

@partidos_bp.route("/partidos", defaults={"categoria": "Todas", "deporte": "Todos", "genero": "Todos"})
@partidos_bp.route("/partidos/<categoria>/<deporte>/<genero>")
def partidos(categoria, deporte, genero):
    db = get_db()

    todos = []
    for doc in db.collection("partidos").order_by("hora").stream():
        p = doc.to_dict()
        p['id'] = doc.id
        todos.append(p)

    filtrados = [
        p for p in todos
        if (categoria == "Todas" or p.get("categoria") == categoria)
        and (deporte   == "Todos"  or p.get("deporte")   == deporte)
        and (genero    == "Todos"  or p.get("genero")     == genero)
    ]

    return render_template(
        "partidos.html",
        partidos=filtrados,
        categoria_activa=categoria,
        deporte_activo=deporte,
        genero_activo=genero
    )

@partidos_bp.route("/fixture")
def fixture():
    return render_template("fixture.html")