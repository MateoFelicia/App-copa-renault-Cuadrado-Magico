import sqlite3

conexion = sqlite3.connect("database.db")
cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    email TEXT,
    password TEXT
)
""")

conexion.commit()
conexion.close()

print("Base de datos creada correctamente")