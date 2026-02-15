def f1(x):
    return x**3 - x**2 - 1

def f2(x):
    return x**2 - 5

def metodo_grafico(func, x_start, x_end, paso):
    print("\nTabla de valores para el método gráfico:")
    print(" x\t|\tf(x)")
    print("----------------------")
    x = x_start
    while x <= x_end:
        print(f"{x:.2f}\t|\t{func(x):.5f}")
        x += paso

def biseccion(func, a, b, tol=1e-5, max_iter=100):
    if func(a) * func(b) >= 0:
        print("No se puede aplicar el método de bisección. f(a) y f(b) deben tener signos opuestos.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        fc = func(c)

        print(f"Iteración {i+1}: a={a:.5f}, b={b:.5f}, c={c:.5f}, f(c)={fc:.5f}")

        if abs(fc) < tol or (b - a) / 2 < tol:
            print(f"Raíz encontrada: {c:.5f}")
            return c

        if func(a) * fc < 0:
            b = c
        else:
            a = c

    print("Máximo de iteraciones alcanzado.")
    return (a + b) / 2

print("Función f1(x) = x^3 - x^2 - 1")
metodo_grafico(f1, x_start=1.0, x_end=2.0, paso=0.1)
biseccion(f1, a=1.0, b=2.0)

print("\nFunción f2(x) = x^2 - 5")
metodo_grafico(f2, x_start=2.0, x_end=3.0, paso=0.1)
biseccion(f2, a=2.0, b=3.0)
