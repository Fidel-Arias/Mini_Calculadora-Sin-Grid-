from tkinter import Tk, Entry, Button
from math import pi

def clickBoton(valor):
    global i
    vista.insert(i, valor)
    i += 1
def BorrarParte():
    global vista
    largo=len(vista.get())-1
    vista.delete(largo)
def BorrarTodo  ():
    vista.delete(0, "end")

def operation():
    try:
        evaluacion = vista.get()
        resultado = round(eval(evaluacion),15)
        vista.delete(0, "end")
        vista.insert(0, resultado)
    except ZeroDivisionError:
        vista.insert(0,"Error desconocido : null ")
i = 0
window = Tk()
window.title("Mini-Calculadora")
window.geometry("300x300")

#Visata de los resultados delas operaciones
vista = Entry(window, bg="light grey", font=25)
vista.place(relx=0.03, rely=0.03, relwidth=0.850, relheight=0.125)

#Botones de la calculadora
#Primera Columna
#Boton-7
boton7 = Button(window, text="7", font=("Helvetica", 20), bg="skyblue", command=lambda : clickBoton(7))
boton7.place(relx=0.03, rely=0.175, relwidth=0.160, relheight=0.150)

#Boton-4
boton4 = Button(window, text="4", font=("Helvetica", 20), bg="skyblue", command=lambda : clickBoton(4))
boton4.place(relx=0.03, rely=0.345, relwidth=0.160, relheight=0.150)

#Boton-1
boton1 = Button(window, text="1", font=("Helvetica", 20), bg="skyblue", command=lambda : clickBoton(1))
boton1.place(relx=0.03, rely=0.520, relwidth=0.160, relheight=0.150)

#Boton-0
boton0 = Button(window, text="0", font=("Helvetica", 20), bg="skyblue", command=lambda : clickBoton(0))
boton0.place(relx=0.03, rely=0.690, relwidth=0.160, relheight=0.150)

#Segunda_Columna
#Boton-8
boton8 = Button(window, text="8", font=("Helvetica", 20), bg="skyblue", command=lambda : clickBoton(8))
boton8.place(relx=0.218, rely=0.175, relwidth=0.150, relheight=0.150)

#Boton-5
boton5 = Button(window, text="5", font=("Helvetica", 20), bg="skyblue", command=lambda : clickBoton(5))
boton5.place(relx=0.218, rely=0.345, relwidth=0.150, relheight=0.150)

#Boton-2
boton2 = Button(window, text="2", font=("Helvetica", 20), bg="skyblue", command=lambda : clickBoton(2))
boton2.place(relx=0.218, rely=0.520, relwidth=0.150, relheight=0.150)

#Boton-0
botonPunto = Button(window, text=".", font=("Helvetica", 20), bg="skyblue", command=lambda : clickBoton("."))
botonPunto.place(relx=0.218, rely=0.690, relwidth=0.150, relheight=0.150)

#Tercera_Columna
#Boton-9
boton9 = Button(window, text="9", font=("Helvetica", 20), bg="skyblue", command=lambda : clickBoton(9))
boton9.place(relx=0.390, rely=0.175, relwidth=0.150, relheight=0.150)

#Boton-6
boton6 = Button(window, text="6", font=("Helvetica", 20), bg="skyblue", command=lambda : clickBoton(6))
boton6.place(relx=0.390, rely=0.345, relwidth=0.150, relheight=0.150)

#Boton-3
boton3 = Button(window, text="3", font=("Helvetica", 20), bg="skyblue", command=lambda : clickBoton(3))
boton3.place(relx=0.390, rely=0.520, relwidth=0.150, relheight=0.150)

#Boton-Pi
botonPi = Button(window, text="π", font=("Helvetica", 20), bg="skyblue", command=lambda : clickBoton(round(pi,6)))
botonPi.place(relx=0.390, rely=0.690, relwidth=0.150, relheight=0.150)

#Cuarta_Columna
#Boton_DEL
botonDEL = Button(window, text="DEL", font=("Helvetica", 15), bg="orange", command=BorrarParte)
botonDEL.place(relx=0.560, rely=0.175, relwidth=0.150, relheight=0.150)

#Boton_Suma
botonSuma = Button(window, text="+", font=("Helvetica", 20) , bg="red", command=lambda : clickBoton("+"))
botonSuma.place(relx=0.560, rely=0.345, relwidth=0.150, relheight=0.150)

#Boton_Multiplicacion
botonMulti = Button(window, text="x", font=("Helvetica", 15) , bg="red", command=lambda : clickBoton("*"))
botonMulti.place(relx=0.560, rely=0.520, relwidth=0.150, relheight=0.150)

#Boton_Igual
botonIgual = Button(window, text="=", font=("Helvetica", 15) , bg="pink", command=operation)
botonIgual.place(relx=0.560, rely=0.690, relwidth=0.320, relheight=0.150)

#Quinta_Columna
#Boton_AC
botonAC = Button(window, text="AC", font=("Helvetica", 15), bg="orange", command=BorrarTodo)
botonAC.place(relx=0.730, rely=0.175, relwidth=0.150, relheight=0.150)

#Boton_Resta
botonResta = Button(window, text="-", font=("Helvetica", 20) , bg="red", command=lambda : clickBoton("-"))
botonResta.place(relx=0.730, rely=0.345, relwidth=0.150, relheight=0.150)

botonDivi = Button(window, text="÷", font=("Helvetica", 20) , bg="red", command=lambda : clickBoton("/"))
botonDivi.place(relx=0.730, rely=0.520, relwidth=0.150, relheight=0.150)

window.mainloop()