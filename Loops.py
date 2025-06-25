# Loops

# While

mi_condicion = 0

while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 2
else:
    print("Mi condicion es mayor o igual a 10")

print("La ejecución continúa")

while mi_condicion < 20:
    mi_condicion += 1
    if mi_condicion == 15:
        print("Mi condicion es 15")
        break
    print(mi_condicion)
print("La ejecución continua")


# For

mi_lista = [35, 24, 62, 52, 30, 30, 17]

for element in mi_lista:
    print(element)

mi_tupla = (26, 1.77, "Cristian", "Camilo", 1)

for element in mi_tupla:
    print(element)
else:
    print("El bucle for para mi diccionario a terminado")

for element in mi_tupla:
    print(element)
    if element == "Cristian":
        break
