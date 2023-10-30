
import sqlite3 as lite

#criando conexão
con = lite.connect('dados.db')

#criando tabela
with con: #abre e fecha bd automaticamente
    cur = con.cursor()
    cur.execute("CREATE TABLE produto(codigo INTEGER PRIMARY KEY , nome VARCHAR(50),modelo VARCHAR(15), fabricante VARCHAR(15), custo DECIMAL(10, 2), quantidade INT, data DATE)")


