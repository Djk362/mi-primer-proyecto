import math

def f(t):
    return t 

def laplace_transform(f, s, t_max=100, dt=0.01):
    integral = 0.0
    t = 0.0
    while t < t_max:
        integral += f(t) * math.exp(-s * t) * dt
        t += dt
    return integral
s = 1.0
resultado = laplace_transform(f, s)
print(f"Transformada de Laplace de f(t)=t en s={s}: {resultado}")