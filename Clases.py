# Clases

class MiPersonaVacia: # Se escribe en mayuscula la primera letra de cada palabra y sin "_" por buena practica
    pass # pass sirve para omitir el error que da no darle valores a la clase, funciona tambien en funciones

print(MiPersonaVacia)
print(MiPersonaVacia())

# Las clases tienen algo que se llama constructor, este es capaz de recibir parametros

class MiPersona:
    def __init__(self, nombre, apellido): # Self es obligatorio, se refiere a si mismo
        self.nombre = nombre
        self.apellido = apellido

mi_persona = MiPersona("Cristian", "Camilo")
print(f"{mi_persona.nombre} {mi_persona.apellido}")

mi_persona2 = MiPersona("Juan", "Luis")
print(f"{mi_persona.nombre} {mi_persona.apellido}")
print(f"{mi_persona2.nombre} {mi_persona2.apellido}")

class MiPersona:
    def __init__(self, nombre, apellido):
        self.nombre_completo = f"{nombre} {apellido}"
        self.__nombre = nombre # Pasa a ser Privado, por lo que no es posible acceder directamente
    
    # Para acceder a __nombre se crea una funcion que lo retorne
    def get_name (self):
        return self.__nombre
    
    def caminar (self):
        print(f"{self.nombre_completo} Esta caminando")

mi_persona = MiPersona("Cristian", "Camilo")
print(mi_persona.nombre_completo)
print(mi_persona.get_name())
mi_persona.caminar()

mi_persona.nombre_completo = 3235
print(mi_persona.nombre_completo)

mi_persona.nombre_completo = "Miguel Gonzalez"
print(mi_persona.nombre_completo)