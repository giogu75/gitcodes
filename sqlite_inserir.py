import sqlite3

tabela = input ('>Qual tabela: ')

campo1 = input('>CAMPO1: ')

campo2 = input ('>CAMPO2: ')

campo3 = input ('>CAMPO3: ')

banco = sqlite3.connect('primeiro_banco.db') #objeto de conexão com o banco

cursor = banco.cursor()

cursor.execute("INSERT INTO "+tabela+" VALUES('"+campo1+"','"+campo2+"', '"+campo3+"')")

banco.commit()

