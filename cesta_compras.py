
def crearArticulo ():
    cesta = {}
    print(f"{"*"*10}Productos{"*"*10}")
    print("Escribir fin para salir\n")
    #bucle para crear articulo - si el articulo se llama salir, lo terminamos
    while True:
        articulo = input("Articulo: ")
        if articulo.lower() == "fin":
            break

        precio = float(input("Precio: "))
        cesta[articulo] = precio
    return cesta


def guardar_compra(cesta):
    print(f"{"*"*10}Lista de compras{"*"*10}")
    for articulo, precio in cesta.items():
        print(f"{articulo}\t {precio:,.0f}".replace(",","."))

    total = sum(cesta.values())
    print(f"Total: ${total:,.0f}".replace(",","."))
    print("*"*40)
    

if __name__ == "__main__":
    
    mi_cesta = crearArticulo()
    guardar_compra(mi_cesta)
