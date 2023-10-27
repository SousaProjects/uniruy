import sqlite3 as lite

con = lite.connect('dados.db')
#inserir informações no B

def inserir_dados(insert):
    with con:
        cur = con.cursor()
        query = "INSERT INTO produto(nome, modelo, fabricante, custo, quantidade, data) VALUES(?, ?, ?, ?,? ,?)"
        cur.execute(query,insert)

def acessar_dados():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM produto "
        cur.execute(query)
        dados = cur.fetchall() #pegar todos os itens do bd
        
        for i in dados:
            lista.append(i)    
        
    return lista        

def atualizar_dados(insert):
    with con:
        cur = con.cursor()
        query = "UPDATE produto SET nome=?, modelo=? , fabricante=?, custo=?, quantidade=?, data=? WHERE id =?"
        cur.execute(query,insert)

def deletar_dados(i): 
    with con:
        cur = con.cursor()
        query = "DELETE FROM produto WHERE id=?"
        cur.execute(query,i)

def pesquisar_dados(i):
    lista = []
    with con:
        cur = con.cursor()
        query = f"SELECT * FROM produto WHERE nome LIKE '%{i}%'"
        cur.execute(query)
        dados = cur.fetchall() #pegar todos os itens do bd
        
        for item in dados:
            lista.append(item)    
        
    return lista 

        
