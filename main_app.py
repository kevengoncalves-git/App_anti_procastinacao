import customtkinter

print("Esse é meu app anti-procastinação")

def resposta_primeiro_botao():
    print("naoooooo")

class APP(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Info. geral
        self.geometry("400x320")
        self.title("ANTI-PROCASTINATOR 1.0")
        self.grid_columnconfigure((0, 1), weight=1)
        #app.grid_columnconfigure(1, weight=1) mais de uma coluna

        #Estudando os widgets
        self.botao = customtkinter.CTkButton(self, text="Ta procastinando?" , command=resposta_primeiro_botao)
        self.botao.grid(row=0, column=0, pady=(0,20), sticky='ew', columnspan=2) #sticky='' esticar algo na propria coluna
        #columnspan=2 fica em duas colunas

        self.checkbox1 = customtkinter.CTkCheckBox(self, text="Ta rico?")
        self.checkbox1.grid(row=1, column=0, padx=10, pady=(0,10), sticky='w')
        self.checkbox2 = customtkinter.CTkCheckBox(self, text="Ta liso?")
        self.checkbox2.grid(row=1, column=1, padx=10, pady=(0,10), sticky='e')


app = APP()
app.mainloop()