from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Paned Window")
root.geometry("500x400")

panel1 = PanedWindow(bd=4, relief='raised', bg='red')
panel1.pack(fill=BOTH, expand=1)

left_label = Label(panel1,text="Painel Esquerdo")
panel1.add(left_label)

panel2 = PanedWindow(panel1,)


root.mainloop()
