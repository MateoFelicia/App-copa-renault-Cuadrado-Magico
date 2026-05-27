# Cómo funciona el proyecto Flask con SQLite 

El proyecto está dividido en varios archivos, cada uno con una responsabilidad clara. La idea es que cada archivo haga una sola cosa y no se mezclen las responsabilidades.

# init.py — Crear la base de datos
Este archivo se ejecuta una sola vez, antes de arrancar el proyecto. Su único trabajo es crear las tablas en la base de datos si no existen. Una vez ejecutado, genera el archivo database.db y no se vuelve a tocar.

# database.db — La base de datos
No es un archivo de código, es la base de datos en sí. Acá viven todos los datos: noticias, usuarios, etc. Flask y Python no la tocan directamente, sino que se comunican con ella a través de consultas SQL.

# database.py — La conexión
Este archivo sabe cómo conectarse a la base de datos. Cuando cualquier otro archivo necesita hablar con la DB, le pide la conexión a este archivo a través de la función get_db(). Así no hay que repetir el código de conexión en cada archivo.

# app.py — El punto de entrada
Es el archivo principal. No maneja datos ni lógica, su único trabajo es arrancar Flask y avisar qué archivos de rutas existen en el proyecto. Sin este archivo, la aplicación no funciona.
app.py registra:
    ├── noticias_bp  (de noticias.py)
    └── usuarios_bp  (de usuarios.py)

# noticias.py, usuarios.py, etc. — Las rutas
Acá vive toda la lógica. Cada archivo maneja un tema (noticias, usuarios, etc.) y define qué pasa cuando alguien entra a una URL. Reciben el request, consultan la base de datos y devuelven una respuesta HTML.

# El flujo completo
Cuando alguien entra a /noticias en el navegador, esto es lo que pasa:
1. El navegador hace un request a /noticias
2. Flask (app.py) recibe el request
3. Busca qué archivo maneja esa ruta → encuentra noticias.py
4. noticias.py le pide la conexión a database.py
5. database.py se conecta a database.db
6. noticias.py consulta los datos con SQL
7. Los datos se mandan al template noticias.html
8. El HTML armado se devuelve al navegador

# Resumen
ArchivoCuándo se usaQué haceinit.pyUna sola vezCrea las tablasdatabase.dbSiempreGuarda los datosdatabase.pyEn cada requestProvee la conexiónapp.pyAl arrancarInicia Flask y registra rutasnoticias.pyEn cada request a /noticiasLógica y consultas de noticias