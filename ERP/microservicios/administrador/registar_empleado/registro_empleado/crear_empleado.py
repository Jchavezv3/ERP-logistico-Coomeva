from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from registro_empleado.models import Empleados
from registro_empleado import db

bp : object = Blueprint("crear_empleado", __name__)

@bp.route("/registro-empleados", methods = ["POST"])
def crear_empleado() -> None:
    datos_cliente : dict = request.get_json()
    nuevo_empleado : object = Empleados(
        nombres = datos_cliente["nombres"], 
        apellidos = datos_cliente["apellidos"], 
        cedula = datos_cliente["cedula"], 
        cargo = datos_cliente["cargo"], 
        correo = datos_cliente["correo"], 
        clave = generate_password_hash(datos_cliente["clave"])
        )

    db.session.add(nuevo_empleado)
    db.session.commit()
    return jsonify({"message": "Empleado creado exitosamente"}), 201