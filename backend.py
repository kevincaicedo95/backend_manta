from flask import Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
import bd
from datetime import datetime

app = Flask(__name__)

## coleccion Empleados
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
def get_document(documento):
    con = bd.get_connection()
    dbemp = con.dbmanta
    try:
        empleados = dbemp.empleados
        retorno = dumps(empleados.find_one({'documento': documento}))
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

## coleccion Proveedor
#se define el enlace para consultar todos los Proveedores
@app.route("/provedor", methods=['GET'])
def get_provedor():
    con = bd.get_connection()
    dbemp = con.dbmanta
    try:
        provedor = dbemp.provedor
        retorno = dumps(provedor.find())
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

#Se define el enlace para ingresar proveedores
@app.route("/provedor", methods=['POST'])
def create_provedor():
    data = request.get_json()
    con = bd.get_connection()
    dbemp = con.dbmanta
    try:
        provedor = dbemp.provedor
        provedor.insert(data)
        return jsonify({"mensaje":"OK"})
    finally:
        con.close()
        print("Conexion cerrada")
        
# se define el enlace para buscar provedor por NIT de la empresa 
@app.route("/provedor/<NIT>", methods=['GET'])
def get_provNIT(NIT):
    con = bd.get_connection()
    dbemp = con.dbmanta
    try:
        provedor = dbemp.provedor
        retorno = dumps(provedor.find_one({'NIT': NIT}))
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")
    

## insumos
# se define el enlace para ingresar insumos
@app.route("/insumos", methods=['POST'])
def create_insumos():
    data = request.get_json()
    con = bd.get_connection()
    dbemp = con.dbmanta
    fecha= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        insumos = dbemp.insumos
        data.update({"fecha":fecha})
        insumos.insert(data)
        return jsonify({"mensaje":"OK"})
    finally:
        con.close()
        print("Conexion cerrada")

#se define el enlace para consultar todos los insumos
@app.route("/insumos", methods=['GET'])
def get_insumos():
    con = bd.get_connection()
    dbemp = con.dbmanta
    try:
        insumos = dbemp.insumos
        retorno = dumps(insumos.find())
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

# se define el enlace para buscar insumo por codigo 
@app.route("/insumo/<codigo>", methods=['GET'])
def get_inscod(codigo):
    con = bd.get_connection()
    dbemp = con.dbmanta
    try:
        insumos = dbemp.insumos
        retorno = dumps(insumos.find_one({'codigo': codigo}))
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

## Proceso de la manta
#Se define el enlace para ingresar la manta y el proceso 
@app.route("/proceso", methods=['POST'])
def create_proceso():
    data = request.get_json()
    con = bd.get_connection()
    dbemp = con.dbmanta
    fecha= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        proceso = dbemp.proceso
        data.update({"fecha":fecha})
        proceso.insert(data)
        return jsonify({"mensaje":"OK"})
    finally:
        con.close()
        print("Conexion cerrada")

# se define el enlace para la manta 
@app.route("/proceso/<manta>", methods=['GET'])
def get_proman(manta):
    con = bd.get_connection()
    dbemp = con.dbmanta
    try:
        proceso= dbemp.proceso
        retorno = dumps(proceso.find_one({'manta': manta}))
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

#enlace para buscar todos los procesos 
@app.route("/proceso", methods=['GET'])
def get_proceso():
    con = bd.get_connection()
    dbemp = con.dbmanta
    try:
        proceso = dbemp.proceso
        retorno = dumps(proceso.find())
        return jsonify(retorno)
    finally:
        con.close()
        print("Conexion cerrada")

