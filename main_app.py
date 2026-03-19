import customtkinter

print("Esse é meu app anti-procastinação")


class FramePrimario(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.checkbox1 = customtkinter.CTkCheckBox(self, text="Ta rico?")
        self.checkbox1.grid(row=0, column=0, padx=10, pady=(0,10), sticky='w')
        self.checkbox2 = customtkinter.CTkCheckBox(self, text="Ta liso?")
        self.checkbox2.grid(row=1, column=0, padx=10, pady=(0,10), sticky='w')
        self.checkbox3 = customtkinter.CTkCheckBox(self, text="Só quer mamão so quer mel?")
        self.checkbox3.grid(row=2, column=0, padx=10, pady=(0,10), sticky='w')

    def get(self):
        if self.checkbox1.get() == 1:
            print("Ta nada")
        if self.checkbox2.get() == 1:
            print("ta mesmo")
        if self.checkbox3.get() == 1:
            print("Hurum")

class APP(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #Info. geral
        self.geometry("400x320")
        self.title("ANTI-PROCASTINATOR 1.0")
        self.grid_columnconfigure((0, 1), weight=1)
        #self.grid_rowconfigure((0,1), weight=1)
        #app.grid_columnconfigure(1, weight=1) mais de uma coluna

        #Estudando os widgets
        self.botao = customtkinter.CTkButton(self, text="Ta procastinando?" , command=self.resposta_primeiro_botao)
        self.botao.grid(row=0, column=0, pady=(0,20), sticky='ew', columnspan=2) #sticky='' esticar algo na propria coluna
        #columnspan=2 fica em duas colunas

        #criando o frame e mandando o chefe "master"
        self.frame_principal = FramePrimario(self)
        self.frame_principal.grid(row=1, column=0, pady=(0,20), sticky='nws')

    def resposta_primeiro_botao(self):
        self.frame_principal.get()


app = APP()
app.mainloop()