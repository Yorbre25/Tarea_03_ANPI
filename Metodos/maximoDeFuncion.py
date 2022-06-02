from sympy.calculus.util import continuous_domain
import sympy as sp

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
    # print(pts_crt)
    
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