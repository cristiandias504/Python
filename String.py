#String

mi_string = "Mi String"
mi_otro_string = "Mi otro String"

print(mi_string + " " + mi_otro_string)

nuevo_string = "Este es un string\ncon salto de linea"
print(nuevo_string)

string_tabulado = "\tEste es un string con tabulación"
print(string_tabulado)

string_scape = "\\tEste es un string \\n escapado" #Con doble barra se anula la funcion del \t y \n
print(string_scape)


#Dar Formato

nombre, apellido, edad = "Cristian" , "Diaz", 26

print("Mi nombre es %s %s y mi edad es %d" %(nombre, apellido, edad))
print("Mi nombre es {} {} y mi edad es {}" .format(nombre, apellido, edad))
print(f"Mi nombre es {nombre} {apellido} y mi edad es {edad}")

#Desempaquetado en caracteres de un String

idioma = "python"

a, b, c, d, e, f = idioma

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)


#División 

recorte_idioma = idioma[1:3]
print(recorte_idioma)

recorte_idioma = idioma[1:]
print(recorte_idioma)

recorte_idioma = idioma[-3] #Inicia de derecha a izquierda restando 
print(recorte_idioma)


#Invertir

invertir_idioma = idioma[::-1]
print(invertir_idioma)


#Funciones

print(idioma.capitalize()) #Pone la primera letra en mayuscula
print(idioma.upper()) #Todo lo pasa a mayuscula
print(idioma.count("t")) #Cuenta cuantas veces esta
print(idioma.isnumeric())
print("1".isnumeric())
print(idioma.capitalize())
print(idioma.lower().isupper()) #Primero lo pasa a nimusculas y luego consulta si es mayuscula
