from tkinter import *
from tkinter import ttk #usado para scrollbar
from datetime import datetime #usado para pegar a data e hora atual e inserir no formulário
import view

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
janela.title("Sismat - Sistema de Materiais v2023.01")
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
texto_pesquisa.place(x=25, y=15)

entry_pesquisa = Entry(frame_direita_cima, width=50, justify='left', relief='sunken' )
entry_pesquisa.place(x=205, y=16)

button_pesquisa = Button(frame_direita_cima, width=15, text="Pesquisar")
button_pesquisa.place(x=520, y=12)


########### Dados do formulário ###########

#Nome
label_nome = Label(frame_baixo, text='Nome do Produto*', font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
label_nome.place(x=10, y=10)
entry_nome = Entry(frame_baixo, width=55, justify='left', relief='solid')
entry_nome.place(x=13, y=40)

#Modelo Produto
label_produto = Label(frame_baixo, text='Modelo do Produto*', font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
label_produto.place(x=13, y=70)
entry_produto = Entry(frame_baixo, width=55, justify='left', relief='solid')
entry_produto.place(x=13, y=100)

#Fabricante
label_fabricante = Label(frame_baixo, text='Fabricante do Produto*', font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
label_fabricante.place(x=13, y=130)
entry_fabricante = Entry(frame_baixo, width=55, justify='left', relief='solid')
entry_fabricante.place(x=13, y=160)

#Custo
label_custo = Label(frame_baixo, text='Custo do Produto*', font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
label_custo.place(x=13, y=190)
entry_custo = Entry(frame_baixo, width=55, justify='left', relief='solid')
entry_custo.place(x=13, y=220)

#Quantidade
label_quantidade = Label(frame_baixo, text='Quantidade*', font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
label_quantidade.place(x=13, y=250)
entry_quantidade = Entry(frame_baixo, width=55, justify='left', relief='solid')
entry_quantidade.place(x=13, y=280)

#Data
data_atual = datetime.now().strftime("%d/%m/%Y %H:%M")
label_data = Label(frame_baixo, text='Data/Hora de Cadastro :', font=('Arial 10 bold'), bg=co1, fg=co4, relief='flat')
label_data.place(x=13, y=310)
entry_data = Label(frame_baixo, width=20, text=data_atual, font=("Arial 10 bold"), justify='left', relief='solid', fg="white", background="grey")
entry_data.place(x=180, y=310)

#Função para limpar os campos do formulário
def limpar():
    entry_nome.delete(0,END)
    entry_produto.delete(0,END)
    entry_fabricante.delete(0,END)
    entry_custo.delete(0,END)
    entry_quantidade.delete(0,END)

#Botões do formulário
button_cadastrar = Button(frame_baixo, text='Cadastrar', font=("Arial 10 bold"), width=12, bg=co2, fg=co1)
button_cadastrar.place(x=10, y=337)

button_alterar = Button(frame_baixo, text='Alterar',font=("Arial 10 bold"), width=12, bg="yellow", fg=co0)
button_alterar.place(x=125, y=337)

button_remover = Button(frame_baixo, text='Remover',font=("Arial 10 bold"), width=12, bg="red", fg=co1 )
button_remover.place(x=240, y=337)

button_limpar = Button(frame_baixo, text = "Limpar Campos", font=("Arial 10 bold"), width=41, fg=co1, bg="grey" , command=limpar)
button_limpar.place(x=10, y=371)

##### lista de teste ###
lista = [
    [1, 'Tijolo Comum', 'TC100', 'Fábrica de Tijolos A', 0.25, 10000,"25/10/2023"],
    [2, 'Cimento Portland', 'CP2000', 'Cimentos ABC', 10.5, 500,"25/10/2023"],
    [3, 'Areia Fina', 'AF300', 'Areias de Construção XYZ', 6.0, 1500,"25/10/2023"],
    [4, 'Telha de Cerâmica', 'TC500', 'Telhas & Telhas Ltda.', 15.0, 300,"25/10/2023"],
    [5, 'Barra de Aço', 'BA400', 'Aços do Brasil SA', 20.0, 800,"25/10/2023"],
    [6, 'Madeira de Pinho', 'MP100', 'Madeireira Silva', 7.5, 600,"25/10/2023"],
    [7, 'Tinta Látex Branca', 'TLB50', 'Tintas & Cia.', 40.0, 100,"25/10/2023"],
    [8, 'Prego Galvanizado', 'PG75', 'Ferragens Martins', 0.05, 10000,"25/10/2023"],
    [9, 'Laje Pré-Moldada', 'LP700', 'Lajes S/A', 80.0, 50,"25/10/2023"],
    [10, 'Tubos de PVC', 'TPV50', 'Plásticos Ltda.', 2.0, 3000,"25/10/2023"],
    [11, 'Porta de Madeira', 'PM120', 'Portas Elegantes', 90.0, 30,"25/10/2023"],
    [12, 'Cerâmica para Pisos', 'CPP300', 'Revestimentos & Cia.', 12.5, 500,"25/10/2023"],
    [13, 'Vidro Temperado', 'VT150', 'Vidraçaria Moderna', 35.0, 200,"25/10/2023"],
    [14, 'Argamassa Colante', 'AC80', 'Argamassas Express', 8.5, 800,"25/10/2023"],
    [15, 'Canos de Cobre', 'CC40', 'Tubos de Cobre SA', 3.5, 4000,"25/10/2023"],
    [16, 'Luminária LED', 'LL100', 'Iluminação Eficaz', 25.0, 200,"25/10/2023"],
    [17, 'Torneira de Cozinha', 'TC50', 'Metais Sanitários B', 15.0, 300,"25/10/2023"],
    [18, 'Lã de Vidro Isolante', 'LVI80', 'Isolantes Térmicos S/A', 6.0, 600,"25/10/2023"],
    [19, 'Papel de Parede', 'PP200', 'Decorações Modernas', 20.0, 100,"25/10/2023"],
    [20, 'Telhas Metálicas', 'TM300', 'MetalTelhas Ltda.', 18.0, 400,"25/10/2023"],
    [21, 'Janela de Alumínio', 'JA90', 'Alumínio & Cia.', 50.0, 50,"25/10/2023"],
    [22, 'Fios Elétricos', 'FE100', 'Elétrica Brasil', 4.0, 1000,"25/10/2023"],
    [23, 'Tinta Esmalte', 'TE75', 'Tintas Duráveis', 45.0, 150,"25/10/2023"],
    [24, 'Parafusos de Aço', 'PA60', 'Fixadores Rápidos', 0.1, 8000,"25/10/2023"],
    [25, 'Pia de Granito', 'PG70', 'Granitos & Pedras', 75.0, 40,"25/10/2023"],
    [26, 'Interruptor de Luz', 'IL30', 'Componentes Elétricos ABC', 3.0, 500,"25/10/2023"],
    [27, 'Tubos de Ferro Fundido', 'TFF150', 'Ferragens Fortes', 10.0, 200,"25/10/2023"],
    [28, 'Portão de Garagem', 'PG120', 'Portões Resistentes SA', 120.0, 20,"25/10/2023"],
    [29, 'Ferramentas de Construção', 'FC200', 'Ferramentas & Ferragens', 25.0, 100,"25/10/2023"],
    [30, 'Calhas de Alumínio', 'CA80', 'Calhas e Rufos Ltda.', 5.0, 500,"25/10/2023"]
]

#cabeçalho da lista
cabecalho = ['ID', 'Nome do Produto', 'Modelo', 'Fabricante', 'Custo', 'Quantidade', 'Data']

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
size_cabecalho_item = [30,170,80,160,50,80,80]
na = 0

for col in cabecalho:
    tree.heading(col, text=col.title(), anchor=CENTER)
    tree.column(col, width=size_cabecalho_item[na], anchor = align_cabecalho[na])
    na += 1
    

for item in lista:
    tree.insert('','end', values=item)


janela.mainloop()