from flask import Blueprint, request, jsonify
from registro_articulos.models import Registro_nuevo_inventario

bp : object = Blueprint("obtner_articulo", __name__)

@bp.route("/registro-nuevo-inventario", methods = ["GET"])
def obtner_articulo() -> dict:
    articulos : list = Registro_nuevo_inventario.query.all()
    lista_articulos = []

    for articulo in articulos:
        lista_articulos.append(articulo.serializacion_datos())
    
    return jsonify({"articulos": lista_articulos})