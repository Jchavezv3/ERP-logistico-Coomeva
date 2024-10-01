from flask import Blueprint, jsonify
from registro_articulos.models import Registro_nuevo_inventario
from registro_articulos import db

bp : object = Blueprint("eliminar_articulo", __name__)

@bp.route("/registro-nuevo-inventario/<codigo>", methods = ["DELETE"])
def eliminar_articulo(codigo) -> dict:
    articulo  = Registro_nuevo_inventario.query.filter_by(codigo=codigo).first()

    if not articulo:
        return jsonify({"mensaje": "el articulo no exite"}), 404

    else:
        db.session.delete(articulo)
        db.session.commit()
        return jsonify({"mensaje": "articulo eliminado exitosamente"})