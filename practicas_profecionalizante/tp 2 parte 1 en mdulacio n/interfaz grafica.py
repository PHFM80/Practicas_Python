from tkinter import *

raiz = Tk()

#parametros de la ventana
raiz.title ("T.P. N° 2 Practicas profezionalizante I, parte 1.")
raiz.resizable(50, 50)
raiz.geometry("650x500")
raiz.config(bg="blue")

#Parametros del frame que va dentro de la ventana

miFrame = Frame()
miFrame.pack()
#miFrame.pack(fill="both", expand="True")
miFrame.config(bg="red")
miFrame.config(width="650", height="300")
miFrame.config(bd= 30)
miFrame.config(relief="raised")





raiz.mainloop()



