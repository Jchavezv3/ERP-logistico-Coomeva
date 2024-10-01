from flask import Blueprint, request, jsonify
from registro_empleado.models import Empleados
from registro_empleado import db

bp : object = Blueprint("obtener_empleado", __name__)

@bp.route("/registro-empleados", methods = ["GET"])
def obtner_empleado() -> None:
    empleados : list = Empleados.query.all()
    lista_empleados = []

    for empleado in empleados:
        lista_empleados.append(empleado.serializacion_datos())
    return jsonify({"empleados": lista_empleados})