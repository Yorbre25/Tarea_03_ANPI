import numpy
import sympy as sp
import numpy as np
import math

from maximoDeFuncion import maximos_de_funcion

"""
Metodo cuadratrura gaussiana: Integración numérica.
"""


"""
Cuadratura Gaussiana General: Antes de llamar la función cuadratura gaussiana
covierte la función de entrada para que calce en el intervalo [-1,1]
    Entrada:
        f: Función 
        a: límite inferior
        b: límite superior
        n: grado del polinomio de Legendre
    Salida:
        Integral de la función
"""
def cuadratura_gaussiana_general(f, a, b, n):
    x = sp.Symbol("x")
    f = sp.simplify(f)
    g = (b-a)/2 * f.subs(x,((b-a)*x+b+a)/2)
    # print(g)
    return cuadratura_gaussiana(g, n)



"""
Cuadraturas Gaussianas: Se calcula la integral de una función,
utilizando un polinomio de Legendre. La integral debe ser desde el 
intervalo -1 a 1
Entrada:
    f: Función 
    n: grado del polinomio de Legendre
Salida:
    Integral de la función
TODO: calcular error
"""
def cuadratura_gaussiana(f, n):
    #Ceros del polinomio
    resul = ceros_pol_legendre(n)
    xv = resul[0]
    xv = np.array(xv)
    p = resul[1]
    #Calcular las w
    w = get_w(xv, p)

    x = sp.Symbol("x")
    f = sp.sympify(f)
    I = 0
    #Calcular la integral (I = w0*f(x0) + w1*f(x1)+...)
    for i in range(n):
        I += w[i]*f.subs(x,xv[i]).evalf()

    #Calcular error:
    for i in range(2*n):
        f = sp.diff(f, x)
    
    c = maximos_de_funcion(f, -1, 1)
    error = c/math.factorial(2*n)

    return I,error


def ceros_pol_legendre(n):
    x = sp.Symbol("x")
    q = sp.diff((x**2 - 1)**n, x, n)
    #print(q)
    p = (1/(math.factorial(n) * 2**n ) * q)
    xv = sp.solve(p)
    return xv,p

def get_w(xv, p):
    x = sp.Symbol("x")
    n = xv.size
    pd = sp.diff(p, x)
    pf_n = np.zeros(n)
    for i in range(n):
        pf_n[i] = pd.subs(x,xv[i]).evalf()
    w = 2/((1-xv**2)*(pf_n**2))
    return w


""""
f = "atan(x)"
n = 3
# I = cuadratura_gaussiana(f, n)
X = cuadratura_gaussiana_general(f, 2, 4, n)
print(X)
"""