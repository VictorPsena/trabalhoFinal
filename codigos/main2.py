from tkinter import *
from lib.FuncCompiladasApp import *
app = Tk()

app.title("LDP")
app.geometry("500x750+610+153")
app.resizable(False, False)


#importando as imgs


img_fundo = PhotoImage(file="codigos\\fundo.png")


label_fundo = Label(app, image= img_fundo)
label_fundo.pack()


vband = Entry(app, justify=CENTER, font="Impact", border= 5, background="#EEE4E8")
vband.place(x=110, y=177, width=270, height=40)


vcreddeb = Entry(app, justify=CENTER, font="Impact", border= 5,background="#EEE4E8")
vcreddeb.place(x=110, y=265.80, width=270, height=40)


vparce = Entry(app, justify=CENTER, font="Impact",  border= 5,background="#EEE4E8")
vparce.place(x=110, y=357, width=270, height=40)



vval = Entry(app, justify=CENTER, font="Impact",  border= 5,background="#EEE4E8")
vval.place(x=110, y=453, width=270, height=40)







def v1():
    i = vband.get()
    c = vcreddeb.get()
    p = vparce.get()
    v = vval.get()

   

    db = DebCred(c)
    taxa = TaxaBandeira(i, int(p), db)
    lista = ldp(float(v), i, taxa)


    label = Label(app, text= f'Lucro: R${lista[0]:.2f} \n Margem de lucro: {lista[1]:.2f}% \n Preço Ideal: R${lista[2]:.2f} \n Desconto Máximo: R${lista[3]:.2f} \n Lucro mínimo: R${lista[4]:.2f} \n Tarifa da maquininha: R${lista[5]:.2f}', bg ="#48D1CC", border= 5, foreground="#fff", font="ArialBlack")
    label.place(x=120, y=580, width=270, height=130)






Button(app, text='Enviar', command= v1, bg="#fff",  font="Impact", justify=CENTER, foreground="green").place(x=210, y=514, width=80, height=40)



app.mainloop()