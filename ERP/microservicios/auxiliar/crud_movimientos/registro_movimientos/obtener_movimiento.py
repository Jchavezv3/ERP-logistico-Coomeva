from flask import Blueprint, jsonify
from registro_movimientos import db
from registro_movimientos.models import Movimientos_inventario, Registro_nuevo_inventario

bp : object = Blueprint("obtener_movimientos", __name__)

@bp.route("/movimientos-inventario", methods = ["GET"])
def obtener_informacion_movimientos() -> dict:
    categorias : list = Registro_nuevo_inventario.query.with_entities(Registro_nuevo_inventario.categoria).all()
    categorias_lista = []
    for registro_categoria in categorias:
        categorias_lista.append(registro_categoria.categoria)

    subcategorias : list = Registro_nuevo_inventario.query.with_entities(Registro_nuevo_inventario.subcategoria).all()
    subcategorias_lista = []
    for registro_subcategoria in subcategorias:
        subcategorias_lista.append(registro_subcategoria.subcategoria)

    articulos : list = Registro_nuevo_inventario.query.with_entities(Registro_nuevo_inventario.articulo).all()
    articulos_lista = []
    for registro_articulo in articulos:
        articulos_lista.append(registro_articulo.articulo)


    movimientos : list = Movimientos_inventario.query.all()
    lista_movimientos : list = []
    for movimiento in movimientos:
        lista_movimientos.append(movimiento.serializacion_datos())

    return jsonify({
        "movimientos": lista_movimientos,
        "items_categorias": categorias_lista,
        "items_subcategorias": subcategorias_lista,
        "items_articulo": articulos_lista
        })