from tkinter import *
import tkinter.font as font

width=400
height=500


#los Constructores del GUI
root = Tk()
root.resizable(width=False, height=False) # prevents resizing window

canvas = Canvas(root, width=width, height=height-20)
canvas.configure(bd=0, highlightthickness=0)
canvas.pack()
pixelVirtual = PhotoImage(width=1, height=1)
var = IntVar()
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
    lb_pau.place(x=180, y=250)
    ent_pts.place(x=220, y=270)
    r_Tr['text'] = 'Trapecio Compuesto'
    r_Sm['text'] = 'Simpson Compuesto'
    r_Bl['text'] = 'Cuadraturas Gausianas'
    r_Tr['value'] = 4
    r_Sm['value'] = 5
    r_Bl['value'] = 6

def calcular():
    print(ent_fx.get())
    print(ent_aEq.get())
    print(ent_bEq.get())
    print(var.get())


#contenido gui

lb_Titulo = Label(canvas,
                text="Calculadora de Integrales Definidas",font=tipgra
                    ).place(x=50, y=2)

img = PhotoImage(file='inte.png')
Label(
    canvas,
    image=img
).place(x=150,y=30)

lb_fx = Label(canvas, font=tipgra,
            text="f(x)=",
                    ).place(x=50, y=110)
ent_fx = Entry(canvas,font=tipgra)
ent_fx.place(x=90, y=110)
lb_aEq = Label(canvas,font=tipgra,
                text="a=").place(x=50, y=150)

ent_aEq = Entry(canvas ,font=tipgra,width = 5)
ent_aEq.place(x=80, y=150)
lb_bEq = Label(canvas,font=tipgra,text="b=").place(x=150, y=150)

ent_bEq = Entry(canvas,font=tipgra,width = 5)
ent_bEq.place(x=180, y=150)

btn_MSimpl = Button(canvas,
               text="Métodos simples",
               image=pixelVirtual,
               command=simpleAcompuesto ,
               height = 20,
               width = 120,
               font=tipgra,
               compound="c").place(x=20, y=200)

btn_MComp = Button(root,
               text="Métodos compuesto",
               image=pixelVirtual,
               command=compuestoAsimple,
               height = 20,
               font=tipgra,
               width = 150,
               compound="c").place(x=150, y=200)



r_Tr = Radiobutton(canvas,
                 font=tipgra,
                 text="Trapecio",
                 variable=var,
                 value=1,
                 command="")
r_Tr.place(x=15, y=230)

r_Sm = Radiobutton(canvas,
                 font=tipgra,
                 text="Simpson",
                 variable=var,
                 value=2,
                 command="")
r_Sm.place(x=15, y=260)

r_Bl = Radiobutton(canvas,
                 font=tipgra,
                 text="Regla de boole",
                 variable=var,
                 value=3,
                 command="")
r_Bl.place(x=15, y=290)


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
               compound="c").place(x=125, y=320)



lb_Aprox = Label(canvas,
               font=tipgra,
                text="Aproximacion").place(x=10, y=370)
ent_Aprox = Entry(canvas,
                  font=tipgra,width=35).place(x=100, y=370)


lb_Err = Label(canvas,
               font=tipgra,
                text="Error").place(x=10, y=400)

ent_Err = Entry(canvas,
               font=tipgra,width=35).place(x=100, y=400)

btn_ayuda = Button(canvas,
               font=tipgra,
               text="Ayuda",
               image=pixelVirtual,
               command="",
               height = 20,
               width = 80,
               compound="c").place(x=125, y=440)


canvas.create_line(0,190,400,190, fill="black", width=1)
canvas.create_line(0,360,400,360, fill="black", width=1)
canvas.create_line(0,435,400,435, fill="black", width=1)





root.mainloop()
