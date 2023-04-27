import tkinter as tk

root = tk.Tk()

# Cria um frame com largura de 200 e altura de 200
frame = tk.Frame(root, width=200, height=200)
frame.pack()

# Cria um label com o texto "Hello, world!"
label = tk.Label(frame, text="Hello, world!")

# Define a coluna 0 do grid do frame com o tamanho mínimo de 1
frame.columnconfigure(0, minsize=1)

# Adiciona o label à primeira linha e primeira coluna do grid do frame
label.grid(row=0, column=0, sticky="ew")

root.mainloop()