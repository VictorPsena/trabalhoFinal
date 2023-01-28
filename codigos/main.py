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

texto = tk.Label(app, text=" Vai ser no crédito ou no débito?",background= '#dde', foreground='#009', anchor= tk.W)
texto.place(x = 10, y = 50, width=200, height=20)

vcreddeb = tk.Entry(app)
vcreddeb.place(x=10, y=80, width=200, height=20)
########################################################################################

texto = tk.Label(app, text=" Quantas parcelas?",background= '#dde', foreground='#009', anchor= tk.W)
texto.place(x = 10, y = 110, width=200, height=20)

vparce = tk.Entry(app)
vparce.place(x=10, y=140, width=200, height=20)

########################################################################################


texto = tk.Label(app, text="Qual o valor do produto comprado pelo vendedor?",background= '#dde', foreground='#009', anchor= tk.W)
texto.place(x = 10, y = 170, width=400, height=20)

vval = tk.Entry(app)
vval.place(x=10, y=200, width=200, height=20)



def v1():
    i = vband.get()
    c = vcreddeb.get()
    p = vparce.get()
    v = vval.get()

   

    db = DebCred(c)
    taxa = TaxaBandeira(i, int(p), db)
    lista = ldp(float(v), i, taxa)


    label = tk.Label(app, text= f' Lucro: {lista[0]:.2f} \n Margem de lucro: {lista[1]:.2f} \n Preço Ideal: {lista[2]:.2f} \n Desconto Máximo: {lista[3]:.2f} \n Lucro mínimo: {lista[4]:.2f} \n Tarifa da maquininha: {lista[5]:.2f}', bg ="#ffe")
    label.place(x=40, y=260, width=400, height=200)

    return [i, c, p, v]




tk.Button(app, text='Enviar', command= v1, bg="#fff").place(x=10, y=230, width=90, height=20)


app.mainloop()