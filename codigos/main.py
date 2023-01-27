import tkinter as tk
from lib.FuncCompiladas import *



app = tk.Tk()
app.title("LPD")
app.configure(background="#dde")
app.geometry("500x500")

tk.Label(app,text = "Qual é a Bandeira do Seu Cartão?", background= '#dde', foreground='#009', anchor= tk.W).place(x =10, y=10, width=400, height=20)

vband = tk.Entry(app)
vband.place(x=10, y=30, width=200, height=20)



########################################################################################

texto = tk.Label(app, text=" Qual o seu número?",background= '#dde', foreground='#009', anchor= tk.W)
texto.place(x = 10, y = 50, width=200, height=20)

vnumero = tk.Entry(app)
vnumero.place(x=10, y=80, width=200, height=20)
########################################################################################
def v1():
    i = vband.get()
    n = vnumero.get()
    print(n, i)
    label = tk.Label(app, text= f'{i} e {n}', background="#ffe")
    label.place(x=10, y=140)

    return [i, n]





tk.Button(app, text='Enviar', command= v1, bg="#fff").place(x=10, y=110, width=90, height=20)

lista = v1()



app.mainloop()