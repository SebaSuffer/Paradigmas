from flask import Flask, render_template, jsonify
from flask_cors import CORS, cross_origin
import json
import os  # Importa el módulo os para trabajar con rutas

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
CORS(app) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/datos')
@cross_origin(origin='*', headers=['Content-Type', 'Authorization'])
def obtener_datos():
    try:
        # Obtiene la ruta absoluta al archivo data.json
        ruta_archivo = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'data.json')

        # Verifica si el archivo existe
        if os.path.exists(ruta_archivo):
            # Abre el archivo utilizando with para garantizar que se cierre correctamente
            with open(ruta_archivo, "r") as archivo_json:
                datos = json.load(archivo_json)
                # Resto del código...

                conteo_manhattan = 0
                conteo_brooklyn = 0
                conteo_queens = 0
                conteo_bronx = 0
                conteo_staten_island = 0

                for linea in datos:
                    if linea["neighbourhood_group"] == "Manhattan":
                        conteo_manhattan += 1
                    elif linea["neighbourhood_group"] == "Brooklyn":
                        conteo_brooklyn += 1
                    elif linea["neighbourhood_group"] == "Queens":
                        conteo_queens += 1
                    elif linea["neighbourhood_group"] == "Bronx":
                        conteo_bronx += 1
                    elif linea["neighbourhood_group"] == "Staten Island":
                        conteo_staten_island += 1

                resultados = {
                    "Manhattan": conteo_manhattan,
                    "Brooklyn": conteo_brooklyn,
                    "Queens": conteo_queens,
                    "Bronx": conteo_bronx,
                    "Staten Island": conteo_staten_island
                }

                return jsonify(resultados)
        else:
            return jsonify({"error": "El archivo data.json no existe."})
    except Exception as e:
        print("Error al cargar datos:", e)
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
