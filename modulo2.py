# Funciones

def mi_funcion ():
    print("Esto es una función")

def suma_dos_valores (primer_valor, segundo_valor): #No sirve de nada forzar el tipo de dato "primer_valor: int", no es fuertemente tipado
    print(primer_valor + segundo_valor)

def suma_dos_valores_con_retorno (primer_valor, segundo_valor):
    return primer_valor + segundo_valor

# Cambiar orden en que se envian los datos

def imprimir_nombre (nombre, apellido):
    print(f"{nombre} {apellido}")

# Dando valores por defecto
def imprimir_nombre (nombre, apellido, alias = "Sin alias"):
    print(f"{nombre} {apellido} {alias}")

# Imprimir varios valores enviados cuando solo esperaba uno
def imprimir_textos (*texto):
    print(texto)