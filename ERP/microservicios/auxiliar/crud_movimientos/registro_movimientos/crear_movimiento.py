from flask import Blueprint, request, jsonify
from registro_movimientos import db
from registro_movimientos.models import Movimientos_inventario

bp : object = Blueprint("crear_movimientos", __name__)

@bp.route("/movimientos-inventario", methods = ["POST"])
def crear_movimiento() -> dict:
    datos_cliente : dict = request.get_json()
    nuevo_movimiento : object = Movimientos_inventario(
        datos_cliente["codigo"], 
        datos_cliente["categoria"],
        datos_cliente["subcategoria"],
        datos_cliente["articulo"],
        datos_cliente["fecha"],
        datos_cliente["cantidad_articulos"],
        datos_cliente["tipo_movimiento"]
        )
    
    db.session.add(nuevo_movimiento)
    db.session.commit()
    return jsonify({"mensaje": "movimiento creado exitosamente", "movimiento": nuevo_movimiento.serializacion_datos()}), 201

