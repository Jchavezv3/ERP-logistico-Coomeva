from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db : object = SQLAlchemy()

def apliacion() -> object:
    app : object = Flask(__name__)

    app.config.from_object("config.Config")

    CORS(app)

    db.init_app(app)

    from registro_articulos import crear_articulo
    app.register_blueprint(crear_articulo.bp)

    from registro_articulos import obtener_articulo
    app.register_blueprint(obtener_articulo.bp)

    from registro_articulos import actualizar_articulo
    app.register_blueprint(actualizar_articulo.bp)

    from registro_articulos import eliminar_articulo
    app.register_blueprint(eliminar_articulo.bp)

    with app.app_context():
        db.create_all()

    return app