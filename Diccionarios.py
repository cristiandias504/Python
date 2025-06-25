#Diccionarios

mi_diccionario = dict()
mi_otro_diccionario = {}

print(type(mi_diccionario))

mi_otro_diccionario = {"Nombre":"Cristian", "Apellido":"Diaz", "edad":26, 1:"Python"}

mi_diccionario = {
    "Nombre":"Cristian",
    "Apellido":"Diaz",
    "Edad":26,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.65
}

print(mi_diccionario)

print(len(mi_otro_diccionario))
print(len(mi_diccionario))

print(mi_diccionario["Nombre"])

mi_diccionario["Nombre"] = "Camilo"
print(mi_diccionario)

mi_diccionario["Calle"] = "Calle 68"
print(mi_diccionario)

del mi_diccionario["Calle"]
print(mi_diccionario)


print("Camilo" in mi_diccionario)
print("Apellido" in mi_diccionario)


print(mi_diccionario.items())
print(mi_diccionario.keys())
print(mi_diccionario.values())


#Inicializar un diccionario sin varoles, son con las llaves
mi_nuevo_diccionario = dict.fromkeys(("Nombre", 1))
print(mi_nuevo_diccionario)

mi_nuevo_diccionario = dict.fromkeys(mi_diccionario)
print(mi_nuevo_diccionario)