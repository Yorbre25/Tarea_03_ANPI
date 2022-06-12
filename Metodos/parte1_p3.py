from operator import ge
from tkinter import *
import tkinter.font as font
import CheckContinuidad as ck
import maximoDeFuncion as mxF
import CuadraturasGaussianas as cg
import Trapecio_y_Simpson as ts
import ReglaDeBoole as RB
import sys, os
import traceback
from sympy import *

dirname = os.path.dirname(__file__)
imagen = os.path.join(dirname, 'inte.png')



width=400
height=500


#los Constructores del GUI
root = Tk()
root.resizable(width=False, height=False) # prevents resizing window

canvas = Canvas(root, width=width, height=height-20)
canvas.configure(bd=0, highlightthickness=0)
canvas.pack()
pixelVirtual = PhotoImage(width=1, height=1)
met_inter = IntVar()
tipgra = font.Font(family='Franklin Gothic Book',size=10)





def simpleAcompuesto():
    lb_pau.place_forget()
    ent_pts.place_forget()
    r_Tr['text'] = 'Trapecio'
    r_Sm['text'] = 'Simpson'
    r_Bl['text'] = 'Regla de Boole'
    r_Tr['value'] = 1
    r_Sm['value'] = 2
    r_Bl['value'] = 3
    

def compuestoAsimple():
    lb_pau.place(x=230, y=250)
    ent_pts.place(x=270, y=270)
    r_Tr['text'] = 'Trapecio Compuesto'
    r_Sm['text'] = 'Simpson Compuesto'
    r_Bl['text'] = 'Cuadraturas Gausianas'
    r_Tr['value'] = 4
    r_Sm['value'] = 5
    r_Bl['value'] = 6

def revisarFuncion(expre):
        
        x = symbols('x')
        exp = expre
        expn= sympify(exp)
        f=lambdify(x, expn)
        f(3.14)
        return true

    
    

def calcular():
    ent_Aprox.config(state= "normal")
    ent_Err.config(state= "normal")
    ent_Aprox.delete(0, END)
    ent_Err.delete(0, END)
    try:
        a= float(ent_aEq.get())
        b= float(ent_bEq.get())
        fun_X= ent_fx.get()
        rfx=revisarFuncion(fun_X)
        metodo=int(met_inter.get())
        ck_inter= ck.checkInverval(fun_X,a,b)
        pts=int(ent_pts.get())
        inver=(-1, 1)[a<b]
        if not(rfx):
            ent_Aprox.insert(0,"0")
            ent_Err.insert(0,"Funcion mal escrita")
        if not(ck_inter):
            ent_Aprox.insert(0,"0")
            ent_Err.insert(0,"Funcion discontinua")
        
        elif a==b:
            ent_Aprox.insert(0,"0")
            ent_Err.insert(0,"Error de sintaxis a = b")
        
        elif metodo==0:
            ent_Aprox.insert(0,"0")
            ent_Err.insert(0,"Seleccione un metodo")
        
        elif metodo==1:#trapecio
            if a<b:
                resultado=ts.trapecio(fun_X,a,b)
            else:
                resultado=ts.trapecio(fun_X,b,a)
            ent_Aprox.insert(0,resultado[0]*inver)
            ent_Err.insert(0,resultado[1])
        
        elif metodo==2:#simpson
            if a<b:
                resultado=ts.simpson(fun_X,a,b)
            else:
                resultado=ts.simpson(fun_X,b,a)
            ent_Aprox.insert(0,resultado[0]*inver)
            ent_Err.insert(0,resultado[1])
        
        elif metodo==3:#Regla_boole
            if a<b:
                resultado=RB.reglaDeBoole(fun_X,a,b)
            else:
                resultado=RB.reglaDeBoole(fun_X,b,a)
            ent_Aprox.insert(0,resultado[0]*inver)
            ent_Err.insert(0,resultado[1])
        
        elif metodo==4:#trapecio_compuesto
            if a<b:
                resultado=ts.trapecio_compuesto(fun_X,a,b,pts)
            else:
                resultado=ts.trapecio_compuesto(fun_X,b,a,pts)
            ent_Aprox.insert(0,resultado[0]*inver)
            ent_Err.insert(0,resultado[1])
        
        elif metodo==5:#simpson_compuesto
            if a<b:
                resultado=ts.simpson_compuesto(fun_X,a,b,pts)
            else:
                resultado=ts.simpson_compuesto(fun_X,b,a,pts)
            ent_Aprox.insert(0,resultado[0]*inver)
            ent_Err.insert(0,resultado[1])
        
        elif metodo==6:#Cuadraturas gaussianas
            if a<b:
                resultado=cg.cuadratura_gaussiana_general(fun_X,a,b,pts)
            else:
                resultado=cg.cuadratura_gaussiana_general(fun_X,b,a,pts)
            ent_Aprox.insert(0,resultado[0]*inver)
            ent_Err.insert(0,resultado[1])
    
    except ValueError:
        ent_Aprox.insert(0,"0")
        ent_Err.insert(0,"Ingresar valores numericos")
        
    except TypeError:
        ent_Aprox.insert(0,"0")
        ent_Err.insert(0,"Ingresar valores numericos2")
    except ZeroDivisionError:
        ent_Aprox.insert(0,"0")
        ent_Err.insert(0,"Numero de puntos < 1")

    except NameError:
        ent_Aprox.insert(0,"0")
        ent_Err.insert(0,"Error en escritura de la funcion")

    except:
        #debug
        #print(traceback.format_exc())
        ent_Aprox.insert(0,"0")
        ent_Err.insert(0,"Error general")
    
        

    ent_Aprox.config(state= "disabled")
    ent_Err.config(state= "disabled")







#contenido gui

lb_Titulo = Label(canvas,
                text="Calculadora de Integrales Definidas",font=tipgra
                    ).place(x=100, y=2)

img = PhotoImage(file=imagen)
Label(
    canvas,
    image=img
).place(x=150,y=30)

lb_fx = Label(canvas, font=tipgra,
            text="f(x)=",)

lb_fx.place(x=100, y=110)

ent_fx = Entry(canvas,font=tipgra)

ent_fx.place(x=140, y=110)
lb_aEq = Label(canvas,font=tipgra,
                text="a=")
lb_aEq.place(x=100, y=150)

ent_aEq = Entry(canvas ,font=tipgra,width = 5)
ent_aEq.place(x=130, y=150)

lb_bEq = Label(canvas,font=tipgra,text="b=")
lb_bEq.place(x=200, y=150)

ent_bEq = Entry(canvas,font=tipgra,width = 5)
ent_bEq.place(x=230, y=150)

btn_MSimpl = Button(canvas,
               text="Métodos simples",
               image=pixelVirtual,
               command=simpleAcompuesto ,
               height = 20,
               width = 130,
               font=tipgra,
               compound="c").place(x=50, y=200)

btn_MComp = Button(root,
               text="Métodos compuesto",
               image=pixelVirtual,
               command=compuestoAsimple,
               height = 20,
               font=tipgra,
               width = 150,
               compound="c").place(x=200, y=200)



r_Tr = Radiobutton(canvas,
                 font=tipgra,
                 text="Trapecio",
                 variable=met_inter,
                 value=1,
                 command="")
r_Tr.place(x=65, y=230)

r_Sm = Radiobutton(canvas,
                 font=tipgra,
                 text="Simpson",
                 variable=met_inter,
                 value=2,
                 command="")
r_Sm.place(x=65, y=260)

r_Bl = Radiobutton(canvas,
                 font=tipgra,
                 text="Regla de Boole",
                 variable=met_inter,
                 value=3,
                 command="")
r_Bl.place(x=65, y=290)


lb_pau = Label(canvas, font=tipgra,
            text="Puntos a utilizar",)


current_value = StringVar(value=0)
ent_pts = Spinbox(
    canvas,
    from_=1,
    to=200,
    width=3,
    textvariable=current_value,
    wrap=True)



btn_calcular = Button(canvas,
               text="Calcular",
               image=pixelVirtual,
               command=calcular,
               height = 20,
               font=tipgra,
               width = 80,
               compound="c").place(x=175, y=320)



lb_Aprox = Label(canvas,
               font=tipgra,
                text="Aproximacion").place(x=10, y=370)
ent_Aprox = Entry(canvas,
                  font=tipgra,width=35)
ent_Aprox.place(x=100, y=370)


lb_Err = Label(canvas,
               font=tipgra,
                text="Error").place(x=10, y=400)

ent_Err = Entry(canvas,
               font=tipgra,width=35)
ent_Err.place(x=100, y=400)

ent_Aprox.config(state= "disabled")
ent_Err.config(state= "disabled")

btn_ayuda = Button(canvas,
               font=tipgra,
               text="Ayuda",
               image=pixelVirtual,
               command="",
               height = 20,
               width = 80,
               compound="c").place(x=175, y=440)


canvas.create_line(0,190,400,190, fill="black", width=1)
canvas.create_line(0,360,400,360, fill="black", width=1)
canvas.create_line(0,435,400,435, fill="black", width=1)





root.mainloop()
