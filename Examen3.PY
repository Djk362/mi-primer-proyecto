import math
import random

l = 10.0
N = 1000000

def vertices_triangulo(x0):
    h = l * math.sqrt(3) / 2
    v1 = [x0, 0, -l/2]
    v2 = [x0, l/2, l/2]
    v3 = [x0, -l/2, l/2]
    return v1, v2, v3

def punto_en_triangulo(P, A, B, C):
    def sub(u, v): return [u[i] - v[i] for i in range(3)]
    def dot(u, v): return sum(u[i]*v[i] for i in range(3))
    v0 = sub(C, A)
    v1 = sub(B, A)
    v2 = sub(P, A)
    d00 = dot(v0, v0)
    d01 = dot(v0, v1)
    d11 = dot(v1, v1)
    d20 = dot(v2, v0)
    d21 = dot(v2, v1)
    denom = d00 * d11 - d01 * d01
    if denom == 0:
        return False
    v = (d11 * d20 - d01 * d21) / denom
    w = (d00 * d21 - d01 * d20) / denom
    u = 1 - v - w
    return (u >= 0) and (v >= 0) and (w >= 0)

def direccion_isotropica():
    theta = math.acos(1 - 2 * random.random())
    phi = 2 * math.pi * random.random()
    x = math.sin(theta) * math.cos(phi)
    y = math.sin(theta) * math.sin(phi)
    z = math.cos(theta)
    return [x, y, z]

def simula(x0):
    A, B, C = vertices_triangulo(x0)
    cuenta = 0
    for _ in range(N):
        d = direccion_isotropica()
        if d[0] <= 0:
            continue
        t = (x0) / d[0]
        y = d[1] * t
        z = d[2] * t
        P = [x0, y, z]
        if punto_en_triangulo(P, A, B, C):
            cuenta += 1
    return 100 * cuenta / N

for x0 in [10, 30, 50]:
    porcentaje = simula(x0)
    print(f"Porcentaje de partículas que alcanzan el triángulo en x={x0} cm: {porcentaje:.4f}%")