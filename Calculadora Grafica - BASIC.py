from tkinter import *
from tkinter import messagebox

#================================================================ BÁSICOS DE LA CALCULADORA

Interfaz = Tk()
Interfaz.title("Calculadora")
Interfaz.resizable("False", "False")
Interfaz.config(bg="grey")

#================================================================ LISTAS DE NÚMEROS

ResultadoL = []

i = 0

MostradorVal = StringVar()

#================================================================ FUNCIONES

def Boton(Valor):
    Tamaño = len(ResultadoL)
    if Tamaño > 0:
        Mostrador.delete(0, END)
        ResultadoL.clear()
    global i
    Mostrador.insert(i, Valor)
    i += 1
    return Valor

def Resultado():
    Mstr = Mostrador.get()
    Div0 = "/0"
    pc = Mstr[0]
    ListaErr = ["*+", "+*", "*-", "-*", "*/", "/*",
                "+-", "-+", "+/", "/+",
                "-/", "/-"]
    
    if Div0 in Mstr:
        Mostrador.delete(0, END)
        Mostrador.insert(0, "Error: División por 0")
        Err = Mostrador.get()
        ResultadoL.append(Err)
    elif (pc == "+") or (pc == "-") or (pc == "*") or (pc == "/"):
        Mostrador.delete(0, END)
        Mostrador.insert(0, "Ingresa un número primero")
        Err = Mostrador.get()
        ResultadoL.append(Err)
    elif any(errores in Mstr for errores in ListaErr):
        Mostrador.delete(0, END)
        Mostrador.insert(0, "Utiliza parentesis (operador juntos)")
        Err = Mostrador.get()
        ResultadoL.append(Err)  
    else:
        Resultado = eval(Mstr)
        Mostrador.delete(0, END)
        Mostrador.insert(0, Resultado)
        ResultadoL.append(Mstr)
        return Resultado

def borrar():
    Mostrador.delete(0, END)

#================================================================ Mostrador

Mostrador = Entry(Interfaz, font = ("Calibri 20"))
Mostrador.grid(row = 0, column = 0, columnspan = 4, padx = 2, pady = 4)
Mostrador.config(justify = "right")

#================================================================ Botones NÚMERICOS

Boton1 = Button(Interfaz, text="1", width = 5, height = 2, command = lambda: Boton(1))
Boton1.grid(row = 2, column = 0, padx = 5, pady = 5)

Boton2 = Button(Interfaz, text="2", width = 5, height = 2, command = lambda: Boton(2))
Boton2.grid(row = 2, column = 1, padx = 5, pady = 5)

Boton3 = Button(Interfaz, text="3", width = 5, height = 2, command = lambda: Boton(3))
Boton3.grid(row = 2, column = 2, padx = 5, pady = 5)

Boton4 = Button(Interfaz, text="4", width = 5, height = 2, command = lambda: Boton(4))
Boton4.grid(row = 3, column = 0, padx = 5, pady = 5)

Boton5 = Button(Interfaz, text="5", width = 5, height = 2, command = lambda: Boton(5))
Boton5.grid(row = 3, column = 1, padx = 5, pady = 5)

Boton6 = Button(Interfaz, text="6", width = 5, height = 2, command = lambda: Boton(6))
Boton6.grid(row = 3, column = 2, padx = 5, pady = 5)

Boton7 = Button(Interfaz, text="7", width = 5, height = 2, command = lambda: Boton(7))
Boton7.grid(row = 4, column = 0, padx = 5, pady = 5)

Boton8 = Button(Interfaz, text="8", width = 5, height = 2, command = lambda: Boton(8))
Boton8.grid(row = 4, column = 1, padx = 5, pady = 5)

Boton9 = Button(Interfaz, text="9", width = 5, height = 2, command = lambda: Boton(9))
Boton9.grid(row = 4, column = 2, padx = 5, pady = 5)

Boton0 = Button(Interfaz, text="0", width = 15, height = 2, command = lambda: Boton(0))
Boton0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)

#================================================================ Botones Lógico

BotonAC = Button(Interfaz, text="AC", width = 5, height = 2, command = borrar)
BotonAC.grid(row = 1, column = 0, padx = 5, pady = 5)

BotonResultado = Button(Interfaz, text="=", width = 5, height = 2, command = Resultado)
BotonResultado.grid(row = 5, column = 3, padx = 5, pady = 5)

BotonPar1 = Button(Interfaz, text="(", width = 5, height = 2, command = lambda: Boton("("))
BotonPar1.grid(row = 1, column = 1, padx = 5, pady = 5)

BotonPar2 = Button(Interfaz, text=")", width = 5, height = 2, command = lambda: Boton(")"))
BotonPar2.grid(row = 1, column = 2, padx = 5, pady = 5)

BotonC = Button(Interfaz, text=".", width = 5, height = 2, command = lambda: Boton("."))
BotonC.grid(row = 5, column = 2, padx = 5, pady = 5)

#================================================================ Botones Operaciones

BotonSuma = Button(Interfaz, text="+", width = 5, height = 2, command = lambda: Boton("+"))
BotonSuma.grid(row = 4, column = 3, padx = 5, pady = 5)

BotonResta = Button(Interfaz, text="-", width = 5, height = 2, command = lambda: Boton("-"))
BotonResta.grid(row = 3, column = 3, padx = 5, pady = 5)

BotonMulti = Button(Interfaz, text="×", width = 5, height = 2, command = lambda: Boton("*"))
BotonMulti.grid(row = 2, column = 3, padx = 5, pady = 5)

BotonDiv = Button(Interfaz, text="÷", width = 5, height = 2, command = lambda: Boton("/"))
BotonDiv.grid(row = 1, column = 3, padx = 5, pady = 5)

#============================================================== Fin

Interfaz.mainloop()
