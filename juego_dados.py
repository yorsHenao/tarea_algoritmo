import random

def dados():
    return random.randint(1,6)

jugadores = ["Álbaro", "Barbara"]


def tirar_dados():
    print(f"{'*'*10}Juego de dados{'*'*10}\n")

    input(f"{jugadores[0]} presione enter para tirar dado.")
    dado1 = dados()
    print(f"{jugadores[0]} sacó: {dado1}\n")

    input(f"{jugadores[1]} presione enter para tirar dado.")
    dado2 = dados()
    print(f"{jugadores[1]} sacó: {dado2}\n")

    if dado1 > dado2:
        print("Gana Álbaro")
    elif dado2 > dado1:
        print("Gana Barbara")
    else:
        print("Empate")
    
    print(f"{'*'*10}Fin del juego{'*'*10}\n")

    input("\nPresiona Enter para continuar...")
    

if __name__ == "__main__":
    tirar_dados()




    
   
