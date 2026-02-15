def leer_matriz(nombre_archivo):
    matriz = []
    with open(nombre_archivo, 'r') as f:
        for linea in f:
            if linea.strip():
                fila = [float(x) for x in linea.strip().split()]
                matriz.append(fila)
    return matriz

def lu_nxn(A):
    n = len(A)
    L = [[0.0]*n for _ in range(n)]
    U = [[0.0]*n for _ in range(n)]
    for i in range(n):
        L[i][i] = 1.0
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k]*U[k][j] for k in range(i))
        for j in range(i+1, n):
            if U[i][i] == 0:
                raise ValueError("Cero en la diagonal, no se puede continuar sin pivoteo.")
            L[j][i] = (A[j][i] - sum(L[j][k]*U[k][i] for k in range(i))) / U[i][i]
    return L, U

A = leer_matriz("matriz.txt")

L, U = lu_nxn(A)

print("Matriz L:")
for fila in L:
    print(fila)
print("\nMatriz U:")
for fila in U:
    print(fila)