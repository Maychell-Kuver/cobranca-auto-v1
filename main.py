import pyodbc

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\maych\Documents\cobranca_auto-v1.0\dados.mdb; PWD=!(&&!!)&')
cursor = conn.cursor()
cursor.execute('select * from ORDEMS')

for row in cursor.fetchall():
    print(row)
