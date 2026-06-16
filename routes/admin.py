from flask import Blueprint, render_template, request, redirect, url_for, session
from functools import wraps
from database import get_db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def login_requerido(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('rol'):
            return redirect('/admin-login')
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route("/")
@login_requerido
def dashboard():
    db = get_db()
    stats = {
        "noticias":  len(list(db.collection("noticias").stream())),
        "partidos":  len(list(db.collection("partidos").stream())),
        "sponsors":  len(list(db.collection("sponsors").stream())),
        "categorias": len(list(db.collection("categorias_cantina").stream())),
    }
    return render_template("admin/dashboard.html", stats=stats)


# ══════════════════════════════════════════════════════════════
# NOTICIAS
# ══════════════════════════════════════════════════════════════
@admin_bp.route("/noticias")
@login_requerido
def admin_noticias():
    db = get_db()
    noticias = []
    for doc in db.collection("noticias").order_by("fecha", direction="DESCENDING").stream():
        n = doc.to_dict(); n['id'] = doc.id
        noticias.append(n)
    return render_template("admin/noticias.html", noticias=noticias)

@admin_bp.route("/noticias/nueva", methods=["GET", "POST"])
@login_requerido
def nueva_noticia():
    if request.method == "POST":
        db = get_db()
        db.collection("noticias").add({
            "titulo":      request.form["titulo"],
            "descripcion": request.form["descripcion"],
            "imagen":      request.form.get("imagen", ""),
            "fecha":       request.form.get("fecha", ""),
        })
        return redirect(url_for("admin.admin_noticias"))
    return render_template("admin/noticia_form.html", noticia=None)

@admin_bp.route("/noticias/<id>/editar", methods=["GET", "POST"])
@login_requerido
def editar_noticia(id):
    db = get_db()
    ref = db.collection("noticias").document(id)
    if request.method == "POST":
        ref.update({
            "titulo":      request.form["titulo"],
            "descripcion": request.form["descripcion"],
            "imagen":      request.form.get("imagen", ""),
            "fecha":       request.form.get("fecha", ""),
        })
        return redirect(url_for("admin.admin_noticias"))
    n = ref.get().to_dict(); n['id'] = id
    return render_template("admin/noticia_form.html", noticia=n)

@admin_bp.route("/noticias/<id>/eliminar", methods=["POST"])
@login_requerido
def eliminar_noticia(id):
    db = get_db()
    db.collection("noticias").document(id).delete()
    return redirect(url_for("admin.admin_noticias"))


# ══════════════════════════════════════════════════════════════
# PARTIDOS
# ══════════════════════════════════════════════════════════════
@admin_bp.route("/partidos")
@login_requerido
def admin_partidos():
    db = get_db()
    partidos = []
    for doc in db.collection("partidos").order_by("hora").stream():
        p = doc.to_dict(); p['id'] = doc.id
        partidos.append(p)
    return render_template("admin/partidos.html", partidos=partidos)

@admin_bp.route("/partidos/nuevo", methods=["GET", "POST"])
@login_requerido
def nuevo_partido():
    if request.method == "POST":
        db = get_db()
        db.collection("partidos").add({
            "hora":             request.form["hora"],
            "equipo_local":     request.form["equipo_local"],
            "equipo_visitante": request.form["equipo_visitante"],
            "goles_local":      request.form.get("goles_local") or None,
            "goles_visitante":  request.form.get("goles_visitante") or None,
            "categoria":        request.form.get("categoria", "Mayor"),
            "deporte":          request.form.get("deporte", "Fútbol"),
            "genero":           request.form.get("genero", "Masculino"),
            "estado":           request.form.get("estado", "prox"),
            "cancha":           request.form.get("cancha", ""),
        })
        return redirect(url_for("admin.admin_partidos"))
    return render_template("admin/partido_form.html", partido=None)

@admin_bp.route("/partidos/<id>/editar", methods=["GET", "POST"])
@login_requerido
def editar_partido(id):
    db = get_db()
    ref = db.collection("partidos").document(id)
    if request.method == "POST":
        ref.update({
            "hora":             request.form["hora"],
            "equipo_local":     request.form["equipo_local"],
            "equipo_visitante": request.form["equipo_visitante"],
            "goles_local":      request.form.get("goles_local") or None,
            "goles_visitante":  request.form.get("goles_visitante") or None,
            "categoria":        request.form.get("categoria", "Mayor"),
            "deporte":          request.form.get("deporte", "Fútbol"),
            "genero":           request.form.get("genero", "Masculino"),
            "estado":           request.form.get("estado", "prox"),
            "cancha":           request.form.get("cancha", ""),
        })
        return redirect(url_for("admin.admin_partidos"))
    p = ref.get().to_dict(); p['id'] = id
    return render_template("admin/partido_form.html", partido=p)

@admin_bp.route("/partidos/<id>/eliminar", methods=["POST"])
@login_requerido
def eliminar_partido(id):
    db = get_db()
    db.collection("partidos").document(id).delete()
    return redirect(url_for("admin.admin_partidos"))


# ══════════════════════════════════════════════════════════════
# CANTINA — Categorías
# ══════════════════════════════════════════════════════════════
@admin_bp.route("/cantina")
@login_requerido
def admin_cantina():
    db = get_db()
    categorias = []
    for doc in db.collection("categorias_cantina").order_by("orden").stream():
        cat = doc.to_dict(); cat['id'] = doc.id
        productos = []
        for pdoc in db.collection("categorias_cantina").document(doc.id).collection("productos").stream():
            p = pdoc.to_dict(); p['id'] = pdoc.id
            productos.append(p)
        cat['productos'] = productos
        categorias.append(cat)
    return render_template("admin/cantina.html", categorias=categorias)

@admin_bp.route("/cantina/nueva-categoria", methods=["GET", "POST"])
@login_requerido
def nueva_categoria():
    if request.method == "POST":
        db = get_db()
        db.collection("categorias_cantina").add({
            "nombre": request.form["nombre"],
            "orden":  int(request.form.get("orden", 0)),
            "promo":  "promo" in request.form,
        })
        return redirect(url_for("admin.admin_cantina"))
    return render_template("admin/categoria_form.html", categoria=None)

@admin_bp.route("/cantina/<cat_id>/editar", methods=["GET", "POST"])
@login_requerido
def editar_categoria(cat_id):
    db = get_db()
    ref = db.collection("categorias_cantina").document(cat_id)
    if request.method == "POST":
        ref.update({
            "nombre": request.form["nombre"],
            "orden":  int(request.form.get("orden", 0)),
            "promo":  "promo" in request.form,
        })
        return redirect(url_for("admin.admin_cantina"))
    cat = ref.get().to_dict(); cat['id'] = cat_id
    return render_template("admin/categoria_form.html", categoria=cat)

@admin_bp.route("/cantina/<cat_id>/eliminar", methods=["POST"])
@login_requerido
def eliminar_categoria(cat_id):
    db = get_db()
    db.collection("categorias_cantina").document(cat_id).delete()
    return redirect(url_for("admin.admin_cantina"))


# ══════════════════════════════════════════════════════════════
# CANTINA — Productos
# ══════════════════════════════════════════════════════════════
@admin_bp.route("/cantina/<cat_id>/nuevo-producto", methods=["GET", "POST"])
@login_requerido
def nuevo_producto(cat_id):
    db = get_db()
    if request.method == "POST":
        db.collection("categorias_cantina").document(cat_id).collection("productos").add({
            "nombre": request.form["nombre"],
            "precio": float(request.form["precio"]),
            "imagen": request.form.get("imagen", ""),
        })
        return redirect(url_for("admin.admin_cantina"))
    cat = db.collection("categorias_cantina").document(cat_id).get().to_dict()
    return render_template("admin/producto_form.html", producto=None, cat_id=cat_id, cat=cat)

@admin_bp.route("/cantina/<cat_id>/productos/<prod_id>/editar", methods=["GET", "POST"])
@login_requerido
def editar_producto(cat_id, prod_id):
    db = get_db()
    ref = db.collection("categorias_cantina").document(cat_id).collection("productos").document(prod_id)
    if request.method == "POST":
        ref.update({
            "nombre": request.form["nombre"],
            "precio": float(request.form["precio"]),
            "imagen": request.form.get("imagen", ""),
        })
        return redirect(url_for("admin.admin_cantina"))
    p = ref.get().to_dict(); p['id'] = prod_id
    cat = db.collection("categorias_cantina").document(cat_id).get().to_dict()
    return render_template("admin/producto_form.html", producto=p, cat_id=cat_id, cat=cat)

@admin_bp.route("/cantina/<cat_id>/productos/<prod_id>/eliminar", methods=["POST"])
@login_requerido
def eliminar_producto(cat_id, prod_id):
    db = get_db()
    db.collection("categorias_cantina").document(cat_id).collection("productos").document(prod_id).delete()
    return redirect(url_for("admin.admin_cantina"))


# ══════════════════════════════════════════════════════════════
# SPONSORS
# ══════════════════════════════════════════════════════════════
@admin_bp.route("/sponsors")
@login_requerido
def admin_sponsors():
    db = get_db()
    sponsors = []
    for doc in db.collection("sponsors").stream():
        s = doc.to_dict(); s['id'] = doc.id
        sponsors.append(s)
    return render_template("admin/sponsors.html", sponsors=sponsors)

@admin_bp.route("/sponsors/nuevo", methods=["GET", "POST"])
@login_requerido
def nuevo_sponsor():
    if request.method == "POST":
        db = get_db()
        db.collection("sponsors").add({
            "nombre": request.form["nombre"],
            "imagen": request.form.get("imagen", ""),
            "url":    request.form.get("url", ""),
        })
        return redirect(url_for("admin.admin_sponsors"))
    return render_template("admin/sponsor_form.html", sponsor=None)

@admin_bp.route("/sponsors/<id>/editar", methods=["GET", "POST"])
@login_requerido
def editar_sponsor(id):
    db = get_db()
    ref = db.collection("sponsors").document(id)
    if request.method == "POST":
        ref.update({
            "nombre": request.form["nombre"],
            "imagen": request.form.get("imagen", ""),
            "url":    request.form.get("url", ""),
        })
        return redirect(url_for("admin.admin_sponsors"))
    s = ref.get().to_dict(); s['id'] = id
    return render_template("admin/sponsor_form.html", sponsor=s)

@admin_bp.route("/sponsors/<id>/eliminar", methods=["POST"])
@login_requerido
def eliminar_sponsor(id):
    db = get_db()
    db.collection("sponsors").document(id).delete()
    return redirect(url_for("admin.admin_sponsors"))