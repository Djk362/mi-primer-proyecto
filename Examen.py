def suma_vectores(v1, v2):
    return [a + b for a, b in zip(v1, v2)]

def producto_vectores(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))

def producto_vectorial(v1, v2):
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("El producto vectorial no está definido para vectores en las 3 dimensiones ps.")
    return [
        v1[1]*v2[2] - v1[2]*v2[1],
        v1[2]*v2[0] - v1[0]*v2[2],
        v1[0]*v2[1] - v1[1]*v2[0]
    ]

def leer_vector(n):
    return [float(x) for x in input(f"Ingrese {n} componentes separadas por espacio muchacho: ").split()]

def main():
    print("Funciones disponibles:")
    print("1. Suma de vectores n-dimensionales")
    print("2. Producto punto de vectores n-dimensionales")
    print("3. Producto vectorial (solo 3 dimensiones)")
    opcion = input("Elija una opción (1/2/3): ")

    if opcion in ("1", "2"):
        n = int(input("Ingrese la dimensión de los vectores joven: "))
        print("Vector 1:")
        v1 = leer_vector(n)
        print("Vector 2:")
        v2 = leer_vector(n)
        if opcion == "1":
            resultado = suma_vectores(v1, v2)
            print("Suma de vectores:", resultado)
        else:
            resultado = producto_vectores(v1, v2)
            print("Producto punto:", resultado)
    elif opcion == "3":
        print("Vector 1 (3 dimensiones):")
        v1 = leer_vector(3)
        print("Vector 2 (3 dimensiones):")
        v2 = leer_vector(3)
        resultado = producto_vectorial(v1, v2)
        print("Producto vectorial:", resultado)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()