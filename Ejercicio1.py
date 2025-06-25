# Registro de estudiantes

# Menu

lista_estudiantes = list()
diccionario_estudiantes = dict()

while True:
    print("...MENU...")
    print("1. Agregar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Buscar estudiante por nombre")
    print("4. Mostrar estadisticas")
    print("5. Salir")

    try:
        opcion = int(input("Marque el numero de la opcion que desea realizar: "))
        if  opcion == 1:
            estudiante = input("Ingrese el nombre del estudiante: ")
            lista_estudiantes.append(estudiante.lower())

            edad = input("Ingrese su edad: ")
            materia = input("Ingrese su materia: ")

            diccionario_estudiantes[estudiante.lower()] = {"edad":edad, "materia":materia}

            print(lista_estudiantes)
            print(diccionario_estudiantes)
        elif opcion == 2:
            lista_estudiantes.sort()
            print(" ")
            for elementos in lista_estudiantes:
                print(elementos)
                print(diccionario_estudiantes[elementos])
                print(" ")
        elif opcion == 3:
            buscar = input("Ingrese el nombre que desea buscar: ")
            for elementos in lista_estudiantes:
                if buscar.lower() == elementos:
                    print(" ")
                    print(elementos)
                    print(diccionario_estudiantes[elementos])
                    print(" ")
        elif opcion == 5:
            break
        else:
            print("Dato invalido, escoja una opcion valida")
    except ValueError:
        print("Ingrese solo valores numericos")

    


