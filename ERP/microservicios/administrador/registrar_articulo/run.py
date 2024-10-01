from registro_articulos import apliacion

if __name__ == "__main__":
    app : object = apliacion()
    app.run(host="0.0.0.0", port="3002")
