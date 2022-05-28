import sunau
import sympy as sp
from sympy import S, Interval

"""
Verifica si el intervalo de entrada es continuo para la función de entrada
    Entrada:
        f: string de la función
        a: limite inferior de la integral
        b: limite superior de la integral
"""
def checkInverval(f, a, b):
    inter = Interval(a, b).boundary
    f = sp.simplify(f)
    x = sp.Symbol("x")

    # Intervalos continuos de la función
    I = sp.calculus.util.continuous_domain(f, x, S.Reals)

    esContinuo = False
    for subset in I.args: 
        #Para cada intervalo continuo, verificar si 
        # el intervalo de entrada es subintervalo de subset
        esContinuo = inter.is_subset(subset)
        if esContinuo:
            break
    
    return esContinuo

f = "1/(x-5)"
checkInverval(f, 2, 3)