
grupoA = []
grupoB = []

def grupos():
    nombre = input("Ingrese su nombre: ")
    sexo = input("Ingrese su sexo: ")
    primera_letra = nombre[0].upper()

    if primera_letra <= "M" and sexo == "Mujer":
        grupoA.append(nombre)
        print("Perteneces al grupo grupo A")
    elif primera_letra >= "N" and sexo == "Hombre":
        grupoA.append(nombre)
        print("Perteneces al grupo grupo A")

    elif primera_letra >= "M" and sexo == "Mujer":
        grupoB.append(nombre)
        print(f"Perteneces al grupo grupo B")
    elif primera_letra <= "N" and sexo == "Hombre":
        grupoB.append(nombre)
        print("Perteneces al grupo grupo B")

    else:
        print("Ingresa un nombre correcto")
    
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    grupos()

        

