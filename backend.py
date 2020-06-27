from flask import Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
import bd

app = Flask(__name__)


#Se define el enlace para ingresar empleados
@app.route("/empleados", methods=['POST'])
def create():
    data = request.get_json()
    con = bd.get_connection()
    dbemp = con.dbmanta
    try:
        empleados = dbemp.empleados
        empleados.insert(data)
        return jsonify({"mensaje":"OK"})
    finally:
        con.close()
        print("Conexion cerrada")

#se define el enlace para consultar los empleados 
@app.route("/empleados", methods=['GET'])
def get_empleados():
    con = bd.get_connection()
    dbemp = con.dbmanta
    try:
        empleados = dbemp.empleados
        retorno = dumps(empleados.find())
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")