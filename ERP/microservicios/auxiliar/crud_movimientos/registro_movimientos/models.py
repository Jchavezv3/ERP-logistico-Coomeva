from registro_movimientos import db

class Registro_nuevo_inventario(db.Model):
    __tablename__ = 'registro_nuevo_inventario'
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(50), nullable = False)
    subcategoria = db.Column(db.String(50), nullable = False)
    articulo = db.Column(db.String(50), nullable = False, unique = True)
    """
    toca crear esta referencia a la tabla que tiene la clave foranea para poder hacer la conexion exitosmante
    """

class Movimientos_inventario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    codigo = db.Column(db.Integer, db.ForeignKey('registro_nuevo_inventario.id'), nullable=False)
    categoria = db.Column(db.String(50), nullable = False)
    subcategoria = db.Column(db.String(50), nullable = False)
    articulo = db.Column(db.String(50), nullable = True, unique = True)
    fecha = db.Column(db.Date, nullable = False)
    cantidad_articulos = db.Column(db.Integer,  nullable = False)
    tipo_movimiento = db.Column(db.String(50),  nullable = False)
    costo = db.Column(db.String(50))


    # Relación con la tabla registro_nuevo_inventario
    registro = db.relationship('Registro_nuevo_inventario', backref='movimientos_inventario')

    def __init__(self, codigo, categoria, subcategoria, articulo, fecha, cantidad_articulos, tipo_movimiento) -> None:
        self.codigo = codigo
        self.categoria = categoria
        self.subcategoria = subcategoria
        self.articulo = articulo
        self.fecha = fecha
        self.cantidad_articulos = cantidad_articulos
        self.tipo_movimiento = tipo_movimiento

    def serializacion_datos(self) -> dict:
        return {
            "id": self.id,
            "codigo": self.codigo,
            "categoria": self.categoria,
            "subcategoria": self.subcategoria,
            "articulo": self.articulo,
            "fecha": self.fecha,
            "cantidad_articulos": self.cantidad_articulos,
            "tipo_movimiento": self.tipo_movimiento
        }