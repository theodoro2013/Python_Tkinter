from tkinter import *

cor = {"azul" : "#1D3557","azulClaro" : "#457B9D","branco" : "#F1FAEE","vermelho" : "#E63946", "cinza" : "#8D99AE"}
#botão de opções (sidebar lateral)
bt_move = False
#carregando opções da treeview

#inicio do app
app = Tk()
app.title("Coliseu Requisições")
app.config(bg=cor["branco"])
app.state('zoomed')

PainelPrincipal = PanedWindow(app, orient=HORIZONTAL, bg=cor["vermelho"], sashrelief=SUNKEN)
PainelPrincipal.paneconfigure(0, minsize=150)
PainelPrincipal.config(minsize=300)
def resize_panes(event):
    size = PainelPrincipal.winfo_width()
    PainelPrincipal.paneconfigure(0, minsize=size/2)
    PainelPrincipal.paneconfigure(1, minsize=size/2)

PainelPrincipal.bind("<Configure>", resize_panes)

PainelPrincipal.pack(fill=BOTH, expand=True)
button1 = Button(PainelPrincipal, text="Button 1")
button2 = Button(PainelPrincipal, text="Button 2")
PainelPrincipal.add(button1)
PainelPrincipal.add(button2)

PainelPrincipal.pack(fill=BOTH, expand=True)
PainelPrincipal.place(x=100, y=100, width=300, height=300)
app.mainloop()