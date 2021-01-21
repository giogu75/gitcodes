import sqlite3

nome = input('>Nome: ')

idade = int(input ('>Idade: '))

email = input ('>Email: ')

banco = sqlite3.connect('primeiro_banco.db') #objeto de conexão com o banco

cursor = banco.cursor()

# cursor.execute("CREATE TABLE pessoas(Nome text, Idade integer, email text)")
#  #cria a tabela - rodar uma vez e depois comentar essa linha
cursor.execute("INSERT INTO pessoas VALUES('"+nome+"','"+str(idade)+"', '"+email+"')")

banco.commit()

