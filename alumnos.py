def alumnos():
    estudiante={}
    print(f"{"*"*20}ESTUDIANTES{"*"*20}\n")
    nombre = input("Estudiante: ")

    materias = []
    notas = []

    
    print("\nIngrese 3 materias")
    for m in range(3):
        materia = input("Materia: ")
        materias.append(materia)
    
    print("\nIngrese nota de cada materia")
    for materia in materias:
        nota = input(f"Nota de {materia}: ")
        notas.append(nota)
    
    estudiante[nombre] = [materias, notas]

    print("\n estudiantes:")
    print(estudiante)
    print(f"\{"*"*60}\n")


if __name__ == "__main__":
    alumnos()
