from re import I
import sympy as sp

"""
* INTEGRACIÓN NUMÉRICA
"""
"""
Metodo del trapecio: Utiliza un polinomio de grado 1
para aproximar el area debajo de la curva.
Entrada:
    f: string de la función a la que sacar la integral
    a: limite inferior de la integral
    b: limite superior de la integral
"""
def trapecio(f, a, b):
    x = sp.Symbol("x")
    f = sp.sympify(f)
    f_a = f.subs(x, a).evalf()
    f_b = f.subs(x, b).evalf()
    I = ((f_a + f_b))*(b - a)/2
    return I
"""
Metodo de Simpson: Utiliza un polinomio de grado 2 
para aproximar el area bajo la curva.
Entrada:
    f: string de la función a la que sacar la integral
    a: limite inferior de la integral
    b: limite superior de la integral
"""
def simpson(f, a, b):
    x = sp.Symbol("x")
    f = sp.sympify(f)
    f_a = f.subs(x, a).evalf()
    f_b = f.subs(x, b).evalf()
    f_medio = f.subs(x, (a + b)/2).evalf()
    I = ((b - a)/6)    *(f_a + 4*f_medio + f_b)
    return I

"""
Trapecio compuesto: Para diferentes subintervalo se aplica
el metodo de trapecio.
Entrada:
    f: string de la función a la que sacar la integral
    a: limite inferior de la integral
    b: limite superior de la integral
    m: cantidad de puntos
"""
def trapecio_compuesto(f, a, b, m):
    x = sp.Symbol("x")
    f = sp.sympify(f)    
    h = (b - a)/(m - 1)
    preima = []
    for i in range(m):
        preima.append(a + i*h)
    
    I = 0
    for j in range(len(preima) - 1):
        I += trapecio(f, preima[j], preima[j + 1])
    # print(I)
    return I

"""
Simpson compuesto: Para diferentes subintervalo se aplica
el metodo de simpson.
Entrada:
    f: string de la función a la que sacar la integral
    a: limite inferior de la integral
    b: limite superior de la integral
    m: cantidad de puntos
"""
def simpson_compuesto(f, a, b, m):
    x = sp.Symbol("x")
    f = sp.sympify(f)    
    h = (b - a)/(m - 1)
    preima = []
    for i in range(m):
        preima.append(a + i*h)
    
    I = 0
    for j in range(len(preima) - 1):
        I += simpson(f, preima[j], preima[j + 1])
    # print(I)
    return I

# f = "exp(x)"
# X = trapecio(f, 0, 1)
# print(X)
# X = simpson(f, 0, 1)
# print(X)
# trapecio_compuesto(f, 0, 1, 5)
# simpson_compuesto(f, 0, 1, 5)
