import sqlite3

conn = sqlite3.connect('banco.db')

nome = 'Icaro'
sql="INSERT INTO users(nome) values (?)"
conn.execute(sql, (nome,))
conn.commit()
conn.close()