import PySimpleGUI as sg
import bd.conect as ct
conexao = ct.Connection()    
from teste.testes import*


def valor_produto():
    '''
    Tentativa de fazer uma função para transformar 'money' em float. Tentativa falha.
    '''
    global id_produto
    valor = ''
    pessoas = conexao.query('SELECT id, nome, preco FROM "produto" p')
    for id, nome, preco in pessoas:
        if id == id_produto:
            valor = ''
            for v in preco[2:-1]:
                if v == ',':
                    valor+= '.'
                else:
                    valor += v

valor_produto()