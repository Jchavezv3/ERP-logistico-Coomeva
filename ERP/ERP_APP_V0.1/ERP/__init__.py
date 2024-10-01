from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Creamos una instancia de la clase SQLAlchemy esta nos permitira interactuar con la base de datos
db : object = SQLAlchemy()

def aplication() -> None:
    # Creamos una instancia de Flask para crear nuestra app
    app : object = Flask(__name__)

    # Implementamos la configuracion del proyecto
    app.config.from_object("config.Config")

    # Inicializamos la base de datos en la aplicacion
    db.init_app(app)

    #Registramos los Blueprints de cada modulo de la aplicacion

    # Modulo Login
    from ERP import auth
    app.register_blueprint(auth.bp)

    # Modulo Administrador
    from ERP import admin
    app.register_blueprint(admin.bp)

    # Modulo Aunxiliar de Inventario
    from ERP import aunxiliar
    app.register_blueprint(aunxiliar.bp)

    # Modulo Analista de Inventario
    from ERP import analista
    app.register_blueprint(analista.bp)

    return app