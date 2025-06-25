#Tuplas
#Una tupla es inmutable, a diferencia de una lista que si es mutable
#Esto significa que la lista se puede modificar, pero la tupla no se puede modificar

mi_tupla = tuple()
mi_otra_tupla = ()

mi_tupla = (26, 1.65, "Cristian", "Camilo")
print(type(mi_tupla))

mi_otra_tupla = (35, 60, 30)

print(mi_tupla[0])
print(mi_tupla[-1])

print(mi_tupla.count("Cristian"))
print(mi_tupla.index("Camilo"))

#mi_tupla[1] = 1.80 #Error, debido a que no es posible modificarla

mi_suma_tuplas= mi_tupla + mi_otra_tupla
print(mi_suma_tuplas) 
print(mi_suma_tuplas[3:6])


#Convertir una tupla en una lista para modificar un valor

mi_tupla =list(mi_tupla)
print(type(mi_tupla))

mi_tupla.insert(1, "Rojo")
print(mi_tupla)

mi_tupla = tuple(mi_tupla)
print(type(mi_tupla))

del mi_tupla
#print(mi_tupla) #Error, debido a que del elimina por completo la tupa, por lo que ya no existe