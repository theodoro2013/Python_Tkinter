import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configurações da janela principal
        self.title("Menu Deslizável")
        self.geometry("300x200")

        # configurações do menu lateral
        self.menu_frame = tk.Frame(self, width=150, bg="black")
        self.menu_frame.pack(side="left", fill="y")
        self.menu_frame.place(x=-150, y=0)

        # botão para abrir/fechar o menu
        self.toggle_menu_button = tk.Button(self, text="Abrir Menu", command=self.toggle_menu)
        self.toggle_menu_button.pack(side="left")

        # adicione widgets ao menu aqui
        label = tk.Label(self.menu_frame, text="Menu Lateral")
        label.pack()

    def toggle_menu(self):
        # alternar a posição do menu
        if self.menu_frame.winfo_x() < 0:
            self.menu_frame.place(x=0, y=0)
            self.toggle_menu_button.config(text="Fechar Menu")
        else:
            self.menu_frame.place(x=-150, y=0)
            self.toggle_menu_button.config(text="Abrir Menu")

app = App()
app.mainloop()