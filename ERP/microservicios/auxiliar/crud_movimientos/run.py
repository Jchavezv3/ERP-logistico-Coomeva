from registro_movimientos import aplicacion

if __name__ == "__main__":
    app : object = aplicacion()
    app.run(host="0.0.0.0", port="3003")