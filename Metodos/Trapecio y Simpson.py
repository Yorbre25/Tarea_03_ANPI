from sympy.calculus.util import continuous_domain
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
TODO: calcular error
"""
def trapecio_compuesto(f, a, b, m):
    x = sp.Symbol("x")
    f = sp.sympify(f)    
    h = (b - a)/(m - 1)
    preima = []
    for i in range(m):
        preima.append(a + i*h)
    
    I = 0
    #Calcular la integral
    for j in range(len(preima) - 1):
        I += trapecio(f, preima[j], preima[j + 1])
    return I

"""
Simpson compuesto: Para diferentes subintervalo se aplica
el metodo de simpson.
Entrada:
    f: string de la función a la que sacar la integral
    a: limite inferior de la integral
    b: limite superior de la integral
    m: cantidad de puntos
TODO: calcular error
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

"""
Devuelve el valor mas alto que puede tomar la función f
en el intervalo de entrda.
Entrada:
    f: string de la funcion
    a: limite inferior
    b: limite superior
Salida:
    mayor: valor maximo
"""
def maximos_de_funcion(f, a, b):
    f = sp.simplify(f)
    x = sp.Symbol("x")
    #Calcular puntos críticos
    f_der = sp.diff(f, x)
    
    #Donde la derivada de f se hace 0
    pts_crt = sp.solve(sp.Eq(f_der, 0))
    
    #Donde la derivada de f se indefine pero f no
    f_domain = continuous_domain(f, x, sp.S.Reals )
    deriv_domain = continuous_domain(f_der, x, sp.S.Reals )
    mas_pts = sp.Complement( f_domain, deriv_domain)
    for value in mas_pts.args:
        pts_crt.append(value)
    print(pts_crt)
    
    #Pasar los valore sa numerico
    aux_lst = pts_crt.copy()
    for i in range(len(aux_lst)):
        pts_crt[i] = aux_lst[i].evalf()

    #Agregar extremos
    pts_crt.append(a)
    pts_crt.append(b)

    #Evaluar los puntos en f
    f_eval = []
    aux_lst = pts_crt.copy()
    for i in range(len(aux_lst)):
        value = f.subs(x, aux_lst[i]).evalf() #evaluar en f
        if value.is_real: # Si es real se agrega
            f_eval.append( abs(f.subs(x, aux_lst[i]).evalf()) )
            continue
        else: #Si no es real se elimina como candidato
            pts_crt.pop(i)
    

    maximo = max(f_eval)
    # print(maximo)
    return maximo

f = "exp(x)"
# f = "sqrt( x - 1 ) - x"
# X = trapecio(f, 0, 1)
# print(X)
X = simpson(f, 0, 1)
print(X)
# trapecio_compuesto(f, 0, 1, 5)
# simpson_compuesto(f, 0, 1, 5)
