from flask import(
    Blueprint, render_template, request, redirect, url_for, session, g
) 
# importamos el modelo de la db
from ERP.models import Empleados
# importaos la libreia par arecuprar la clave encriptada
from werkzeug.security import check_password_hash
# importamos el modulo que nos permite mantener la seccion iniciada
import functools


# Crea,os el Blueprint para controlas las vistas del modulo auth
bp : object = Blueprint("auth", __name__, url_prefix="/auth")

# creamos los endpoints a las vistas de la aplicacion
@bp.route("/login", methods=["GET", "POST"])
def login() -> str:
    if request.method == "POST":
        # recupramos del cliente el correo y la calve
        correo = request.form.get("correo")
        clave = request.form.get("clave")

        #consultamos en la base de datos si exite el correo
        user_existe = Empleados.query.filter_by(correo=correo).first()

        # hacemos las validaciones correspondientes y mandamos los codigos de rror si es neseaario 
        if user_existe is None:
            error = f"El nombre de usuario {correo} es incorrecto!!!"
            return render_template("login/inicio_seccion.html", error=error)

        elif not check_password_hash(user_existe.clave, clave):
            error = "La contraseña es incorrecta!!!"
            return render_template("login/inicio_seccion.html", error=error)

        else:
            #creamos una seccion con el id del user para poder iniciar la seccion
            session.clear()
            session["user_id"] = user_existe.id
            return redirect(url_for("admin.panel_admin"))

    else:
        return render_template("login/inicio_seccion.html")
# cerrar seccion
@bp.route("/logout")
def logout() -> str:
    # limipiamos la seccion para poder cerrarla
    session.clear()
    return redirect(url_for("auth.login"))

# mantener seccion 
@bp.before_app_request
def mantener_seccion() -> None:
    id_user = session.get("user_id")

    if id_user == None:
        g.user = None

    else:
        g.user = Empleados.query.get_or_404(id_user)

def vista_con_autenticacion(vista):
    @functools.wraps(vista)
    def vista_envuelta(*args, **kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return vista(*args, **kwargs)
    return vista_envuelta
"""
Creamos una funcion anidada que recibe como argumento la vista en donde se esta leugo
recibe el decorador " @functools.wraps(vista)" para la funcion anidada vista_envuelta(**kwargs)
si esta ultima encurtra que el valr del objeto "g.user" es none redirije al cliente al login
en caso de que no lo deja en la vista ctual
"""