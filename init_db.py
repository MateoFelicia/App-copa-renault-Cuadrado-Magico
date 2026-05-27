import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Crea la colección "usuarios" con un usuario de prueba
db.collection("usuarios").add({
    "nombre": "Admin",
    "email": "admin@copa.com",
    "password": "1234"
})

print("Colecciones inicializadas correctamente")