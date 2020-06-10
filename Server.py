from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return {
        "Soldadora de friccion por aglomeración": {
            "Eje horizontal": {
                "Velocidad": 500,
                "Distancia": 1500,
                "Paso": 25,
            },
            "Eje Vertical": {
                "Velocidad": 50,
                "Altura": 10,
                "Paso": 25,
            },
            "Disco soldadura": {
                "Velocidad": 18000,
                "Diametro": 200,
                "Geometria": "Tipo 1",
                "Ancho": 20,
            }
        }}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
