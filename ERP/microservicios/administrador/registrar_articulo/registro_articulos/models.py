from registro_articulos import db

class Registro_nuevo_inventario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    codigo = db.Column(db.String(50), nullable = False, unique = True)
    categoria = db.Column(db.String(50), nullable = False)
    subcategoria = db.Column(db.String(50), nullable = False)
    articulo = db.Column(db.String(50), nullable = False, unique = True)
    alerta_amarilla = db.Column(db.Integer, nullable = False)
    alerta_roja = db.Column(db.Integer, nullable = False)

    def __init__(self, codigo, categoria, subcategoria, articulo, alerta_amarilla, alerta_roja) -> None:
        self.codigo = codigo
        self.categoria = categoria
        self.subcategoria = subcategoria
        self.articulo = articulo
        self.alerta_amarilla = alerta_amarilla
        self.alerta_roja = alerta_roja

    def serializacion_datos(self) -> dict:
        return {
            "id": self.id,
            "codigo": self.codigo,
            "categoria": self.categoria,
            "subcategoria": self.subcategoria,
            "articulo": self.articulo,
            "alerta_amarilla": self.alerta_amarilla,
            "alerta_roja": self.alerta_roja
        }
