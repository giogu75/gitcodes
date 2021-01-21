import sqlite3

campo = input ('DELETAR DADOS DO CAMPO: ')

valor = input('VALOR DO CAMPO: ')

banco = sqlite3.connect('primeiro_banco.db')# objeto de conexão com o banco

cursor = banco.cursor()

try:

    cursor.execute("DELETE FROM pessoas WHERE "+campo+" = '"+valor+"'") 

    banco.commit()

    banco.close()

    print('Os dados foram removidos com sucesso!!')

except sqlite3.Error as erro:

    print('Erro ao excluir: ', erro)
