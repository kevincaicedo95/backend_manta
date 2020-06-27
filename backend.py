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

#se define el enlace para consultar todos los empleados 
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


# se define el enlace para eliminar empleados por medio del documento 
@app.route("/empleados/<documento>", methods=['DELETE'])
def delete(documento):
    con = bd.get_connection()
    dbemp = con.dbmanta
    try:
        empleados = dbemp.empleados
        empleados.delete_one({'documento':documento})
        return jsonify({"mensaje":"OK"})
    finally:
        con.close()
        print("Conexion cerrada")

# se define el enlace para buscar empleado por documento
@app.route("/empleados/<documento>", methods=['GET'])
def get_cargo(documento):
    con = bd.get_connection()
    dbemp = con.dbmanta
    try:
        empleados = dbemp.empleados
        retorno = dumps(empleados.find_one({'documento': documento}))
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")