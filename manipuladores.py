import pyodbc
from condominios import *

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\SHARMAQ\SHOficina\dados.mdb; PWD=!(&&!!)&')
cursor = conn.cursor()

def servicos(n):  # puxa os servicos feitos na OS.n
    n = str(n)
    select = cursor.execute('select DESCRICAO, TOTAL from OS_SERVICOS where OS_NUM = ' + n + '')
    l = []
    valor = [] #valor total de servicos
    for row in select.fetchall():
        l.append(row[0])
        l.append(row[1])
        valor.append(row[1])
        with open("arquivos_txt/email.txt", "a") as arquivo:
            arquivo.write(f"\n     {row[0]} R${row[1]:.2f}")

    return valor


def pecas(n):  # puxa as pecas da OS.n
    n = str(n)
    select = cursor.execute('select DESCRICAO, VALOR from OS_PECAS where COD_OS = ' + n + '')
    l = []
    valor = [] #valor total de pecas
    for row in select.fetchall():
        l.append(row[0])
        l.append(row[1])
        valor.append(row[1])
        with open("arquivos_txt/email.txt", "a") as arquivo:
            arquivo.write(f"\n     {row[0]} R${row[1]:.2f}")

    return valor

def valor_total(os):
    valor_servico = servicos(os)
    valor_total_servico = 0

    for e in valor_servico:
        valor_total_servico += e

    valor_pecas = pecas(os)
    valor_total_pecas = 0

    for e in valor_pecas:
        valor_total_pecas += e

    valor_total = valor_total_servico + valor_total_pecas
    with open("arquivos_txt/email.txt", "a") as arquivo:
        arquivo.write(f"\n     TOTAL: R${valor_total:.2f}")

    return valor_total
