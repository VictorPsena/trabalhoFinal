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
    i = vband.get().lower().strip()
    # if i != "visa" or i != "elo" or i!= "mastercard":
    #     erro = Tk()
    #     erro.geometry("270x100+710+253")
    #     erro.title("ERRO")
    #     erro.resizable(False, False)
    #     texto = Label(erro, text="Digite uma bandeira válida.",background= '#dde', foreground='red', anchor= N, font="Impact")
    #     texto.place(x = 10, y =10, width= 250, height= 30)
    #     Button(erro, text="Enviar", command= erro.destroy,font="Impact", justify=CENTER, foreground="green" ).place(x = 105, y=50, width=50, height= 30)
    #     erro.mainloop()

    lista = ['elo', 'visa', 'mastercard', 'hipercard']
    try:
       lista.index(i)
    except (ValueError, TypeError):
        erro = Tk()
        erro.geometry("270x100+710+253")
        erro.title("ERRO")
        erro.resizable(False, False)
        texto = Label(erro, text="Digite uma bandeira válida. \n  visa, mastercard, elo, hipercard",background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
        texto.place(x = 10, y =10, width= 250, height= 50)
        Button(erro, text="OK", command= erro.destroy,font="Impact", justify=CENTER, foreground="green" ).place(x = 105, y=65, width=50, height= 30)
    

        erro.mainloop()
       
   
    
    


    c = vcreddeb.get().lower().strip()[0]
    lista1 = ['d', 'c']
    try:
       lista1.index(c)
    except (ValueError, TypeError):
        erro = Tk()
        erro.geometry("270x100+710+253")
        erro.title("ERRO")
        erro.resizable(False, False)
        texto = Label(erro, text="Escolha entre crédito ou débito.",background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
        texto.place(x = 10, y =10, width= 250, height= 30)
        Button(erro, text="OK", command= erro.destroy,font="Impact", justify=CENTER, foreground="green" ).place(x = 105, y=50, width=50, height= 30)
    

        erro.mainloop()






    p = vparce.get()
    try:
         p = int(p)
         if p > 12 or p < 1:
            erro = Tk()
            erro.geometry("270x100+710+253")
            erro.title("ERRO")
            erro.resizable(False, False)
            texto = Label(erro, text="Digite um número de 1 a 12",background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
            texto.place(x = 10, y =10, width= 250, height= 30)
            Button(erro, text="OK", command= erro.destroy,font="Impact", justify=CENTER, foreground="green" ).place(x = 105, y=50, width=50, height= 30)
        

            erro.mainloop()
             
    except(ValueError, TypeError):
        erro = Tk()
        erro.geometry("270x100+710+253")
        erro.title("ERRO")
        erro.resizable(False, False)
        texto = Label(erro, text="É um número inteiro." ,background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
        texto.place(x = 10, y =10, width= 250, height= 30)
        Button(erro, text="OK", command= erro.destroy,font="Impact", justify=CENTER, foreground="green" ).place(x = 105, y=50, width=50, height= 30)
    

        erro.mainloop()

    



    v = vval.get()
    try:
        v = float(v)
        if  v > 50000:
            erro = Tk()
            erro.geometry("270x100+710+253")
            erro.title("ERRO")
            erro.resizable(False, False)
            texto = Label(erro, text="O valor máximo de pruduto é R$50.000",background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
            texto.place(x = 10, y =10, width= 250, height= 30)
            Button(erro, text="OK", command= erro.destroy,font="Impact", justify=CENTER, foreground="green" ).place(x = 105, y=50, width=50, height= 30)
        
        elif v <= 0:
            erro = Tk()
            erro.geometry("270x100+710+253")
            erro.title("ERRO")
            erro.resizable(False, False)
            texto = Label(erro, text="Seria uma boa comprar de graça.",background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
            texto.place(x = 10, y =10, width= 250, height= 30)
            Button(erro, text="OK", command= erro.destroy,font="Impact", justify=CENTER, foreground="green" ).place(x = 105, y=50, width=50, height= 30)


        

            erro.mainloop()
    except(ValueError, TypeError):
            erro = Tk()
            erro.geometry("270x100+710+253")
            erro.title("ERRO")
            erro.resizable(False, False)
            texto = Label(erro, text="Digíte um número, obrigado...",background= '#dde', foreground='#FF6666', anchor= N, font="Impact")
            texto.place(x = 10, y =10, width= 250, height= 30)
            Button(erro, text="OK", command= erro.destroy,font="Impact", justify=CENTER, foreground="green" ).place(x = 105, y=50, width=50, height= 30)    

            
            erro.mainloop()

    


    db = DebCred(c)
    taxa = TaxaBandeira(i, int(p), db)
    lista = ldp(float(v), i, taxa)


    label = Label(app, text= f'Lucro: R${lista[0]:.2f} \n Margem de lucro: {lista[1]:.2f}% \n Preço Ideal: R${lista[2]:.2f} \n Desconto Máximo: R${lista[3]:.2f} \n Lucro mínimo: R${lista[4]:.2f} \n Tarifa da maquininha: R${lista[5]:.2f} \n Parcelas: R${lista[2]/int(vparce.get()):.2f}', bg ="#48D1CC", border= 5, foreground="#fff", font="ArialBlack")
    label.place(x=120, y=580, width=270, height=130)






Button(app, text='Enviar', command= v1, bg="#fff",  font="Impact", justify=CENTER, foreground="green").place(x=210, y=514, width=80, height=40)



app.mainloop()