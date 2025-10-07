
def calcular_factura():
    print(f"{'*'*10} calcular iva  {'*'*10}")
    saldo = float(input("Ingrese valor factura sin iva: "))
    iva = input("Ingrese porcentaje iva a cobrar: ")
    
    if iva == "":
        saldo_iva = saldo * 1.21 
    else:
        saldo_iva = saldo * (1 + float(iva) / 100)
    
    print(f"Total de la factura con iva es: {saldo_iva:.3f}")
    print(f"\n{'*'*40}")
    input("\nPresiona Enter para continuar...")
    return saldo_iva
    

if __name__ == "__main__":
    calcular_factura()





