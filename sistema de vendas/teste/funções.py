import PySimpleGUI as sg
import bd.conect as ct
conexao = ct.Connection()
lista_produtos = []
def listagem(tabela):
    pessoas = conexao.query(f'select * from {tabela}')
    for id, nome, preco in pessoas:
        lista_produtos.append(f'{id}: {nome} preço: {preco}')