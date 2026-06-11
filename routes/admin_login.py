from flask import Blueprint, request, redirect, url_for, jsonify, session, redirect
from database import get_db
import firebase_admin
from firebase_admin import credentials, auth

admin_bp = Blueprint('admin', __name__)

cred = credentials.Certificate("ruta/al/archivo.json")
firebase_admin.initialize_app(cred)

auth.set_custom_user_claims("Iw29cbeyWASl4VUM5BTgzCOl8Qr1", {"rol": "superadmin"})
auth.set_custom_user_claims("zvCLe3q0DySAZtGNYQ5rMNbGlpZ2", {"rol": "superadmin"})
auth.set_custom_user_claims("2NdttyMAqJNNr5SfJaQLhcgNCa83", {"rol": "superadmin"})
auth.set_custom_user_claims("BNw7TUA6xVXhTtD6F6vEYQA4UNp2", {"rol": "superadmin"})