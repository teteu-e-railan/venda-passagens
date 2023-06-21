import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "dark-blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Montagem da tela e componentes
        self.title("Exemplo teste")
        self.geometry(f"{1100}x{580}")

        # Testando a renderizacao de botoes dentro de um `for loop`
        for i in [0, 1, 2, 3]:
            customtkinter.CTkButton(
                self, text=f"Botao{i}", command=lambda index=i: self.on_click(index)
            ).pack(padx=20, pady=10)

    def mostra_opcoes(self):
        self.mainloop()

        return self.index_selecionado

    def on_click(self, index: int):
        self.index_selecionado = index
        self.destroy()


app = App()
print(app.mostra_opcoes())
