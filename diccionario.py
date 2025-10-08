precios_frutas = {
    "manzana": 1500,
    "pera": 1000,
    "banano": 700,
    "mango": 1000,
}
def calcular_frutas():

    while True:
        print(f"{"*"*20} Calculadora de frutas {"*"*20}")
        fruta = input("Ingrese fruta: ").lower()
        cantidad = int(input("Ingrese Cantidad: "))

        if fruta in precios_frutas:
            precioUnd = precios_frutas[fruta]
            total = precioUnd * cantidad
            print(f"Total: ${total}")
            {"*"*40}
        else:
            print("La fruta ingresada no existe")
        {"*"*40}
        
        volver = input("¿Quieres hacer otra consulta? (s/n): ")
        if volver.lower() != "s":
            break
    

if __name__ == "__main__":
    calcular_frutas()


    


    


    
