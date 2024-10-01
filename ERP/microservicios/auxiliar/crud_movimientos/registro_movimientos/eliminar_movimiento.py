from flask import Blueprint, request, jsonify
from registro_movimientos import db
from registro_movimientos.models import Movimientos_inventario
bp : object = Blueprint("eliminar_movimiento", __name__)

@bp.route("/movimientos-inventario/<int:id>", methods = ["DELETE"])
def eliminar_movimiento(id) -> dict:
    movimiento : dict = Movimientos_inventario.query.get(id)

    if not movimiento:
        return jsonify({"mensaje": "el movimiento no exite"}), 404
    
    else:
        db.session.delete(movimiento)
        db.session.commit()
        return jsonify({"mensaje": "movimiento eliminado exitosamnte"})
