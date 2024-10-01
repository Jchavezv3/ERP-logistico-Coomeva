from flask import Blueprint, render_template
# importamos el modulo decorador que permite la utenticacion de las vistas
from ERP.auth import vista_con_autenticacion

# Crea,os el Blueprint para controlas las vistas del modulo del analista
bp : object = Blueprint("analista", __name__)

# creamos los endpoints a las vistas de la aplicacion

# Endpoints panel del analista
@bp.route("/base-datos-inventario")
@vista_con_autenticacion
def base_datos() -> str:
    return render_template("analista_inventario/Analista_inventario.html")

