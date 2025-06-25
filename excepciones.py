# Excepciones

# Sirven para el manejo de errores

numero_uno = 5
numero_dos = 4
numero_dos = "4"

# try except
try:
    print(numero_uno + numero_dos)
except:
    print("Se ha producido un error")


# try except else
try:
    print(numero_uno + numero_dos)
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepción
    print("La ejecución continua correctamente")
finally:
    # Se ejecuta siempre
    print("La ejecución continua")


# Excepciones por tipo de error
try:
    print(numero_uno + numero_dos)
except ValueError:
    print("Error de tipo ValueError")
except TypeError:
    # Se ejecuta solo si el error se da por TypeError (Tipo de dato)
    print("Se ha producido un TypeError")


# Captura de la información de la excepción
try:
    print(numero_uno + numero_dos)
    print("No se ha producido un error")
except TypeError as Error: # Captura solo errores del tipo TypeError, "Exception" Captura todos los errores
    print(Error)
except Exception as Error:
    print(Error)
