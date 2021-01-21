import sqlite3


campo = input ('SUBSTITUIR DADOS DO CAMPO: ')

valor = input('NOVO VALOR DO CAMPO: ')

campo2 = input ('LOCALIZAR CAMPO A SER SUBSTITUIDO: ')

valor2 = input ('VALOR DO CAMPO A SER SUBSTITUÍDO: ')

try:

    banco = sqlite3.connect('primeiro_banco.db') #objeto de conexão com o banco

    cursor = banco.cursor()

    #cursor.execute("UPDATE pessoas SET Nome = 'Fábio' WHERE Idade = 65")
    cursor.execute("UPDATE pessoas SET "+campo+" = '"+valor+"' WHERE "+campo2+" = '"+valor2+"'") 

    banco.commit()

except sqlite3.Error as erro:

    print('Erro ao localizar: ', erro)
