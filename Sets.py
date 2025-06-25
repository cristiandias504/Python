#Set
#Puede ser mas rapido, al no permitir repetidos, y manipular puede ser mas rapido gracias a su
#estructura interna para organizar los datos

mi_set = set()
mi_otro_set = {}

print(type(mi_set))
print(type(mi_otro_set)) # Inicialmente dice que es un diccionario

mi_otro_set = {"Cristian", "Camilo", 26}
print(type(mi_otro_set))

print(len(mi_otro_set))

mi_otro_set.add("Diaz")
print(mi_otro_set) # No es una estructura ordenada

mi_otro_set.add("Diaz")
print(mi_otro_set) # No admite valores repetidos

print("Camilo" in mi_otro_set)

mi_otro_set.remove("Camilo")
print(mi_otro_set)

mi_otro_set.clear()
print(len(mi_otro_set))

mi_set = {"Cristian", "Camilo", 26}
mi_otro_set = {"Rojo", "Verde", 30}

mi_nuevo_set = mi_set.union(mi_otro_set)
print(mi_nuevo_set)

print(mi_nuevo_set.difference(mi_set))