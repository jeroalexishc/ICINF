class Usuarios:
    def __init__(self, nid, alias, nombre, apellidos, password):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos
        self.__password = password

    def muestra_datos(self):
        print("El nombre y los apellidos del usuario son: {} {}".format(self.nombre, self.apellidos))
        print("El ID de usuario es: {}.".format(self.nid))
        print("El alias del usuario es: {}.".format(self.alias))
        print("La contraseña es: {}".format(self.__password))

usuario1 = Usuarios("002", "PdePython", "Alex", "Vega García", "h$6pOcN9YDub")

usuario1.muestra_datos()
