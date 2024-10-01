from flask import Blueprint, request, jsonify
from registro_articulos import db
from registro_articulos.models import Registro_nuevo_inventario

bp : object = Blueprint("crear_articulo", __name__)

@bp.route("/registro-nuevo-inventario", methods = ["POST"])
def crear_articulo() -> dict:
    datos_cliente : dict = request.get_json()
    nuevo_articulo : object = Registro_nuevo_inventario(
        datos_cliente["codigo"],
        datos_cliente["categoria"], 
        datos_cliente["subcategoria"], 
        datos_cliente["articulo"], 
        datos_cliente["alerta_amarilla"], 
        datos_cliente["alerta_roja"]
        )
    
    db.session.add(nuevo_articulo)
    db.session.commit()
    return jsonify({"mensaje": "articulo creado exitosamente"}), 201