import sqlite3

conn = sqlite3.connect('banco.db')
conn.row_factory = sqlite3.Row

res = conn.execute("SELECT * FROM users")
lista = res.fetchall()

# pessoa[1]
for pessoa in lista:
    print(pessoa['nome'])
conn.close()