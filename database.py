import firebase_admin
from firebase_admin import credentials, firestore

_db = None

def init_app(app):
    global _db
    cred = credentials.Certificate("firebase_credentials.json")
    firebase_admin.initialize_app(cred)
    _db = firestore.client()
    app.extensions['firestore'] = _db

def get_db():
    return _db