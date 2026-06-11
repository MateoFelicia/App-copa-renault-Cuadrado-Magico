from flask import Blueprint, render_template

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/admin-login")
def login():
    return render_template("admin/login.html", error=None)