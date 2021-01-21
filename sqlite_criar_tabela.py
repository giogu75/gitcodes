import sqlite3

nome = input('NOME DA TABELA: ')

campo1 = input ('CAMPO 1: ')
campo2 = input ('CAMPO 2: ')
campo3 = input ('CAMPO 3: ')

banco = sqlite3.connect('primeiro_banco.db') #objeto de conexão com o banco

cursor = banco.cursor()

cursor.execute("CREATE TABLE "+nome+"("+campo1+" text, "+campo2+" text, "+campo3+" text)")

print(f'Tabela {nome} criada com sucesso!')

banco.commit()
