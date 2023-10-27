import sqlite3 as lite

con = lite.connect('dados.db')
lista = ['Calhas de Alumínio', 'CA80', 'Calhas e Rufos Ltda.', 5.0, 500,"25/10/2023"]
#inserir informações no B

def inserir_dados():
    with con:
        cur = con.cursor()
        query = "INSERT INTO produto(nome, modelo, fabricante, custo, quantidade, data) VALUES(?, ?, ?, ?,? ,?)"
        cur.execute(query,lista)

def acessar_dados():
    with con:
        cur = con.cursor()
        query = "SELECT * FROM produto "
        cur.execute(query)
        info = cur.fetchall() #pegar todos os itens do bd
        print(info)

def atualizar_dados():

    lista = ['Pedro',4]    
    with con:
        cur = con.cursor()
        query = "UPDATE produto SET nome=? WHERE id =?"
        cur.execute(query,lista)

def apagar_dados():
    lista = [2]    
    with con:
        cur = con.cursor()
        query = "DELETE FROM produto WHERE id=?"
        cur.execute(query,lista)
        

acessar_dados()
