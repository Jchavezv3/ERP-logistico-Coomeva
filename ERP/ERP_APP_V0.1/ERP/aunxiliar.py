from flask import Blueprint, render_template
# importamos el modulo decorador que permite la utenticacion de las vistas
from ERP.auth import vista_con_autenticacion

# Crea,os el Blueprint para controlas las vistas del modulo aunxiliar
bp : object = Blueprint("aunxiliar", __name__)

# creamos los endpoints a las vistas de la aplicacion

# Endpoints panel del aunxiliar
@bp.route("/movimientos-inventario")
@vista_con_autenticacion
def movimientos_inventario() -> str:
    return render_template("aunxiliar_logistico/Auxiliar_logistico.html")

