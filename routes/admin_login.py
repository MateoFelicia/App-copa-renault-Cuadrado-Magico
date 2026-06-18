from flask import Blueprint, request, redirect, url_for, jsonify, session, redirect, render_template
from firebase_admin import auth

login_bp = Blueprint('admin_login', __name__)

@login_bp.route('/admin/verify', methods=['POST'])
def verify_token():
    id_token = request.json.get('idToken')
    try:
        decoded_token = auth.verify_id_token(id_token)
        rol = decoded_token.get('rol')
        if not rol:
                return jsonify({'error': 'No autorizado'}), 403
        session['rol'] = rol
        session['uid'] = decoded_token['uid']
        return jsonify({'ok': True, 'rol': rol})
    except Exception as e:
        return jsonify({'error': str(e)}), 401

@login_bp.route('/admin/logout')
def logout():
    session.clear()
    return redirect(url_for('admin_login.admin_login_page'))

@login_bp.route('/admin-login')
def admin_login_page():
    if session.get('rol'):
        return redirect('/admin')
    return render_template('admin/login.html', error=None)

# try:
#         # Firebase Admin verifica que el token sea auténtico
#         decoded_token = auth.verify_id_token(id_token)
#         rol = decoded_token.get('rol')
        
#         # Si el token no tiene rol asignado, no es admin
#         if not rol:
#             return jsonify({'error': 'No autorizado'}), 403
        
#         # Guarda el rol en la sesión del navegador
#         session['rol'] = rol
#         session['uid'] = decoded_token['uid']
        
#         return jsonify({'ok': True, 'rol': rol})
    
#     except Exception as e:
#         return jsonify({'error': str(e)}), 401