import tkinter as tk
from tkinter import *


cor = {"preto" : "#252726","purple" : "#800080","white" : "#FFFFFF"}


btnE_mover = False


app = tk.Tk()
app.title("TELA DE MOBILE EM TKINTER")
app.config(bg="gray30")
app.geometry("400x600")

top_frame = tk.Frame(app, bg=cor['purple'])
top_frame.pack(side="top", fill=tk.X)


acc_text_navbar = tk.Label(top_frame,text="Tkinter",font="ExtraCondensed 15",
                           bg=cor["purple"],fg="white",height=2,padx=20)
acc_text_navbar.pack(side="right")

app.mainloop()