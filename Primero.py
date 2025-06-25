variable_int = 5
print(variable_int)

variable_int_a_str = str(variable_int)
print(variable_int_a_str)

variable_str = "10"
variable_str_a_int = int(variable_str)
print(type(variable_str_a_int), variable_str_a_int)

print(type(variable_int), "Valor de la suma int=", variable_int + variable_int)
print(type(variable_int_a_str), "Valor de la suma str=", variable_int_a_str + variable_int_a_str)

print(type(print(5))) # Tipo NoneType, esto debido a que print no es un dato, es una función


#Funciones del sistema
print(len(variable_int_a_str)) # Cuenta la longitud de la cadena
print(len(variable_str))


#Definir varias variables en una sola linea
nombre, apellido, edad = "Cristian", "Camilo", 26
print("Mi nombre es", nombre, "mi apellido es", apellido, "y mi edad es", edad, "años")


#Ingresar datos desde la terminal
primer_nombre = input("¿Cual es tu nombre? ")
edad = input("¿Cual es tu edad? ")

print("Tu nombre es", primer_nombre, "y tu edad es", edad, "años")


#Cambiar el tipo de una variable
nombre = 45
edad = "Cristian"
print(type(nombre), nombre)
print(type(edad), edad)

"""
Esto es posible por que Python es un lenguaje de tipado debil,
a diferencia de otros lenguajes de tipado fuerte.
"""