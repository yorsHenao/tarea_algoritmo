import getpass


def privacidad():
    print(f"{'*'*10} Guardado contraseña {'*'*10}")
    contraseña = getpass.getpass("Introduce tu contraseña: ")

    while True:
        print(f"\n ingresa tu contraseña guardada \n")
        contraseña_user = getpass.getpass("Introduce tu contraseña: ")

        if contraseña_user == contraseña:
            print("Contraseña correcta")
            break
        else:
            print("Contraseña erronea. Intentelo de nuevo")
    print(f"\n{'*'*40}")
    input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    privacidad()


