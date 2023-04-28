from tkinter import *

root = Tk()

# Cria um PanedWindow e define suas dimensões
paned_window = PanedWindow(root, width=400, height=300, bg='white')
paned_window.pack(fill=BOTH, expand=True)

# Cria dois frames dentro do PanedWindow
frame1 = Frame(paned_window, bg='red')
frame2 = Frame(paned_window, bg='blue')
paned_window.add(frame1)
paned_window.add(frame2)

# Posiciona o frame1 usando o place
frame1.place(x=50, y=50, width=150, height=150)
frame2.place(x=100, y=100, width=150, height=150)

root.mainloop()