from juego_dados import tirar_dados
from nombre_y_sexo import grupos
from salas_juegos import edad
from contraseña import privacidad
from iva import calcular_factura
from Metodos import ejecutar_menu
from diccionario import calcular_frutas




def volver_al_menu():
    input("\nPreciosa Enter para volver al menú.")

def mostrar_menu():
    print("Menu")
    print("1. Juego dados:")
    print("2. Nombre y sexo")
    print("3. Casino")
    print("4. Contraseña")
    print("5. Facturas")
    print("6. Posición de numeros en listas")
    print("7. precios frutas")
    print("8. Crear diccionario ")
    print("9. Alumnos ")
    print("10. Salir")

def menu ():
    while True:
        mostrar_menu()
        opcion  = input("Ingrese una opción: ")
        
        if opcion == "1":
            tirar_dados()
        
        elif opcion == "2":
            grupos()

        elif opcion == "3":
            edad()

        elif opcion == "4":
            privacidad()
        
        elif opcion == "5":
            calcular_factura()
        
        elif opcion == "6":
            ejecutar_menu()
        
        elif opcion == "7":
            calcular_frutas()
        
        elif opcion == "8":
            print("Crear diccionario")
        
        elif opcion == "9":
            print("Alumnos")
        
        elif opcion =="10":
            print("Hasta luego")
            break
        
        else: 
            print("Opción invalida")
        
        volver = input("¿Quieres volver al menú? (s/n): ")
        if volver != "s":
            print("Programa finalizado")
            break


if __name__ == "__main__":
    menu()


        


