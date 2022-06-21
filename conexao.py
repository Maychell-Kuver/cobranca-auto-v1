from manipuladores import *
import pyodbc
from tkinter import *

"""
Códigos de Clientes
CODIGO	NOME
419	CONDOMÍNIO CAMINHO DO REI
583	CONDOMINIO HORIZONTAL PRAIA DA BARRA
679	CONDOMINIO HORIZONTAL CAMINHO DO REI
1782	CONDOMINIO SOL POENTE
2143	CONDOMINIO POMARES DE GAROPABA
2188	CONDOMÍNIO BELA VISTA MIRADOURO
2374	CONDOMINIO BELA VISTA MORRINHOS
2578	CONDOMINIO BELA VISTA RESERVA
3228	CONDOMÍNIO ROSA INTERNACIONAL
3951	CONDOMÍNIO FERRUGEM PRIVATE RESIDENCE
3997	CONDOMÍNIO ACQUALINA LAKE CLUB
4084	CONDOMÍNIO RESIDENCIAL MAR AZUL

Cada Condominio tem que ter email, cnpj, razao social

\
"""



def cobrar(condo):


    janela2 = Toplevel()
    janela2.title("Ordens de Serviço")
    janela2.geometry("400x400")
    janela2.configure(bg="#7887AB")
    conn = pyodbc.connect(
        r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\maych\Documents\cobranca_auto-v1.0\dados.mdb; PWD=!(&&!!)&')
    cursor = conn.cursor()
    label_os = Label(janela2, text="Número de OS", width=20, bg="#7887AB")
    label_os.pack()

    os_numero = Entry(janela2)
    os_numero.pack(padx=10, pady=10)

    labelTotal = Button(janela2, text="0", width=20)

    def cobrar_os():
        n = os_numero.get()
        with open("arquivos_txt/email.txt", "a") as arquivo:
            arquivo.write(f"\n\nOS.{n}")
        valor_total_os = valor_total(n)
        counter = float(str(labelTotal['text']))
        counter += float(valor_total_os)
        labelTotal.config(text=str(counter))

    def voltar_inicio():
        total_geral = float(str(labelTotal['text']))
        with open("arquivos_txt/email.txt", "a") as arquivo:
            arquivo.write(f"\n\nTOTAL GERAL: R${total_geral:.2f}")
        janela2.destroy()

    valor = 0
    btn_cobrar= Button(janela2, text="Cobrar OS", command=cobrar_os, width=20)
    btn_cobrar.pack(padx=10, pady=10)

    btn_voltar1= Button(janela2, text="Voltar", command=voltar_inicio, width=20)
    btn_voltar1.pack(padx=10, pady=10)


    with open("arquivos_txt/email.txt", "a") as arquivo:
        arquivo.write(f"\n\n{condo}")

    labelTotal.pack(padx=10, pady=10)
