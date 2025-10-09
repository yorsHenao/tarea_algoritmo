
grupoA = []
grupoB = []

def grupos():
    print(f"{"*"*20}GRUPO A Y GRUPO B{"*"*20}")
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo: ").upper()
    primera_letra = nombre[0].upper()

    if primera_letra <= "M" and sexo == "MUJER":
        grupoA.append(nombre)
        print("Perteneces al grupo grupo A")
    elif primera_letra >= "N" and sexo == "HOMBRE":
        grupoA.append(nombre)
        print("Perteneces al grupo grupo A")

    elif primera_letra >= "M" and sexo == "MUJER":
        grupoB.append(nombre)
        print(f"Perteneces al grupo grupo B")
    elif primera_letra <= "N" and sexo == "HOMBRE":
        grupoB.append(nombre)
        print("Perteneces al grupo grupo B")

    else:
        print("Ingresa un nombre correcto")
    
    
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    grupos()

        

