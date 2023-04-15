import PySimpleGUI as sg
import conect as ct
import matplotlib.pyplot as plt # Biblioteca usada para fazer o gráfico
from Tabelas.Produtos import *
from Tabelas.Vendas import *
from tabela_fechamento_caixa import*

conexao = ct.Connection()
caixa = False
tempo_aberto = []
caixa_atual = 'Abrir Caixa'
sg.theme('Default')
sg.set_options(font=('Arial 12'), text_color='black')

layout = [  
            [sg.Text('Sistema de Vendas', font=('Arial 16'))],
            [sg.Button('Produtos', size=(25,0))],
            [sg.Button('Vendas', size=(25,0), button_color='grey')],
            [sg.Button('Fechamento de caixa', size=(25,0))],
            [sg.Button('Encerrar', size=(25,0))]
        ]

janela = sg.Window('Menu', layout, element_justification='c', size = (300,200))

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Encerrar': 
        break
    elif eventos == 'Produtos':
        janela.hide()
        produtos()
        janela.un_hide()
    elif eventos == 'Fechamento de caixa':
        janela.hide()
        #======================================================================================================================
        # Fechamento de caixa que eu não consegui exporta de outra pasta
        sg.theme('Default')
        sg.set_options(font=('Arial 12'), text_color='black')

        layout = [  
                    [sg.Text('Fechamento de Caixa', font=('Arial 16'))],
                    [sg.Button(f'{caixa_atual}', size=(25,0), key= 'Abrir Caixa')],
                    [sg.Button('Ver Caixas', size=(25,0))],
                    [sg.Button('Ver Grafico', size=(25,0))],
                    [sg.Button('Voltar', size=(25,0))]
                ]

        janela_c = sg.Window('Fechamento de caixa', layout, element_justification='c')

        while True:
            eventos, valores = janela_c.read()
            if eventos == sg.WIN_CLOSED or eventos == 'Voltar': 
                break
            
            if eventos == 'Abrir Caixa':
                if caixa == False:
                    janela_c['Abrir Caixa'].update('Fechar Caixa')
                    caixa_atual = 'Fechar Caixa'
                    tempo = str(conexao.query("SELECT CURRENT_TIME")[0][0])[0:8]
                    
                    maxId = conexao.query("SELECT COUNT(*) FROM fechamento_caixa")

                    try:
                        inicial = conexao.query(f'SELECT dinhfinal FROM fechamento_caixa WHERE id = {maxId[0][0]}')[0][0]
                    except:
                        inicial = '0'
                    print(inicial, type(inicial))

                    if type(inicial) != int and type(inicial) != str:
                        inicial = '0'
                    else:   
                        valor_i = ''
                        for v in inicial:
                            if v == 'R':
                                pass
                            elif v == '$':
                                pass
                            elif v == ',':
                                valor_i += '.'
                            
                            else:
                                valor_i += v
                        inicial = valor_i
                    
                    conexao.execute(f"INSERT INTO fechamento_caixa(id, horaabertura, dataabertura, dinhinicial, dinhrecebido) VALUES({maxId[0][0] + 1}, '{tempo}', CURRENT_DATE, {inicial}, 0)")
                    
                    caixa = True
                    sg.popup('Caixa Aberto')
                    janela['Vendas'].update(button_color='#0c2464')

                elif caixa == True: 
                    janela_c['Abrir Caixa'].update('Abrir Caixa')
                    caixa_atual = 'Abrir Caixa' 
                    maxId = conexao.query("SELECT max(id) FROM fechamento_caixa")  
                    dinhInicial = conexao.query("SELECT dinhinicial FROM fechamento_caixa")
                    dinhRecebido = conexao.query("SELECT dinhrecebido FROM fechamento_caixa")
                    dinhfinal = dinhInicial[0][0] + dinhRecebido[0][0]        
                    tempo = str(conexao.query("SELECT CURRENT_TIME")[0][0])[0:8]
                    conexao.execute(f"UPDATE fechamento_caixa SET horafecha = '{tempo}', datafecha = CURRENT_DATE, dinhfinal = dinhinicial + dinhrecebido WHERE id = {maxId[0][0]}")

                    sg.popup('Caixa Fechado')
                    caixa = False
                    janela['Vendas'].update(button_color='grey')
            elif eventos == 'Ver Caixas':
                listagem_C()  
                janela_c.hide()
                lista_caixa()
                janela_c.un_hide()

            elif eventos == 'Ver Grafico':
                # Chamando o gráfico
                lista_data = []
                lista_valores = []
                '''
                Aqui eu peguei a data final e o dinheiro recebido, para comparar quando cada caixa vendeu no seu dia.
                '''
                datas = conexao.query('SELECT datafecha FROM public.fechamento_caixa;')
                valores_recebido = conexao.query('SELECT dinhrecebido FROM public.fechamento_caixa;')
                # Quebrando a data para colocar em uma outra lista
                for d in datas:
                    d = str(d[0])
                    lista_data.append(d)
                # Transformando o dinheiro recebido em float
                for val in valores_recebido:
                    val = val[0]
                    valor_i = ''
                    for v in val:
                        if v == 'R':
                            pass
                        elif v == '$':
                            pass
                        elif v == ',':
                            valor_i += '.'
                        
                        else:
                            valor_i += v
                    lista_valores.append(float(valor_i))
                plt.plot(lista_data, lista_valores)
                plt.show()


        janela_c.close()
        #========================================================================================================================
        janela.un_hide()
    elif eventos == 'Vendas':
        if caixa == True:
            janela.hide()
            vendas()
            janela.un_hide()
        else:
            sg.popup('Caixa fechado')


janela.close()
