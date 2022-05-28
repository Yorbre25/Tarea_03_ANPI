import sympy as sp
import numpy as np

"""
Regla de Boole: Calcula la integral de una función
Entrada:
    f: string de la función a la que sacar la integral
    a: limite inferior de la integral
    b: limite superior de la integral
"""
def reglaDeBoole(f, a, b):
    x = sp.Symbol("x")
    f = sp.simplify(f)
    n = 5;

    h = (b - a)/(n - 1)
    t = np.zeros(n)
    for i in range(n):
        t[i] = a + i*h
    print(t)
    y = get_y(f, t)

    I = 2*(h/45) * (7*y[0] + 32*y[1] + 12*y[2] + 32*y[3] + 7*y[4])
    return I

"""
Evalua todos los elemenos de t en f
Entrada:
    f: función de sympy.
    t: vector de preimágenes.
"""
def get_y(f, t):
    n = t.size
    x = sp.Symbol("x")

    y = np.zeros(n)
    for i in range(n):
        y[i] = f.subs(x, t[i]).evalf()
    print(y)
    return y

f = "cos(x)"
X = reglaDeBoole(f, 2, 5)
print(X)

