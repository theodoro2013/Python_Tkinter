from tkinter import *

root = Tk()

# Cria um PanedWindow horizontal e define suas dimensões
PainelPrincipal = PanedWindow(root, orient=HORIZONTAL, width=600, height=400)
PainelPrincipal.pack(fill=BOTH, expand=True)

# Cria dois frames dentro do PanedWindow horizontal
FrameVermelho = Frame(PainelPrincipal, bg='red')
FrameAzul = Frame(PainelPrincipal, bg='blue')
botaoLaranja = Button(FrameVermelho,text="frameVermelho",bg='orange')
botaoLaranja.place(x=0,y=0)
PainelPrincipal.add(FrameVermelho)
PainelPrincipal.add(FrameAzul)

# Cria um PanedWindow vertical e define suas dimensões
paned_window_v = PanedWindow(FrameAzul, orient=VERTICAL, width=200, height=400)
paned_window_v.pack(fill=BOTH, expand=True)

# Cria dois frames dentro do PanedWindow vertical
frameVerde = Frame(paned_window_v, bg='green')
frameAmarelo = Frame(paned_window_v, bg='yellow')
paned_window_v.add(frameVerde)
paned_window_v.add(frameAmarelo)



root.mainloop()