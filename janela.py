import time
from tkinter import *
from enviar_email import *
from tkinter.ttk import *
from conexao import *
import datetime as dt
import pyautogui
import time

def enviar_email():
    l = dt.date.today()
    mes = l.month
    ano = l.year
    enviar(cb_email.get(), mes, ano)


def obter():
    cobrar(cb_condo.get())
# JANELAS
btn = "#C0C0C0"
txt_dark = "#1C1C1C"

def refresh():
    janela.update_idletasks()

janela = Tk()
janela.title("Cobrança Condomínios")
janela.geometry("400x400")
janela.configure(bg="#7887AB")

lista_emails= ["condominiori@consultsc.com.br", "alessandra@azenha.com.br", "leonidossantospereira@gmail.com", "atendimento@jotasempreendimentos.com.br"]

lista_consult = ["CONDOMÍNIO ROSA INTERNACIONAL",]

lista_azenha = ["CONDOMÍNIO CAMINHO DO REI", "CONDOMÍNIO HORIZONTAL PRAIA DA BARRA", "CONDOMÍNIO HORIZONTAL CAMINHO DO REI", "CONDOMÍNIO POMARES DE GAROPABA", "CONDOMÍNIO BELA VISTA MIRADOURO", "CONDOMÍNIO BELA VISTA MORRINHOS", "CONDOMÍNIO BELA VISTA RESERVA","CONDOMÍNIO FERRUGEM PRIVATE RESIDENCE", "CONDOMÍNIO ACQUALINA LAKE CLUB",]

lista_lilico = ["COSTÃO EMPREENDIMENTOS IMOBILIÁRIOS"]

lista_jotas = ["JOTAS"]

# lista_condo = ["CONDOMÍNIO CAMINHO DO REI", "CONDOMÍNIO HORIZONTAL PRAIA DA BARRA", "CONDOMÍNIO HORIZONTAL CAMINHO DO REI", "CONDOMÍNIO SOL POENTE", "CONDOMÍNIO POMARES DE GAROPABA", "CONDOMÍNIO BELA VISTA MIRADOURO", "CONDOMÍNIO BELA VISTA MORRINHOS", "CONDOMÍNIO BELA VISTA RESERVA", "CONDOMÍNIO ROSA INTERNACIONAL", "CONDOMÍNIO FERRUGEM PRIVATE RESIDENCE", "CONDOMÍNIO ACQUALINA LAKE CLUB", "CONDOMÍNIO RESIDENCIAL MAR AZUL"]

#COMBOBOX EMAIL
cb_email = Combobox(janela, values=lista_emails, width=60)
cb_email.current(0)
cb_email.pack(padx=10, pady=10)

cb_condo = Combobox(janela, values="", width=60)
cb_condo.pack(padx=10, pady=10)

# COMBOBOX CONDOMINIOS
def atualizar():
    with open("arquivos_txt/email.txt", "w") as arquivo:
        arquivo.write(f"Olá,\n\nSegue relação de ordens de serviço em aberto do(s) condomínio(s):")

    if cb_email.get() == "condominiori@consultsc.com.br":
        cb_condo.config(values=lista_consult)
        cb_condo.current(0)
    elif cb_email.get() == "alessandra@azenha.com.br":
        cb_condo.config(values=lista_azenha)
        cb_condo.current(0)
    elif cb_email.get() == "leonidossantospereira@gmail.com":
        cb_condo.config(values=lista_lilico)
        cb_condo.current(0)
    elif cb_email.get() == "atendimento@jotasempreendimentos.com.br":
        with open("arquivos_txt/email.txt", "w") as arquivo:
            arquivo.write(f"Olá,\n\nSegue relação de ordens de serviço em aberto:")
        cb_condo.config(values=lista_jotas)
        cb_condo.current(0)

btn_cobrar = Button(janela, text="Adicionar Ordem de Serviço", command=obter, width=30)
btn_cobrar.pack(padx=10, pady=10)

btn_att = Button(janela, text="Atualizar", command=atualizar, width=30)
btn_att.pack(padx=10, pady=10)

btn_enviar = Button(janela, text="Enviar Email", command=enviar_email, width=30)
btn_enviar.pack(padx=10, pady=10)



janela.mainloop()
