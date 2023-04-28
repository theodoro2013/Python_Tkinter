from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Paned Window")
root.geometry("500x400")

panel1 = PanedWindow(bd=4, relief='raised', bg='green')
panel1.pack(fill=BOTH, expand=1)#preenche tudo

Framepreto= Frame(panel1,bg="black")
panel1.add(Framepreto)

nav_lateral= Frame(Framepreto,bg="green",height=100,width=100)
nav_lateral.place(x= 10,y=10)

#nav_lateral.place(x= 10,y=10)

#left_label = Label(panel1,text="Painel Esquerdo")
#panel1.add(left_label)

panel2 = PanedWindow(orient = VERTICAL, bd=4, relief='raised', bg='blue')
#panel1.add(panel2)

top = Label(panel2, text="Top")
panel2.add(top)



# Cria o TreeView com duas colunas
treeview = ttk.Treeview(panel2, columns=('Name', 'Age'))

# Define o cabeçalho das colunas
treeview.heading('#0', text='ID')
treeview.heading('Name', text='Name')
treeview.heading('Age', text='Age')

# Define a largura das colunas
treeview.column('#0', width=50)
treeview.column('Name', width=150)
treeview.column('Age', width=50)

# Adiciona alguns itens à árvore
treeview.insert('', '0', 'item1', text='1', values=('John', 25))
treeview.insert('', '1', 'item2', text='2', values=('Sarah', 32))
treeview.insert('', 'end', 'item3', text='3', values=('Bob', 18))

# Define um estilo para os itens da árvore
style = ttk.Style()
style.configure('Treeview', font=('Arial', 12))

# Define a cor de fundo para os itens pares
treeview.tag_configure('even', background='#e8e8e8')

# Adiciona tags aos itens pares
treeview.item('item2', tags=('even',))

#bottom = Label(panel2,text = 'Bottom')
panel2.add(treeview)

root.mainloop()
