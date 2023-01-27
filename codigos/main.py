import tkinter as tk


def v1():
    print('oi')


app = tk.Tk()
app.title("LPD")
app.configure(background="#dde")
app.geometry("500x500")

tk.Label(app,text = "Qual é a Bandeira do Seu Cartão?", background= '#dde', foreground='#009', anchor= tk.W).place(x =10, y=10, width=400, height=20)

vband = tk.Entry(app)
vband.place(x=10, y=30, width=200, height=20)

tk.Button(app, text='Enviar', command= v1).place(x=250, y=30, width=90, height=20)

########################################################################################








app.mainloop()