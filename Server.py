'''

Aplicacion api para probar los metodos GET, POST, PUT Y DELETED

'''
from flask import Flask, jsonify, request
from Subsistemas import Subsistemas

app = Flask(__name__)

@app.route('/')
def page():
    return "Soldadora de friccion por aglomeracion" 

@app.route('/Subsistemas')
def getSubsistemas():
    return jsonify({"mensaje": "Variables de control", "Subsistemas": Subsistemas})

@app.route('/Subsistemas/<string:subsistema_Nombre>')
def getsubsistema(subsistema_Nombre):
    SubsistemasFound = [subsistema for subsistema in Subsistemas if subsistema['Nombre'] == subsistema_Nombre]
    if (len(SubsistemasFound) > 0):
        return jsonify({"subsistema":SubsistemasFound[0]})
    return jsonify({"mensaje":"error 404 subsistema no encontrado"})

@app.route('/Subsistemas', methods=['POST'])
def addsubsistema():
    new_subsistema ={
        "Nombre": request.json['Nombre'],
        "Velocidad": request.json['Velocidad'],
        "Distancia": request.json['Distancia'],
        "Paso": request.json['Paso'],
        "Diametro": request.json['Diametro'],
        "Geometria": request.json['Geometria'],
        "Ancho": request.json['Ancho']
    }
    Subsistemas.append(new_subsistema)
    return jsonify({"mensaje:":"Subsistemas added Succesfully", "Subsistemas": Subsistemas})

@app.route('/Subsistemas/<string:subsistema_Nombre>', methods=['PUT'])
def editsubsistema(subsistema_Nombre):
    subsistemaFound= [subsistema for subsistema in Subsistemas if subsistema['Nombre'] == subsistema_Nombre]
    if (len(subsistemaFound) > 0):
        subsistemaFound[0]['Nombre'] = request.json['Nombre']
        subsistemaFound[0]['Velocidad'] = request.json['Velocidad']
        subsistemaFound[0]['Distancia'] = request.json['Distancia']
        subsistemaFound[0]['Paso'] = request.json['Paso']
        subsistemaFound[0]['Diametro'] = request.json['Diametro']
        subsistemaFound[0]['Geometria'] = request.json['Geometria']
        subsistemaFound[0]['Ancho'] = request.json['Ancho']
        return jsonify({
        "mensaje": "subsistema Update",
        "subsistema":subsistemaFound[0]
        })
    return jsonify({"mesage":"error 404 subsistema no encontrado"})

@app.route('/Subsistemas/<string:subsistema_Nombre>', methods=['DELETE'])
def delectsubsistema(subsistema_Nombre):
    subsistemaFound= [subsistema for subsistema in Subsistemas if subsistema['Nombre'] == subsistema_Nombre]
    if (len(subsistemaFound) > 0):
        Subsistemas.remove(subsistemaFound[0])
        return jsonify({
            "mensaje": "subsistema eliminado",
            "Subsistemas": Subsistemas
        })
    return jsonify({"mesage":"error 404 subsistema no encontrado"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
