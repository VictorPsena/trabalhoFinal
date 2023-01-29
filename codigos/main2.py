from tkinter import *
from lib.FuncCompiladasApp import *
app = Tk()

app.title("LDP")
app.geometry("500x750+610+153")
app.resizable(width=1, height=1)

#importando as imgs


img_fundo = PhotoImage(file="codigos\\fundo.png")


label_fundo = Label(app, image= img_fundo)
label_fundo.pack()


vband = Entry(app)
vband.place(x=110, y=177, width=270, height=40)


vcreddeb = Entry(app)
vcreddeb.place(x=110, y=265.80, width=270, height=40)


vparce = Entry(app)
vparce.place(x=110, y=357, width=270, height=40)



vval = Entry(app)
vval.place(x=110, y=453, width=270, height=40)







def v1():
    i = vband.get()
    c = vcreddeb.get()
    p = vparce.get()
    v = vval.get()

   

    db = DebCred(c)
    taxa = TaxaBandeira(i, int(p), db)
    lista = ldp(float(v), i, taxa)


    label = Label(app, text= f' Lucro: {lista[0]:.2f} \n Margem de lucro: {lista[1]:.2f} \n Preço Ideal: {lista[2]:.2f} \n Desconto Máximo: {lista[3]:.2f} \n Lucro mínimo: {lista[4]:.2f} \n Tarifa da maquininha: {lista[5]:.2f}', bg ="#ffe")
    label.place(x=150, y=580, width=270, height=100)

    return [i, c, p, v]




Button(app, text='Enviar', command= v1, bg="#fff").place(x=210, y=514, width=80, height=40)



app.mainloop()