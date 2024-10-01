from flask import Blueprint, request, jsonify
from registro_articulos.models import Registro_nuevo_inventario
from registro_articulos import db

bp : object = Blueprint("actualizar_articulo", __name__)

@bp.route("/registro-nuevo-inventario/<codigo>", methods = ["PUT", "PATCH"])
def actualizar_articulo(codigo) -> dict:
    datos_cliente : dict = request.get_json()
    articulo : dict = Registro_nuevo_inventario.query.filter_by(codigo=codigo).first()

    if "codigo" in datos_cliente:
        articulo.codigo = datos_cliente["codigo"]

    if "categoria" in datos_cliente:
        articulo.categoria = datos_cliente["categoria"]

    if "subcategoria" in datos_cliente:
        articulo.subcategoria = datos_cliente["subcategoria"]
    
    if "articulo" in datos_cliente:
        articulo.articulo = datos_cliente["articulo"]

    if "alerta_amarilla" in datos_cliente:
        articulo.alerta_amarilla = datos_cliente["alerta_amarilla"]

    if "alerta_roja" in datos_cliente:
        articulo.alerta_roja = datos_cliente["alerta_roja"]

    db.session.commit()
    return jsonify({"mensaje": "articulo actualizado exitosamente", "articulo": articulo.serializacion_datos()})

