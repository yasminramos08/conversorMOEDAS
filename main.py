#janela => 500 x 500
#título 
#campos para selecionar as moedas de origem e destino 
#botão para converter 
#lista de exibição com os nomes das moedas 

#importar a biblioteca que vai fazer a janela 
import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

#criar e configurar a jenela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("700x700")
janela.title("Conversor de Moedas")
janela.iconbitmap("coco.ico")

dic_conversoes_disponiveis= conversoes_disponiveis() 

#criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("Old English Text MT", 25), text_color="#468faf")
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem", font=("Book Antiqua", 16), text_color="#89c2d9")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino", font=("Book Antiqua", 16), text_color="#89c2d9")

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])
    
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()), command= carregar_moedas_destino, font=("Century Gothic", 16), text_color="light blue")
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values= ["Selecione uma moeda de origem"], font=("Century Gothic", 16), text_color="light blue")

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} = {cotacao} {moeda_destino}")


botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda, font=("Old English Text MT", 26),fg_color="#0353a4", text_color="#89c2d9")

lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")

moedas_disponiveis = nomes_moedas()

for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()

#colocar elementos criados na tela
titulo.pack(padx=10, pady=20)
texto_moeda_origem.pack(padx=10, pady=0)
campo_moeda_origem.pack(padx=10, pady=10)
texto_moeda_destino.pack(padx=10, pady=0)
campo_moeda_destino.pack(padx=10, pady=10)
botao_converter.pack(padx=10, pady=10)
texto_cotacao_moeda.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

#rodar a janela 
janela.mainloop()



