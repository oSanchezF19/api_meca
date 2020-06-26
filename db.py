import sqlite3

conn = sqlite3.connect("subsistemas.sqlite")

cursor = conn.cursor()
sql_query = """ CREATE TABLE subsistema(
    id integer PRIMARY KEY,
    nombre text NOT NULL,
    velocidad integer NOT NULL,
    distancia integer NOT NULL,
    paso integer NOT NULL,
    diametro integer NOT NULL,
    geometria text NOT NULL,
    ancho integer
)"""

cursor.execute(sql_query)


