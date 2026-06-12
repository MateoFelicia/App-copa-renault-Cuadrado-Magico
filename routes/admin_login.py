from flask import Blueprint, request, redirect, url_for, jsonify, session, redirect, render_template
import firebase_admin
from firebase_admin import credentials, auth

login_bp = Blueprint('admin_login', __name__)

cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)

auth.set_custom_user_claims("Iw29cbeyWASl4VUM5BTgzCOl8Qr1", {"rol": "superadmin"})
auth.set_custom_user_claims("zvCLe3q0DySAZtGNYQ5rMNbGlpZ2", {"rol": "superadmin"})
auth.set_custom_user_claims("2NdttyMAqJNNr5SfJaQLhcgNCa83", {"rol": "superadmin"})
auth.set_custom_user_claims("BNw7TUA6xVXhTtD6F6vEYQA4UNp2", {"rol": "superadmin"})

@login_bp.route('/admin/verify', methods=['POST'])
def verify_token():
    id_token = request.json.get('idToken')
    
    decoded_token = auth.verify_id_token(id_token)
    rol = decoded_token.get('rol')
    if not rol:
            return jsonify({'error': 'No autorizado'}), 403
    session['rol'] = rol
    session['uid'] = decoded_token['uid']
    return jsonify({'ok': True, 'rol': rol})

@login_bp.route('/admin/logout')
def logout():
    session.clear()
    return redirect(url_for('login.admin_login_page'))

@login_bp.route('/admin-login')
def admin_login_page():
    if session.get('rol'):
        return redirect('templates/admin/dashboard')
    return render_template('templates/admin/login.html')