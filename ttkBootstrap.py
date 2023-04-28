from tkinter import Tk, ttk
from ttkbootstrap import Style

root = Tk()
style = Style(theme='cosmo')

tree = ttk.Treeview(root, columns=('name', 'age', 'gender'))
tree.heading('#0', text='ID')
tree.heading('name', text='Name')
tree.heading('age', text='Age')
tree.heading('gender', text='Gender')

tree.insert('', '0', 'item1', text='1', values=('John', '32', 'Male'))
tree.insert('', '1', 'item2', text='2', values=('Jane', '25', 'Female'))
tree.insert('', '2', 'item3', text='3', values=('Bob', '42', 'Male'))

tree.pack(expand=True, fill='both')
root.mainloop()