import sqlite3 as lite
import pandas as pd #precisa instalar esse módulo e o módulo do openpyxl para exportar

con = lite.connect('dados.db')
#inserir informações no Bd

def inserir_dados(insert):
    with con:
        cur = con.cursor()
        query = "INSERT INTO produto(codigo, nome, modelo, fabricante, custo, quantidade, data) VALUES(?,?, ?, ?, ?, ?, ?)"
        cur.execute(query,insert)

def acessar_dados():
    with con:
        cur = con.cursor()
        query = "SELECT * FROM produto "
        cur.execute(query)
        dados = cur.fetchall() #pegar todos os itens do bd 
        
    return dados       

def atualizar_dados(insert):
    with con:
        cur = con.cursor()
        query = "UPDATE produto SET nome=?, modelo=? , fabricante=?, custo=?, quantidade=?, data=? WHERE codigo =?"
        cur.execute(query,insert)

def deletar_dados(i): 
    with con:
        cur = con.cursor()
        query = "DELETE FROM produto WHERE codigo=?"
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

def exportar_excel_tudo():
    with con:
        cur = con.cursor()
        query = "SELECT * FROM produto "
        cur.execute(query)
        dados = cur.fetchall() #pegar todos os itens do bd 
        clientes_exportados = pd.DataFrame(dados, columns=['Código','Nome', 'Modelo', 'Fabricante', 'Custo', 'Quantidade', 'Data de Cadastro'])
        clientes_exportados.to_excel('relatorio_estoque.xlsx')

def exportar_excel_pesquisar(i):
    with con:
        cur = con.cursor()
        query = f"SELECT * FROM produto WHERE nome LIKE '%{i}%'"
        cur.execute(query)
        dados = cur.fetchall() #pegar todos os itens do bd 
        clientes_exportados = pd.DataFrame(dados, columns=['Código','Nome', 'Modelo', 'Fabricante', 'Custo', 'Quantidade', 'Data de Cadastro'])
        clientes_exportados.to_excel('relatorio_estoque.xlsx')