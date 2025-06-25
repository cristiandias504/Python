# Funciones

def mi_funcion ():
    print("Esto es una función")

mi_funcion()
mi_funcion()

def suma_dos_valores (primer_valor, segundo_valor): #No sirve de nada forzar el tipo de dato "primer_valor: int", no es fuertemente tipado
    print(primer_valor + segundo_valor)

suma_dos_valores(5, 7)
suma_dos_valores(45343, 35343)
suma_dos_valores("dd", "gf")
suma_dos_valores(1.4, 5)


def suma_dos_valores_con_retorno (primer_valor, segundo_valor):
    return primer_valor + segundo_valor


mi_resultado = suma_dos_valores(5, 3) #No cuenta con return
print(mi_resultado) 

mi_resultado = suma_dos_valores_con_retorno(10, 5)
print(mi_resultado)

# Cambiar orden en que se envian los datos

def imprimir_nombre (nombre, apellido):
    print(f"{nombre} {apellido}")

imprimir_nombre("Diaz", "Cristian")
imprimir_nombre(apellido = "Diaz", nombre = "Cristian")

# Dando valores por defecto
def imprimir_nombre (nombre, apellido, alias = "Sin alias"):
    print(f"{nombre} {apellido} {alias}")

imprimir_nombre("Cristian", "Diaz")
imprimir_nombre("Cristian", "Diaz", "El aspero")

# Imprimir varios valores enviados cuando solo esperaba uno
def imprimir_textos (*texto):
    print(texto)

imprimir_textos("Hola")
imprimir_textos("Hola", "Python", "Camilo")