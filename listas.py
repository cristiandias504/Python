#Listas

mi_lista = list() # Es diferente a un Array, ya que permite hacer mas funciones
mi_otra_lista = []

print(mi_lista)
print(len(mi_lista))

mi_lista = [35, 24, 62, 52, 30, 30, 17]
print(mi_lista)
print(len(mi_lista))

mi_otra_lista = [26, 1.77, "Cristian", "Diaz"]
print(mi_otra_lista)

print(type(mi_lista))
print(type(mi_otra_lista))

print(mi_otra_lista[1])
print(mi_otra_lista[-1])


#Cuenta cuantas veces hay un valor en una lista

print(mi_lista.count(30))
print(mi_otra_lista.count("Cristian"))


#Extraer datos de una lista
 
edad, estatura, nombre, apellido = mi_otra_lista
print(edad)

nombre, apellido, edad, estatura = mi_otra_lista[2], mi_otra_lista[3], mi_otra_lista[0], mi_otra_lista[1]
print(nombre)
print(apellido)
print(edad)
print(estatura)


#sumar listas

print(mi_lista + mi_otra_lista)


#Modificar listas

mi_otra_lista.append("Nuevo")
print(mi_otra_lista)

mi_otra_lista.insert(1, "Azul")
print(mi_otra_lista)

mi_otra_lista[1] = "Rojo"
print(mi_otra_lista)

mi_otra_lista.remove("Rojo")
print(mi_otra_lista)

print(mi_lista)
mi_lista.remove(30)
print(mi_lista)

print(mi_lista)
print(mi_lista.pop())
print(mi_lista)

print(mi_lista)
print(mi_lista.pop(2))
print(mi_lista)

del mi_lista[2]
print(mi_lista)


#Copiar una lista

mi_lista_copia = mi_lista.copy()

mi_lista.clear()
print(mi_lista)
print(mi_lista_copia)

mi_lista_copia.reverse()
print(mi_lista_copia)

mi_lista_copia.sort()
print(mi_lista_copia)