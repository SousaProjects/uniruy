from tkinter import *
from tkinter import ttk #usado para scrollbar
from tkinter import messagebox
from datetime import datetime #usado para pegar a data e hora atual e inserir no formulário
import view #modulo com as funções de BD
import pandas as pd #modulo para exportar dados excel

####Paleta de cores###
co0 = "#565656"   # Preta
co1 = "#feffff"   # branca
co2 = "#4fa882"   # verde
co3 = "#38576b"   # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

#Criando Janela
janela = Tk()
janela.title("Sismat - Sistema de Materiais v23.1 - Desenvolvido pela Equipe 02")
janela.geometry("1050x465")
janela.configure(background=co9)
janela.resizable(False, False)

#divindo a janela em frames

frame_cima = Frame(janela, width=370, height=57, bg=co0, relief="flat")
frame_cima.grid(row=0,column=0)

frame_baixo = Frame(width=370, height=403, bg=co1, relief="flat")
frame_baixo.grid(row=1,column=0, padx=0, pady=1, sticky=NSEW)

frame_direita_cima = Frame(width=650, height=19, bg=co0, relief="flat")
frame_direita_cima.grid(row=0, column=1, rowspan=2, padx=1,pady=0, sticky=NSEW)

frame_direita = Frame(janela, width=650, height= 440, relief="flat")
frame_direita.grid(row=1, column=1, rowspan=2, padx=1,pady=0, sticky=NSEW)

#Ajustes de imagem de logotipo
imagem = PhotoImage(file="./estoque.png")
imagem_cima = Label(janela, image=imagem, bg=co0)
imagem_cima.place(x=0, y=0)

#configurações dos frames de cima
    
texto_cima = Label(frame_cima, text='Sismat - Sistema de Materiais', font=('Arial 12 bold'), fg=co1, bg=co0)
texto_cima.place(x=75, y=17)

texto_pesquisa = Label(frame_direita_cima,text="Digite o nome do Produto :", font=("Arial 10 bold"), bg=co0, fg="white")
texto_pesquisa.place(x=15, y=15)

entry_pesquisa = Entry(frame_direita_cima, width=45, justify='left', relief='sunken' )
entry_pesquisa.place(x=195, y=16)

########### Dados do formulário ###########

#Nome
label_nome = Label(frame_baixo, text='Nome do Produto*', font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
label_nome.place(x=10, y=10)
entry_nome = Entry(frame_baixo, width=55, justify='left', relief='solid')
entry_nome.place(x=13, y=40)

#Modelo Produto
label_modelo = Label(frame_baixo, text='Modelo do Produto*', font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
label_modelo.place(x=13, y=70)
entry_modelo = Entry(frame_baixo, width=55, justify='left', relief='solid')
entry_modelo.place(x=13, y=100)

#Fabricante
label_fabricante = Label(frame_baixo, text='Fabricante do Produto*', font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
label_fabricante.place(x=13, y=130)
entry_fabricante = Entry(frame_baixo, width=55, justify='left', relief='solid')
entry_fabricante.place(x=13, y=160)

#Custo
label_custo = Label(frame_baixo, text='Custo do Produto*', font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
label_custo.place(x=13, y=190)
entry_custo = Entry(frame_baixo, width=25, justify='left', relief='solid')
entry_custo.place(x=13, y=220)

#Quantidade
label_quantidade = Label(frame_baixo, text='Quantidade*', font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
label_quantidade.place(x=185, y=190)
entry_quantidade = Entry(frame_baixo, width=25, justify='left', relief='solid')
entry_quantidade.place(x=185, y=220)

#Data
def data_atual():
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
    return data_atual

label_data = Label(frame_baixo, text='Data/Hora de Cadastro :', font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
label_data.place(x=13, y=290)
entry_data = Label(frame_baixo, width=20, text=data_atual(), font=("Arial 10 bold"), justify='left', relief='solid', fg="white", background="grey")
entry_data.place(x=180, y=290)

# Função Inserir
def inserir():
    
    global custo, quantidade
    
    #criando o código do produto com data, hora, min e segundos
    cod_produto = datetime.now().strftime("%d/%m/%y %H:%M:%S") #Retorna data completa com min e segundos
    cod_produto = cod_produto.replace('/','') #substituição 01
    cod_produto = cod_produto.replace(' ','') #substituição 02
    cod_produto = cod_produto.replace(':','') #substituição 03

    codigo = cod_produto
    
    #Manipulando as entradas para inserir os dados como letra maiuscula e remover os espacos adicionais
    
    nome = entry_nome.get().strip().upper()
    modelo = entry_modelo.get().strip().capitalize().upper()
    fabricante = entry_fabricante.get().strip().capitalize().upper()
    data = data_atual()
    
    #Validação se os dados estão em branco
    
    if nome == "" or modelo == "" or fabricante == "":
        messagebox.showerror('Erro', 'Verifique se todos os campos foram preenchidos')
    else:
        #Validação se o custo está como número
        try:
            custo = float(entry_custo.get())
        except ValueError:
            messagebox.showerror('Erro', 'Insira o valor correto em custo')
            
        #Validação se a quantidade está como número
        try:
            quantidade = int(entry_quantidade.get())
        except ValueError:
            messagebox.showerror('Erro', 'Insira o valor correto em quantidade')
        else:
            lista = [codigo, nome, modelo, fabricante, custo, quantidade, data]
            view.inserir_dados(lista)

            messagebox.showinfo('Sucesso', 'Produto cadastrado com Sucesso!')
            
        #Limpar os campos do formulário, do início ao fim
            
            entry_nome.delete(0, END)
            entry_modelo.delete(0, END)
            entry_fabricante.delete(0, END)
            entry_custo.delete(0, END)
            entry_quantidade.delete(0, END)

        #função para apagar todos os dados da lista no Frame Direita
        for widget in frame_direita.winfo_children():
            widget.destroy()
            
        #função para reinserir os dados, nesse caso vai vir atualizado com o dado inserido
        mostrar()

#Limpar a barra de pesquisa de itens

def limpar_pesquisa():
    entry_pesquisa.delete(0, END)
    mostrar()

#Função para atualizar o item selecionado na lista

def atualizar_main():
    try:
        #Pegar os dados do item focado e trazer como dicionário
        
        treev_dados = tree.focus() #Pegar todos os dados do item focado
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario["values"]
        
        print(treev_dados)
        #Limpar os campos do formulário, do início ao fim
        
        entry_nome.delete(0,END)
        entry_modelo.delete(0,END)
        entry_fabricante.delete(0,END)
        entry_custo.delete(0,END)
        entry_quantidade.delete(0,END)
        
        entry_codigo = tree_lista[0]
        entry_nome.insert(0,tree_lista[1])
        entry_modelo.insert(0,tree_lista[2])
        entry_fabricante.insert(0,tree_lista[3])
        entry_custo.insert(0,tree_lista[4])
        entry_quantidade.insert(0,tree_lista[5])
        
        def atualizar():
            codigo = tree_lista[0]
            nome = entry_nome.get().strip().upper()
            modelo = entry_modelo.get().strip().upper()
            fabricante = entry_fabricante.get().upper()
            custo = entry_custo.get().strip()
            quantidade = entry_quantidade.get().strip()
            data = data_atual()
            
            if nome == "" or modelo == "" or fabricante == "":
                messagebox.showerror('Erro', 'Verifique se todos os campos foram preenchidos')
            else:
                try:
                    custo = float(entry_custo.get())
                except ValueError:
                    messagebox.showerror('Erro', 'Insira o valor correto em custo')

                try:
                    quantidade = int(entry_quantidade.get())
                except ValueError:
                    messagebox.showerror('Erro', 'Insira o valor correto em quantidade')
                else:
                    
                    lista = [nome, modelo, fabricante, custo, quantidade, data, codigo]
                    view.atualizar_dados(lista)
                
                messagebox.showinfo('Sucesso', 'Produto atualizado com Sucesso!')
                entry_nome.delete(0,END)
                entry_modelo.delete(0,END)
                entry_fabricante.delete(0,END)
                entry_custo.delete(0,END)
                entry_quantidade.delete(0,END)
            
            for widget in frame_direita.winfo_children():
                widget.destroy()
                mostrar()
                
        button_confirmar = Button(frame_baixo, text='Confirmar',font=("Arial 10 bold"), width=12, bg="yellow", fg=co0, command=lambda:(atualizar(), limpar_pesquisa()))
        button_confirmar.place(x=240, y=351)
            
            
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um dos itens na tabela')

#função atualizar
def delete_item():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario["values"]
        codigo = [tree_lista[0]] # Os dados precisam estar em formato de lista
        
        view.deletar_dados(codigo)
        
        messagebox.showinfo('Sucesso', 'Produto excluído com sucesso!')
        
        for widget in frame_direita.winfo_children():
            widget.destroy()
            
        mostrar()
        
    except IndexError:
        
        messagebox.showerror('Erro', 'Selecione um dos itens na tabela')
    


#Função para limpar os campos do formulário
def limpar():
    
    entry_nome.delete(0,END)
    entry_modelo.delete(0,END)
    entry_fabricante.delete(0,END)
    entry_custo.delete(0,END)
    entry_quantidade.delete(0,END)

#Botões do formulário
button_cadastrar = Button(frame_baixo, text='Cadastrar', font=("Arial 10 bold"), width=12, bg=co2, fg=co1, command=inserir)
button_cadastrar.place(x=10, y=315)

button_alterar = Button(frame_baixo, text='Alterar',font=("Arial 10 bold"), width=12, bg="yellow", fg=co0, command=atualizar_main)
button_alterar.place(x=125, y=315)

button_remover = Button(frame_baixo, text='Remover',font=("Arial 10 bold"), width=12, bg="red", fg=co1, command=delete_item )
button_remover.place(x=240, y=315)

button_limpar = Button(frame_baixo, text = "Limpar Campos", font=("Arial 10 bold"), width=26, fg=co1, bg="grey" , command=limpar)
button_limpar.place(x=11, y=351)

def mostrar():
    
    global tree
    
    ##### importando a lista da view e inserindo na tabela ###
    lista = view.acessar_dados()

    #cabeçalho da lista
    cabecalho = ['Código', 'Nome do Produto','Modelo', 'Fabricante', 'Custo', 'Qtd', 'Data']

    #configurações de scrollbar da lista
    tree = ttk.Treeview(frame_direita, selectmode='extended', columns=cabecalho, show='headings')
    vsb = ttk.Scrollbar(frame_direita, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_direita.grid_rowconfigure(0, weight = 12)

    #alinhamento do texto de cabeçalho
    align_cabecalho = ["center","nw","center","nw","center","center","center"]

    #tamanho do texto de cabeçalho, por item
    size_cabecalho_item = [80,170,80,100,50,60,110]
    na = 0

    for col in cabecalho:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=size_cabecalho_item[na], anchor = align_cabecalho[na])
        na += 1
        

    for item in lista:
        tree.insert('','end', values=item)
        
def mostrar_pesquisa():
    
    global tree
    
    ##### importando a lista da view e inserindo na tabela ###
    pesquisa = entry_pesquisa.get()
    lista = view.pesquisar_dados(pesquisa)
    
    for widget in frame_direita.winfo_children():
        widget.destroy()

    #cabeçalho da lista
    cabecalho = ['Código', 'Nome do Produto','Modelo', 'Fabricante', 'Custo', 'Qtd', 'Data']

    #configurações de scrollbar da lista
    tree = ttk.Treeview(frame_direita, selectmode='extended', columns=cabecalho, show='headings')
    vsb = ttk.Scrollbar(frame_direita, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_direita.grid_rowconfigure(0, weight = 12)

    #alinhamento do texto de cabeçalho
    align_cabecalho = ["center","nw","center","nw","center","center","center"]

    #tamanho do texto de cabeçalho, por item
    size_cabecalho_item = [80,170,80,100,50,60,110]
    na = 0

    for col in cabecalho:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=size_cabecalho_item[na], anchor = align_cabecalho[na])
        na += 1
        

    for item in lista:
        tree.insert('','end', values=item)

def exportar():
    texto = entry_pesquisa.get()
    if len(texto) != 0:
        texto_pesquisado = entry_pesquisa.get()
        view.exportar_excel_pesquisar(texto_pesquisado)
        messagebox.showinfo('Concluído','Sua exportação foi salva com sucesso, verifique no diretório raiz!')
    else:
        view.exportar_excel_tudo()
        messagebox.showinfo('Concluído','Sua exportação foi salva com sucesso, verifique no diretório raiz!')
        
button_pesquisa = Button(frame_direita_cima, width=8, text="Pesquisar", command=mostrar_pesquisa)
button_pesquisa.place(x=490, y=12)

button_limpar_pesquisa = Button(frame_direita_cima, width=6, text="Limpar", command=lambda:(data_atual(),limpar_pesquisa()))
button_limpar_pesquisa.place(x=560, y=12) 

button_exportar = Button(frame_direita_cima, width=6, text="Exportar", bg="darkgreen", fg="white", command=exportar)
button_exportar.place(x=615, y=12)

mostrar()

janela.mainloop()