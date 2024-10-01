class Config():
    DEBUG = True
    SECRET_KEY = "RooT$123456$"
    SQLALCHEMY_DATABASE_URI = "mysql://root:ravage01@localhost/db_erp_grupo_cooomeva"

"""
definimos las configuraciones que va a tener el proyecto en este caso 
- activamos el modo debug para mirar errores 
- definimos la clave secreta para los formularios
- generamos la ruta de coneccion al la base de datos previamente creada en mysql
"""
    