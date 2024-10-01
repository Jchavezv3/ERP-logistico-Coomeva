from flask import Blueprint, request, jsonify
from registro_empleado.models import Empleados
from registro_empleado import db
from werkzeug.security import generate_password_hash

bp : object = Blueprint("actualizar_empleado", __name__)

@bp.route("/registro-empleados/<int:id>", methods = ["PUT", "PATCH"])
def actualizar_empleado(id) -> None:
    empleado : dict = Empleados.query.get_or_404(id)
    datos_cliente = request.get_json()
    
    if "nombres" in datos_cliente:
        empleado.nombres = datos_cliente["nombres"]

    if "apellidos" in datos_cliente:    
        empleado.apellidos = datos_cliente["apellidos"]

    if "cedula" in datos_cliente:    
        empleado.cedula = datos_cliente["cedula"]

    if "cargo" in datos_cliente:    
        empleado.cargo = datos_cliente["cargo"]

    if "correo" in datos_cliente:    
        empleado.correo = datos_cliente["correo"]

    if "clave" in datos_cliente:    
        empleado.clave = generate_password_hash(datos_cliente["clave"])

    db.session.commit()

    return jsonify({"mensaje": "Se actualizo el empleado", "empleado": empleado.serializacion_datos()})
