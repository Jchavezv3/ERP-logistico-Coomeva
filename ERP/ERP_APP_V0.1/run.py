from ERP import aplication

if __name__ == "__main__":
    app : object = aplication()
    app.run(port="3000", host="0.0.0.0")
    
    """
    configuramos el modlo de ejecucion de nuestra aplicacion 
    importando la funcion de la palicacion asignanosela a una nueva varible
    y usando el metodo run para su ejecucion
    """