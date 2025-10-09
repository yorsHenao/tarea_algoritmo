def modificar_listas_numeros():
    print(f"\n{"*"*10}Menu de opciones{"*"*10}\n")
    print("1. Agregar un numero a la lista")
    print("2. Eliminar numero de la lista")
    print("3. Insertar un numero en una posición especifica")
    print("4. Ordenar de menor a mayor")
    print("5. De menor a mayor")
    print("6. Eliminar el ultimo elemento")
    print("7. Monstrar Lista")
    print("8. Salir")


def ejecutar_menu():
    numeros = []
    while True:
        modificar_listas_numeros()
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            valor = int(input("Ingresa un valor: "))
            numeros.append(valor)
            print("Numero agregado")
        
        
        elif opcion == "2":
            eliminar = int(input("Cual es el numero a eliminar: "))
            if eliminar in numeros:
                numeros.remove(eliminar)
                print("Numero eliminado")
            else:
                print("Numero no esta en la lista")
        
        elif opcion == "3":
            valor = int(input("Ingresar el numero nuevo: "))
            indice = int(input("Ingrese la posición: "))
            if 0 <= indice <= len(numeros):
                print("Numero guardado")
            else:
                print("Posición invalida")
        
        elif  opcion == "4":
            numeros.sort()
            print("Lista ordenada de menor a mayor")
        
        elif opcion == "5":
            numeros.sort(reverse=True)
            print("Lista de mayor a menor")
        
        elif opcion == "6":

            if numeros:
                eliminado = numeros.pop()
                print(f"el numero eliminado es: {eliminado}")
            else:
                print("Lista vacia")


        elif opcion == "7":
            print(f"Lista actual: {numeros}") 

        elif opcion == "8":
            print("Saliendo del programa.....")
            break

        else:
            print("Opción invalida, intente de nuevo")
        
        if opcion != "8":
            volver = input("¿Quieres volver al menú de listas? (s/n): ")
            if volver.lower() != "s":
                print("Saliendo al menu inicial")
                break

if __name__ == "__main__":
    ejecutar_menu()


