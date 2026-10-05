notas = []


def pedirNotas():

    while True:

        try:

            nota = int(input("Dime la nota: "))

            if nota < 0 or nota > 100:
                print("La nota debe estar entre 0 y 100.")
            else:
                return nota

        except ValueError:

            print("Error, escriba un numero")


def agregarNota():

    nota = pedirNotas()
    notas.append(nota)

    otra = input("¿Quieres agregar otra nota? (s/n): ")

    if otra.lower() == "s":
        agregarNota()


def guardarNotas():

    archivo = open("notas.txt", "w")

    for nota in notas:
        archivo.write(str(nota) + "\n")

    archivo.close()


def mostrarResultados():

    promedio = sum(notas) / len(notas)
    notaMax = max(notas)
    notaMin = min(notas)

    print("\nResultados:")
    print("Promedio:", promedio)
    print("Nota máxima:", notaMax)
    print("Nota mínima:", notaMin)


agregarNota()
guardarNotas()
mostrarResultados()