#Condicionales

mi_condicional = False

if mi_condicional:  # Es igual a if mi_condicional == True:
    print("se ejecuta la condicion del if")

mi_condicional = 5 * 2

if mi_condicional == 11:
    print("se ejecuta la condicion del Segundo if")

if mi_condicional >= 10:
    print("Se ejecuta la condicional del tercer if")

if mi_condicional > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual a 10")
if mi_condicional > 10 and mi_condicional < 20:
    print("Es mayor que 10 y menor que 20")
else:
    print("Es menor o igual a 10 o mayor o igual a 20")

if mi_condicional < 10:
    print("Es menor a 10")
elif mi_condicional >= 10 and mi_condicional < 20:
    print("Es mayor o igual a 10 y menor a 20")
else:
    print("Es mayor o igual a 20")
    
print("La ejecucion continua")


mi_string = ""

if mi_string:
    print("Mi cadena de texto no es vacia")

if not mi_string:
    print("Mi cadena de texto es vacia")

if mi_string == "Hola":
    print("Estas cadenas de texto coinciden")

