import customtkinter

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
        self.fonte_personalizada = customtkinter.CTkFont(family='Roboto', size=20, weight='bold')

        self.columnconfigure(0, weight=1)

        self.label_titulo = customtkinter.CTkLabel(self, text="Aplicativo anti-procastinação", 
                                                   font=self.fonte_personalizada, text_color='black')
        self.label_titulo.grid(row=0, column=0, padx=3, pady=3, ipadx=20)

#1.2
class FrameFuncoesTempo(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='#D9D9D9', width=230, height=250, corner_radius=30)

        self.columnconfigure(0, weight=1)

        self.frame_sessao = FrameSessao(self)
        self.frame_sessao.grid(row=0, column=0, padx=10, pady=(10, 90))
        self.grid_propagate(False)

#1.2.1
class FrameSessao(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='#9B9B9B', width=230, height=150)

        self.grid_propagate(False)
        self.columnconfigure((0,1,2), weight=1)

        #Label da sessão
        self.label_sessao_string = customtkinter.CTkLabel(self, text="Sessão", 
                                                          font=customtkinter.CTkFont(family='Roboto', size=18, weight='bold'), 
                                                          text_color="black")
        self.label_sessao_string.grid(row=0, column=0, pady=3, columnspan=3)

        #Label do timer
        self.label_timer = customtkinter.CTkLabel(self, text='30:00', 
                                                  font=customtkinter.CTkFont(family='Arial', size=50, weight='bold'), 
                                                  text_color="black")
        self.label_timer.grid(row=1, column=0, pady=3, columnspan=3)

        #Botões de controle do timer
        self.botao_iniciar = BotaoControle(self, "Iniciar")
        self.botao_iniciar.grid(row=2, column=0, padx=3, pady=(20, 10))

        self.botao_reiniciar = BotaoControle(self, "Reiniciar")
        self.botao_reiniciar.grid(row=2, column=1, padx=3, pady=(20, 10))

        self.botao_parar = BotaoControle(self, "Parar")
        self.botao_parar.grid(row=2, column=2, padx=3, pady=(20, 10))

#1.2.1.1 Botões
class BotaoControle(customtkinter.CTkButton):
    def __init__(self, master, tipo_botao):
        super().__init__(master, fg_color='#2D2E2C', width=65, height=25, text=tipo_botao)

#1.3
class FrameFrases(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color='#F7DECE', width=300, height=20, border_width=2)

        self.columnconfigure(0, weight=1)

        #Fonte pras frases
        self.fonte_para_frases = customtkinter.CTkFont(family='Times', size=16, slant='italic')

        self.label_frases = customtkinter.CTkLabel(self, text="O resultado do amanhã é o fruto do hoje.", 
                                                   font=self.fonte_para_frases, text_color='black')
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