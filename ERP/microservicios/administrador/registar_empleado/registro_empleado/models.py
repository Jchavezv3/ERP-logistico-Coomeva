from registro_empleado import db

class Empleados(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombres = db.Column(db.String(20), nullable = False)
    apellidos = db.Column(db.String(20), nullable = False)
    cedula = db.Column(db.String(20), nullable = False, unique = True)
    cargo = db.Column(db.String(30), nullable = False)
    correo = db.Column(db.String(50), nullable = False)
    clave = db.Column(db.Text, nullable = False)

    def __init__(self, nombres, apellidos, cedula, cargo, correo, clave):
        self.nombres = nombres
        self.apellidos = apellidos
        self.cedula = cedula
        self.cargo = cargo
        self.correo = correo
        self.clave = clave

    def serializacion_datos(self) -> dict:
        return {
            "id": self.id,
            "nombres": self.nombres,
            "apellidos": self.apellidos,
            "cedula": self.cedula,
            "cargo": self.cargo,
            "correo": self.correo,
            "clave": self.clave
        }