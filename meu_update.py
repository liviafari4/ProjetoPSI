import sqlite3

conn = sqlite3.connect('banco.db')
conn.row_factory = sqlite3.Row

sql="UPDATE users SET nome=? where nome=?"
nome="Flauber"
conn.execute(sql, ('Flauber jogador', nome))
conn.commit()
conn.close()

