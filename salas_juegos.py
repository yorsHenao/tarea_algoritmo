

def edad ():
     print(f"{'*'*10} Casino {'*'*10}\n")
     cliente = int(input("Ingrese su edad: "))

     if cliente < 4:
          print("Entrada gratis")
     elif cliente >= 4 and cliente <= 18:
        print("Valor de entrada 30.000")
     else:
         print("Valor entrada 50.000")
     print(f"\n{'*'*14}{'*'*14}\n")
     input("\nPresiona Enter para continuar...")


if __name__ == "__main__":
    edad()
