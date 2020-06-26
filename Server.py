'''

Aplicacion api para probar los metodos GET, POST, PUT Y DELETED

'''
from flask import Flask, jsonify, request
import json
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("subsistemas.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn


@app.route('/')
def page():
    return jsonify({"mensaje":"Soldadora de friccion por aglomeracion"})

@app.route('/Subsistemas')
def getSubsistemas():
    conn = db_connection()
    cursor = conn.cursor()
    cursor = conn.execute("SELECT * FROM subsistema")
    getSubsistemas =[
        dict(id=row[0], nombre=row[1], velocidad=row[2], distancia=row[3], paso=row[4], diametro=row[5], geometria=row[6], ancho=row[7])
        for row in cursor.fetchall()
    ]
    if getSubsistemas is not None:
        return jsonify(getSubsistemas), 200
    
@app.route('/Subsistemas/<int:id>')
def getsubsistema(id):
    conn = db_connection()
    cursor = conn.cursor()
    subsistema = None

    cursor.execute("SELECT * FROM subsistema WHERE id=?", (id,))
    rows = cursor.fetchall()
    for r in rows:
        subsistema = r
    if subsistema is not None:
        return jsonify(subsistema), 200
    else:
        return jsonify({"mensaje":"subsistema no encontrado"}), 404

@app.route('/Subsistemas', methods=['POST'])
def addsubsistema():
    conn = db_connection()
    cursor = conn.cursor()
    try:
        
        new_Nombre = request.form["Nombre"]
        new_Velocidad = int(request.form["Velocidad"])
        new_Distancia = int(request.form["Distancia"])
        new_Paso = int(request.form["Paso"])
        new_Diametro = int(request.form["Diametro"])
        new_Geometria= request.form["Geometria"]
        new_Ancho = int(request.form["Ancho"])
        
    except:
        return jsonify({"mensaje:":"error en la solicitud"}), 400
    sql = """INSERT INTO subsistema (Nombre, Velocidad, Distancia, Paso, Diametro, Geometria, Ancho)
                 VALUES (?, ?, ?, ?, ?, ?, ?)"""
    cursor = cursor.execute(sql, (new_Nombre, new_Velocidad, new_Distancia, new_Paso, new_Diametro, new_Geometria, new_Ancho))
    conn.commit()
    return jsonify({"mensaje":"subsistema creado exitosamente"}), 201

@app.route('/Subsistemas/<int:id>', methods=['PUT'])
def editsubsistema(id):
    conn = db_connection()
    sql = """UPDATE subsistema
                SET Nombre=?,
                    Velocidad=?,
                    Distancia=?,
                    Paso=?,
                    Diametro=?,
                    Geometria=?,
                    Ancho=?
                WHERE id=? """
    try:
        Nombre = request.form["Nombre"]
        Velocidad = int(request.form["Velocidad"])
        Distancia = int(request.form["Distancia"])
        Paso = int(request.form["Paso"])
        Diametro = int(request.form["Diametro"])
        Geometria= request.form["Geometria"]
        Ancho = int(request.form["Ancho"])
    except:
        return jsonify({"mensaje:":"error en la solicitud"}), 400

    updated_subsistema ={
        "id" : id,
        "Nombre" : Nombre,
        "Velocidad" : Velocidad,
        "Distancia" : Distancia,
        "Paso" : Paso,
        "Diametro" : Diametro,
        "Geometria" : Geometria,
        "Ancho" : Ancho,
    }
    conn.execute(sql, (Nombre, Velocidad, Distancia, Paso, Diametro, Geometria, Ancho, id))
    conn.commit()
    return jsonify(updated_subsistema), 200


@app.route('/Subsistemas/<int:id>', methods=['DELETE'])
def delectsubsistema(id):
    conn = db_connection()
    sql = """ DELETE FROM subsistema WHERE id=? """
    conn.execute(sql, (id,))
    conn.commit()
    return jsonify({"mensaje":"El subsistema de id: {} ah sido eliminado.".format(id)}), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
