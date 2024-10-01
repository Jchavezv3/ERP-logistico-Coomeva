from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db : object = SQLAlchemy()

def aplicacion() -> object:
    app : object = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    CORS(app)

    from registro_movimientos import crear_movimiento
    app.register_blueprint(crear_movimiento.bp)

    from registro_movimientos import obtener_movimiento
    app.register_blueprint(obtener_movimiento.bp)

    from registro_movimientos import editar_movimiento
    app.register_blueprint(editar_movimiento.bp)

    from registro_movimientos import eliminar_movimiento
    app.register_blueprint(eliminar_movimiento.bp)

    with app.app_context():
        db.create_all()


    return app