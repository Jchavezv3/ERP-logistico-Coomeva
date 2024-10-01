# creamos un modelo que mapero los campos de la base de datos ocn los cules haremos la validacion par ainiciar
#  seccion
from ERP import db

class Empleados(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    correo = db.Column(db.String(50), nullable = False)
    clave = db.Column(db.Text, nullable = False)

    def __init__(self, correo, clave):
        self.correo = correo
        self.clave = clave

    def serializacion_datos(self) -> dict:
        return {
            "id": self.id,
            "correo": self.correo,
            "clave": self.clave
        }