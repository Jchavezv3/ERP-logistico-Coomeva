from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# usasmos CORS par aprevenir errors al mandar y recibir  solicitudes del cliente

db : object = SQLAlchemy()

def aplicacion() -> object:
    app : object = Flask(__name__)

    app.config.from_object("config.Config")

    CORS(app)

    db.init_app(app)

    from registro_empleado import crear_empleado
    app.register_blueprint(crear_empleado.bp)

    from registro_empleado import obtener_empleado
    app.register_blueprint(obtener_empleado.bp)

    from registro_empleado import actualizar_empleado
    app.register_blueprint(actualizar_empleado.bp)

    from registro_empleado import eliminar_empleado
    app.register_blueprint(eliminar_empleado.bp)
    
    with app.app_context():
        db.create_all()

    return app