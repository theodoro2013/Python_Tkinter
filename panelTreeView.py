import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('400x400')

# Cria um PanedWindow
pw = ttk.PanedWindow(root, orient=tk.VERTICAL)
pw.grid(row=0, column=0, sticky='nsew')

# Cria um frame para o primeiro pane
top_frame1 = tk.Frame(pw, bg='blue', height=30)
top_frame1.grid(row=0, column=0, sticky='nsew')#sticky como 'nsew' para que eles sejam expandidos em todas as direções e ocupem todo o espaço disponível.

# Adiciona o primeiro pane ao PanedWindow
pw.add(top_frame1)

# Cria um segundo frame para o segundo pane
top_frame2 = tk.Frame(pw, bg='green', height=30)
top_frame2.grid(row=1, column=0, sticky='nsew')

# Adiciona o segundo pane ao PanedWindow
pw.add(top_frame2)

# Cria o terceiro pane com a treeview
treeview_pane = ttk.Frame(pw)
treeview_pane.grid(row=2, column=0, sticky='nsew')

treeview = ttk.Treeview(treeview_pane, columns=('Name', 'Age'))
treeview.heading('#0', text='ID')
treeview.heading('Name', text='Name')
treeview.heading('Age', text='Age')
treeview.column('#0', width=50)
treeview.column('Name', width=150)
treeview.column('Age', width=50)
treeview.insert('', '0', 'item1', text='1', values=('John', 25))
treeview.insert('', '1', 'item2', text='2', values=('Sarah', 32))
treeview.insert('', 'end', 'item3', text='3', values=('Bob', 18))

style = ttk.Style()
style.configure('Treeview', font=('Arial', 12))
treeview.tag_configure('even', background='#e8e8e8')
treeview.item('item2', tags=('even',))

treeview.grid(row=0, column=0, sticky='nsew')
treeview_pane.grid_propagate(False)

pw.add(treeview_pane)

bottom_frame = tk.Frame(root)
bottom_frame.grid(row=3, column=0, sticky='nsew')

button = ttk.Button(bottom_frame, text='Click me!')
button.pack(side=tk.LEFT, padx=5, pady=5)

root.rowconfigure(0, weight=1, minsize=30)
root.rowconfigure(1, weight=1, minsize=30)
root.rowconfigure(2, weight=1, minsize=300)
root.rowconfigure(3, weight=1, minsize=50)
root.columnconfigure(0, weight=1, minsize=400)

root.mainloop()