def restaMatrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        print("Error: Las matrices deben tener las mismas dimensiones")
        return None

    resultado = []

    for i in range(len(matriz1)):
        filaResultado = []
        for x in range(len(matriz1[0])):
            resta = matriz1[i][x] - matriz2[i][x]
            filaResultado.append(resta)
        resultado.append(filaResultado)

    return resultado

def main():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    print("Ingrese los numeros de la primera matriz:")
    matriz1 = []
    for i in range(filas):
        fila = []
        for x in range(columnas):
            numeros = int(input(f"Ingrese los numeros [{i}][{x}]: "))
            fila.append(numeros)
        matriz1.append(fila)
    print("Ingrese los numeros de la segunda matriz:")
    matriz2 = []
    for i in range(filas):
        fila = []
        for x in range(columnas):
            numeros = int(input(f"Ingrese los numeros [{i}][{x}]: "))
            fila.append(numeros)
        matriz2.append(fila)
    resultado = restaMatrices(matriz1, matriz2)
    if resultado is not None:
        print("Resultado de la resta de las matrices:")
        for fila in resultado:
            print(fila)

if __name__ == "__main__":
    main()