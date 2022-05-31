from tkinter import *
width=320
height=480


#los Constructores del GUI
root = Tk()
root.resizable(width=False, height=False) # prevents resizing window
canvas = Canvas(root, width=width, height=height)
canvas.configure(bd=0, highlightthickness=0)
canvas.pack()
pixelVirtual = PhotoImage(width=1, height=1)
var = IntVar()

frm_sim = Frame(canvas,
             height = 100,
             width =200).place(x=70, y=240)


def simpleAcompuesto():
    r_Tr['text'] = 'Trapecio'
    r_Sm['text'] = 'Simpson'
    r_Bl['text'] = 'Regla de boole'
    r_Tr['value'] = 1
    r_Sm['value'] = 2
    r_Bl['value'] = 3
    

def compuestoAsimple():
    r_Tr['text'] = 'Trapecio Compuesto'
    r_Sm['text'] = 'Simpson Compuesto'
    r_Bl['text'] = 'Cuadraturas Gausianas'
    r_Tr['value'] = 4
    r_Sm['value'] = 5
    r_Bl['value'] = 6

def calcular():
    print(var.get())


#contenido gui estatico
lb_Titulo = Label(canvas,
                text="Calculadora de Integrales Definidas",
                    ).place(x=65, y=10)

lb_fx = Label(canvas,
            text="f(x)=",
                    ).place(x=50, y=125)
ent_fx = Entry(canvas).place(x=90, y=125)

lb_aEq = Label(canvas,
                text="a=").place(x=10, y=150)

ent_aEq = Entry(canvas).place(x=30, y=150)

lb_bEq = Label(canvas,
                text="b=").place(x=160, y=150)
ent_bEQ = Entry(canvas).place(x=180, y=150)

btn_MSimpl = Button(canvas,
               text="Métodos simples",
               image=pixelVirtual,
               command=simpleAcompuesto ,
               height = 20,
               width = 105,
               compound="c").place(x=40, y=200)

btn_MComp = Button(root,
               text="Métodos compuesto",
               image=pixelVirtual,
               command=compuestoAsimple,
               height = 20,
               width = 110,
               compound="c").place(x=155, y=200)



btn_calcular = Button(canvas,
               text="Calcular",
               image=pixelVirtual,
               command=calcular,
               height = 20,
               width = 80,
               compound="c").place(x=125, y=350)



lb_Aprox = Label(canvas,
                text="Aproximacion").place(x=10, y=390)
ent_Aprox = Entry(canvas).place(x=100, y=390)


lb_Err = Label(canvas,
                text="Error").place(x=10, y=410)

ent_Err = Entry(canvas).place(x=100, y=410)

btn_ayuda = Button(canvas,
               text="Ayuda",
               image=pixelVirtual,
               command="",
               height = 20,
               width = 80,
               compound="c").place(x=125, y=440)




r_Tr = Radiobutton(frm_sim,
                 text="Trapecio",
                 variable=var,
                 value=1,
                 command="")
r_Tr.place(x=30, y=260)

r_Sm = Radiobutton(frm_sim,
                 text="Simpson",
                 variable=var,
                 value=2,
                 command="")
r_Sm.place(x=30, y=280)

r_Bl = Radiobutton(frm_sim,
                 text="Regla de boole",
                 variable=var,
                 value=3,
                 command="")
r_Bl.place(x=30, y=300)






root.mainloop()
