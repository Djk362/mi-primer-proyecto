def gauss3x3(A, b):
    #empezamos con laa eliminaciion hacia adelante
    n = 3
    for i in range(n):
        #hacemos un pivoteo parcial simple, sirve para la eliminacion gaussiana
        max_row = max(range(i, n), key=lambda r: abs(A[r][i]))
        if i != max_row:
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]
            #eliminacion
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]
            #hacemos una sustitucion hacia atras
    x = [0]*n
    for i in reversed(range(n)):
        x[i] = (b[i] - sum(A[i][j]*x[j] for j in range(i+1, n))) / A[i][i]
    return x
A = [
    [-5, -2, -4],
    [-5, -3, 3],
    [4, 1, 4]
]
b = [6, -2, 1]
sol = gauss3x3([row[:] for row in A], b[:]) 
#si esta bien deberia arrojar los valores a,b y c. Lo intente en python puro pero a veces me marca error
print(f"a = {sol[0]}")
print(f"b = {sol[1]}")
print(f"c = {sol[2]}")