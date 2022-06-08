from operator import ge
from tkinter import *
import tkinter.font as font
import CheckContinuidad as ck
import Metodos.ReglaDeBoole as Rb

import os



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
    r_Bl['text'] = 'Regla de boole'
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




def calcular():
    ent_Aprox.config(state= "normal")
    ent_Err.config(state= "normal")
    ent_Aprox.delete(0, END)
    ent_Err.delete(0, END)
    try:
        a= float(ent_aEq.get())
        b= float(ent_bEq.get())
        fun_X=ent_fx.get()
        
        ck_inter= ck.checkInverval(fun_X,a,b)
        
        
        if not(ck_inter):
            ent_Aprox.insert(0,"0")
            ent_Err.insert(0,"Funcion discontinua")
        
        if a==b:
            ent_Aprox.insert(0,"0")
            ent_Err.insert(0,"Error de sintaxis a = b")
            print("igual 0")
        
        if met_inter==0:
            ent_Aprox.insert(0,"0")
            ent_Err.insert(0,"Seleccione un metodo")
        
        if met_inter==1:#trapecio
            ent_Aprox.insert(0,"0")
            ent_Err.insert(0,"Seleccione un metodo")
        
        if met_inter==2:#simpson
            ent_Aprox.insert(0,"0")
            ent_Err.insert(0,"Seleccione un metodo")
        
        if met_inter==3:#Regla_boole
            ent_Aprox.insert(0,"0")
            ent_Err.insert(0,"Seleccione un metodo")
        
        if met_inter==4:#trapecio_compuesto
            ent_Aprox.insert(0,"0")
            ent_Err.insert(0,"Seleccione un metodo")
        
        if met_inter==5:#simpson_compuesto
            ent_Aprox.insert(0,"0")
            ent_Err.insert(0,"Seleccione un metodo")
        
        if met_inter==6:#Cuadraturas gaussianas
            ent_Aprox.insert(0,"0")
            ent_Err.insert(0,"Seleccione un metodo")
    
    except ValueError:
        ent_Aprox.insert(0,"0")
        ent_Err.insert(0,"Ingresar valores numericos")
    except TypeError:
        ent_Aprox.insert(0,"0")
        ent_Err.insert(0,"Ingresar valores numericos")
    except:
        print("Something else went wrong")
    
        

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
                 text="Regla de boole",
                 variable=met_inter,
                 value=3,
                 command="")
r_Bl.place(x=65, y=290)


lb_pau = Label(canvas, font=tipgra,
            text="Puntos a utilizar",)
ent_pts = Entry(canvas,font=tipgra,width=3)






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
