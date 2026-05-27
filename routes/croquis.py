from flask import  render_template, Blueprint

croquis_bp = Blueprint('croquis', __name__)

@croquis_bp.route("/croquis", methods=["GET"])
def croquis():
    return render_template("croquis.html")