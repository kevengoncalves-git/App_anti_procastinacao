import customtkinter

"""print("Esse é meu app anti-procastinação")


class FramePrimario(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.checkbox1 = customtkinter.CTkCheckBox(self, text="Ta rico?")
        self.checkbox1.grid(row=1, column=0, padx=10, pady=(0,10), sticky='w')
        self.checkbox2 = customtkinter.CTkCheckBox(self, text="Ta liso?")
        self.checkbox2.grid(row=2, column=0, padx=10, pady=(0,10), sticky='w')
        self.checkbox3 = customtkinter.CTkCheckBox(self, text="Só quer mamão so quer mel?")
        self.checkbox3.grid(row=3, column=0, padx=10, pady=(0,10), sticky='w')

        #Add um titulo no meu frame
        self.titulo = customtkinter.CTkLabel(self, text="Meu titulo", bg_color="gray")
        self.titulo.grid(row=0, column=0, padx=10, pady=(0,10), sticky='ew')

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
app.mainloop()"""

#1.
class FramePrincipal(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='#536D88', corner_radius=20)

        self.columnconfigure(0, weight=1)

        self.frame_titulo_inicial = FrameTituloInicial(self)
        self.frame_titulo_inicial.grid(row=0, column=0, padx=10, pady=10)

        self.frame_funcoes = FrameFuncoesTempo(self)
        self.frame_funcoes.grid(row=1, column=0, padx=40, pady= 5, sticky='ew')

        self.frame_frases = FrameFrases(self)
        self.frame_frases.grid(row=2, column=0, padx=10, pady=10, ipadx=90)

#1.1
class FrameTituloInicial(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='#F7DECE', width=200, height=20, border_width=2)

        #Minha fonte
        self.fonte_personalizada = customtkinter.CTkFont(family='Roboto', size=18, weight='bold')

        self.columnconfigure(0, weight=1)

        self.label_titulo = customtkinter.CTkLabel(self, text="Aplicativo anti-procastinação", 
                                                   font=self.fonte_personalizada, text_color='black')
        self.label_titulo.grid(row=0, column=0, padx=3, pady=3, ipadx=20)

#1.2
class FrameFuncoesTempo(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='#9B9B9B', width=180, height=250, corner_radius=30)

#1.3
class FrameFrases(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='#F7DECE', width=300, height=20, border_width=2)

        self.columnconfigure(0, weight=1)

        #Fonte pras frases
        self.fonte_para_frases = customtkinter.CTkFont(family='Times', size=16, slant='italic')

        self.label_frases = customtkinter.CTkLabel(self, text="Frase qualquer ", font=self.fonte_para_frases, text_color='black')
        self.label_frases.grid(row=0, column=0, padx=10, pady=3, ipadx=20)

class APP(customtkinter.CTk):
    def __init__(self):
        super().__init__(fg_color='#0F132E')

        #Informações sobre o aplicativo
        self.title("ANTI-PROCASTINATOR 1.0")
        self.geometry("450x420")
        self.resizable(False, False)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.frame_principal = FramePrincipal(self)
        self.frame_principal.grid(row=0,column=0, padx=20, pady=20, sticky='ewns')

app = APP()
app.mainloop()