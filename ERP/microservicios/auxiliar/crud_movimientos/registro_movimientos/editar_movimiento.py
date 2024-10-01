from flask import Blueprint, request, jsonify
from registro_movimientos.models import Movimientos_inventario


bp : object = Blueprint("editar_movimiento", __name__)

@bp.route("/movimientos-inventario/<int:id>", methods = ["PUT", "PATCH"])
def editar_movimiento(id) -> dict:
    movimiento : dict = Movimientos_inventario.query.get_or_404(id)
    datos_cliente : dict = request.get_json()

    if "codigo" in datos_cliente:
        movimiento.codigo = datos_cliente["codigo"]

    if "categoria" in datos_cliente:
        movimiento.categoria = datos_cliente["categoria"]

    if "subcategoria" in datos_cliente:
        movimiento.subcategoria = datos_cliente["subcategoria"]

    if "articulo" in datos_cliente:
        movimiento.articulo = datos_cliente["articulo"]

    if "fecha" in datos_cliente:
        movimiento.fecha = datos_cliente["fecha"]

    if "cantidad_articulos" in datos_cliente:
        movimiento.cantidad_articulos = datos_cliente["cantidad_articulos"]

    if "tipo_movimiento" in datos_cliente:
        movimiento.tipo_movimiento = datos_cliente["tipo_movimiento"]

    return jsonify({"mensaje": "movimiento actualizado", "movimiento": movimiento.serializacion_datos()})