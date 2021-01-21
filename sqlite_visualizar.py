import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())