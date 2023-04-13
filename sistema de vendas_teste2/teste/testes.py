import PySimpleGUI as sg
import bd.conect as ct
conexao = ct.Connection()

def listagem_p():
    '''
    Função que listas os produtos. Ela é chama no arquivo 'adicionar_vendas'.
    '''
    global lista_id
    global lista_de_produtos 
    global lista_nome
    lista_nome = []
    lista_de_produtos = []
    lista_id = []
    pessoas = conexao.query(f'select * from produto')
    for id, nome, preco in pessoas:
        lista = []
        lista.append(nome)
        lista_id.append(id)
        lista_nome.append(nome)
        lista_de_produtos.append(lista)
listagem_p()





