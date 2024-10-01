from flask import Blueprint, request, jsonify
from registro_empleado.models import Empleados
from registro_empleado import db

bp : object = Blueprint("eliminar_empleado", __name__)

@bp.route("/registro-empleados/<int:id>", methods = ["DELETE"])
def eliminar_empleado(id) -> None:
    empleado : dict = Empleados.query.get(id)
    if not empleado:
        return "el empleado no existe", 404
    
    else:
        db.session.delete(empleado)
        db.session.commit()
        return jsonify({"message": "Empleado eliminado exitosamente"})