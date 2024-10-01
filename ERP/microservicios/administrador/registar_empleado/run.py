from registro_empleado import aplicacion

if __name__ == "__main__":
    app : object = aplicacion()
    app.run(host="0.0.0.0", port="3001")

# ejecutmos en el puerto 3001 ya que la aplicacion principal ejecuta en el 3000