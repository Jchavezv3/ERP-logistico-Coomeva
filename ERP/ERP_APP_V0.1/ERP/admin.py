from flask import (
    Blueprint, render_template, redirect, request, url_for
    )
# importamos el modulo decorador que permite la utenticacion de las vistas
from ERP.auth import vista_con_autenticacion

# Creamos el Blueprint para controlas las vistas del modulo del adminitrador del sistema
bp : object = Blueprint("admin", __name__)

# creamos los endpoints a las vistas de la aplicacion

# Endpoints panel general del administrador
@bp.route("/")
@bp.route("/panel-general")
@vista_con_autenticacion
def panel_admin() -> str:
    return render_template("administrador/Admin.html")


# Endpoints modulo registro de nuevo inventario a microservicios
@bp.route("/registro-nuevo-inventario")
@vista_con_autenticacion
def nuevo_inventario() -> str:
    return render_template("administrador/registro_de_nuevo_inventario.html")

# Endpoints modulo registro de empleados a microservicios
@bp.route("/registro-empleados")
@vista_con_autenticacion
def registro_empleados() -> str:
    return render_template("administrador/Registro_de_empleados.html")

# Endpoints modulo politica de compras
@bp.route("/politicas-inventario")
@vista_con_autenticacion
def politicas_inventario() -> str:
    return render_template("administrador/politica_compras.html")