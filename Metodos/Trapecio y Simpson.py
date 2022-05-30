import sympy as sp

from maximoDeFuncion import maximos_de_funcion

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
Salida:
    I: valor numerico de la integral
    error: Error maximo del calculo
"""
def trapecio(f, a, b):
    x = sp.Symbol("x")
    f = sp.sympify(f)
    f_a = f.subs(x, a).evalf()
    f_b = f.subs(x, b).evalf()
    #Calcular Integral
    I = ((f_a + f_b))*(b - a)/2

    #Calcular error:
    for i in range(2):
        f = sp.diff(f, x)
    
    c = maximos_de_funcion(f, a, b)
    error = ((b - a)**3/12) * c

    return I,error



"""
Metodo de Simpson: Utiliza un polinomio de grado 2 
para aproximar el area bajo la curva.
Entrada:
    f: string de la función a la que sacar la integral
    a: limite inferior de la integral
    b: limite superior de la integral
Salida:
    I: valor numerico de la integral
    error: Error maximo del calculo
"""
def simpson(f, a, b):
    x = sp.Symbol("x")
    f = sp.sympify(f)
    f_a = f.subs(x, a).evalf()
    f_b = f.subs(x, b).evalf()
    f_medio = f.subs(x, (a + b)/2).evalf()
    I = ((b - a)/6)    *(f_a + 4*f_medio + f_b)

    #Calcular error:
    for i in range(5):
        f = sp.diff(f, x)
    
    c = maximos_de_funcion(f, a, b)
    error = ((b - a)**5/2880) * c

    return I,error

"""
Trapecio compuesto: Para diferentes subintervalo se aplica
el metodo de trapecio.
Entrada:
    f: string de la función a la que sacar la integral
    a: limite inferior de la integral
    b: limite superior de la integral
    m: cantidad de puntos
Salida:
    I: valor numerico de la integral
    error: Error maximo del calculo
"""
def trapecio_compuesto(f, a, b, m):
    x = sp.Symbol("x")
    f = sp.sympify(f)    
    h = (b - a)/(m - 1)
    t = []
    for i in range(m):
        t.append(a + i*h)
    # print(t)

    I = 0
    error = 0
    #Calcular la integral
    for j in range(len(t) - 1):
        sol = trapecio(f, t[j], t[j + 1])
        I += sol[0]
        error += sol[1]

    return I,error

"""
Simpson compuesto: Para diferentes subintervalo se aplica
el metodo de simpson.
Entrada:
    f: string de la función a la que sacar la integral
    a: limite inferior de la integral
    b: limite superior de la integral
    m: cantidad de puntos
Salida:
    I: valor numerico de la integral
    error: Error maximo del calculo
"""
def simpson_compuesto(f, a, b, m):
    x = sp.Symbol("x")
    f = sp.sympify(f)    
    h = (b - a)/(m - 1)
    preima = []
    for i in range(m):
        preima.append(a + i*h)
    
    I = 0
    error = 0
    for j in range(len(preima) - 1):
        sol = simpson(f, preima[j], preima[j + 1])
        I += sol[0]
        error += sol[1]
    # print(I)
    return I, error

# f = "exp(x)"
# f = "cos(x)"
# f = "atan(x)"
# a = -2
# b = 1
# X = trapecio(f, a, b)
# print(X)
# X = simpson(f, a, b)
# print(X)
# X = trapecio_compuesto(f, a, b, 5)
# print(X)
# X = simpson_compuesto(f, a, b, 5)
# print(X)
