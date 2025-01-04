import FreeSimpleGUI as sg
import Funções as fc
import threading as mp

#Definição das cores 
escuro = '#8C6057'
claro = '#FAF3E0'
tijolo = '#DC143C'

#Janela Erro
def janelaErro(tipoerro):
    layout=[
        [sg.Text(tipoerro,background_color=claro,font = ("Cooper Hewitt",12), text_color=escuro)], 
        [sg.Button("Ok", button_color=(claro,escuro),font = ('Cooper Hewitt',12))]
        ]
    window= sg.Window(title="Janela Erro",background_color=claro, default_element_size=(15,1)).Layout(layout)

    stop=False  
    while not stop:
        evento, valor = window.read()
        if evento == "Ok" or evento == sg.WIN_CLOSED:
            stop = True
    window.close()

def interface_grafica():
    Guardada = 0
    BD = None

    esquerda_layout = [
        [sg.Push(background_color=claro)],
        [sg.Text("Sistema de Consulta e Análise de Publicações Científicas",
                 font=("Cambria", 30, "bold"), text_color=escuro, background_color=claro,
                 justification="center", size=(25, 2), expand_x=True)],
        [sg.Push(background_color=claro)],
        [sg.Push(background_color=claro),
         sg.Button("Sair", size=(10, 1), font=("Cambria", 14),
                   button_color=(claro,tijolo), key="-SAIR-"),
         sg.Button("Help", size=(10, 1), font=("Cambria", 14),
                   button_color=(claro, escuro), key="-HELP-"),
         sg.Push(background_color=claro)]
    ]
    
    menu_layout = [
        [sg.Text("Menu", font=("Cambria", 25), text_color=escuro,
                 background_color=claro, justification="center", size=(25, 1))],
        [sg.Column(
            [[sg.Button("Carregar BD", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-CARREGAR-"),
              sg.Button("Gravar BD", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-GRAVAR-")],
             [sg.Button("Consultar Publicação", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-CONSULTAR-"),
              sg.Button("Analisar Publicações", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-LISTAGEM-")],
             [sg.Button("Importar Dados", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-IMPORTAR-"),
              sg.Button("Exportação Parcial", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-EXPORTAR-")],
             [sg.Button("Atualizar Publicação", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-ATUALIZAR-"),
              sg.Button("Criar Publicação", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-CRIAR-")],
             [sg.Button("Estatísticas", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-ESTATISTICAS-"),
              sg.Button("Eliminar Publicação", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-ELIMINAR-")]],background_color=claro, element_justification="center")],
             [sg.Text("", size=(60, 1), font=("Cambria", 16), justification="center", key="-DADOS-",
                 background_color=claro, text_color=escuro)]
             ]
    
    layout = [
        [sg.Column(esquerda_layout, background_color=claro, vertical_alignment="center", element_justification="left"),
         sg.VSep(),
         sg.Column(menu_layout, background_color=claro, vertical_alignment="center", element_justification="center", expand_y=True)]
    ]

    window = sg.Window("Sistema de Consulta e Análise de Publicações Científicas", layout,resizable=True,
                       background_color=claro)

    stop = False

    while stop == False:

        eventos, valores = window.read()
        
        if eventos in [sg.WIN_CLOSED, '']:
            stop = True

        elif eventos == '-SAIR-':
            stop = True
            window.close()

        #Carregar Dataset
        elif eventos == "-CARREGAR-":  
            window["-DADOS-"].update("A carregar a base de dados...")
            layout_carregar = [
                [
                sg.Text("Base de dados:", font=("Cooper Hewitt", 12), pad=(0, 30), text_color=claro, background_color=escuro),
                sg.InputText(key="-FICHEIRO-", readonly=True, enable_events=True, text_color=escuro),
                sg.FileBrowse(file_types=[("JSON (*.json)", "*.json")], size=(8, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                sg.Button(key="-CARREGAR-", button_text="Carregar", size=(12, 1), disabled=True, font=("Cooper Hewitt", 12), button_color=(claro, escuro)) 
                ]
            ]

            wform = sg.Window('Carregamento da base de dados',layout_carregar, size=(650,100), background_color=claro)

            stopform = False
            while not stopform:
                inputEvent, inputValues = wform.read()
                if inputEvent == sg.WIN_CLOSED:
                    window["-DADOS-"].update("")
                    stopform = True
                elif inputEvent == '-FICHEIRO-':
                    wform["-CARREGAR-"].update(disabled=False)
                elif inputEvent == "-CARREGAR-":
                    if inputValues['Browse']:
                        BD = fc.carregar_dataset(inputValues['Browse'])
                        nome = inputValues['Browse']
                        stopform = True
                        window["-DADOS-"].update("Base de dados carregada com sucesso!")
                        wform.close()
        
        #Guardar Dataset
        elif eventos == "-GRAVAR-":
            window["-DADOS-"].update("A gravar base de dados...")
            
            if BD == None:
                janelaErro("Introduza primeiro uma base de dados!")
            
            else:
                Guardada = 1
                fc.guardar_dataset(nome, BD)
                window["-DADOS-"].update("Base de dados gravada!")
        
        #Consultar publicações
        elif eventos == "-CONSULTAR-":
            window["-DADOS-"].update("Preparar para consultar...")
            if BD is None:
                janelaErro("Introduza primeiro uma base de dados!")
                return
            elif Guardada == 0:
                janelaErro("Guarde primeiro a base de dados!")
                return

            layout_consultar = [
                [sg.Text('Deseja consultar a publicação por:', size=(45, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), 
                        background_color=claro, text_color=escuro)],
                [sg.Button('Título', size=(17, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                sg.Button('Autor', size=(17, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                sg.Button('Afiliação', size=(17, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                sg.Button('Data de publicação', size=(17, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                sg.Button('Palavras-chave', size=(17, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                sg.Button('Retornar ao Menu', font=("Cooper Hewitt", 12), size=(17, 1), button_color=(claro, tijolo))]
            ]

            window8 = sg.Window(title="Consultar Publicação", resizable=False, background_color=claro).Layout(layout_consultar)

            continue_reading = True
            while continue_reading:
                event, values = window8.read()
                if event in (sg.WINDOW_CLOSED, 'Retornar ao Menu'):
                    continue_reading = False  
                    window8.close()
                elif event == "Título":
                    resultados = []
                    formLayout = [
                        [sg.Text('Título:', size=(15, 1), font=("Cooper Hewitt", 12, "bold"), justification="left", background_color=claro, text_color=escuro),
                        sg.InputText(key='-TITULO-', size=(65, 10))],
                        [sg.Text('Deseja ordenar por data de publicação ou por título?', font=("Cooper Hewitt", 12), background_color=claro, text_color=escuro),
                        sg.Radio("Data de publicação", "OPCAO", default=False, key="-OPC1-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro),
                        sg.Radio("Título", "OPCAO", default=True, key="-OPC2-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro)],
                        [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))],
                        [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                        [sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                    ]

                    wform = sg.Window('Digite o título', formLayout, size=(700, 400), modal=True, resizable=False, background_color=claro)
                    reading_form = True

                    while reading_form:
                        event_form, values_form = wform.read()

                        if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                            reading_form = False  
                            wform.close()
                        elif event_form == 'Consultar':
                            if values_form['-TITULO-']:
                                if values_form['-OPC1-']:
                                    res = fc.filtertitle_ordenadodate(BD, values_form['-TITULO-'])
                                    if res:
                                        resultados.extend(res)  
                                        window["-DADOS-"].update("Publicação consultada com sucesso!")
                                    else:
                                        resultados.append("A publicação que procurou não existe!")
                                    wform['-RESULTADOS-'].update(values=resultados)

                                else:
                                    res = fc.filtertitle_ordenadotitle(BD, values_form['-TITULO-'])
                                    if res:
                                        resultados.extend(res)  
                                        window["-DADOS-"].update("Publicação consultada com sucesso!")
                                    else:
                                        resultados.append("A publicação que procurou não existe!")
                                    wform['-RESULTADOS-'].update(values=resultados)


                        
                elif event == "Autor":
                    resultados = []
                    formLayout = [
                        [sg.Text('Autor:', size=(15, 1), font=("Cooper Hewitt", 12, "bold"), justification="left", background_color=claro, text_color=escuro),
                        sg.InputText(key='-AUTOR-', size=(65, 10))],
                        [sg.Text('Deseja ordenar por data de publicação ou por título?', font=("Cooper Hewitt", 12), background_color=claro, text_color=escuro),
                        sg.Radio("Data de publicação", "OPCAO", default=False, key="-OPC1-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro),
                        sg.Radio("Título", "OPCAO", default=True, key="-OPC2-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro)],
                        [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))],
                        [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                        [sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                    ]

                    wform = sg.Window('Digite o autor', formLayout, size=(700, 400), modal=True, resizable=False, background_color=claro)
                    reading_form = True

                    while reading_form:
                        event_form, values_form = wform.read()

                        if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                            reading_form = False  
                            wform.close()
                        elif event_form == 'Consultar':
                            if values_form['-AUTOR-']:
                                if values_form['-OPC1-']:
                                    res = fc.filterauthor_ordenadodate(BD, values_form['-AUTOR-'])
                                    if res:
                                        resultados.extend(res)  
                                        window["-DADOS-"].update("Publicação consultada com sucesso!")
                                    else:
                                        resultados.append("A publicação que procurou não existe!")
                                    wform['-RESULTADOS-'].update(values=resultados)

                                else:
                                    res = fc.filterauthor_ordenadotitle(BD, values_form['-AUTOR-'])
                                    if res:
                                        resultados.extend(res)  
                                        window["-DADOS-"].update("Publicação consultada com sucesso!")
                                    else:
                                        resultados.append("A publicação que procurou não existe!")
                                    wform['-RESULTADOS-'].update(values=resultados)
                    
                elif event == "Afiliação":
                    resultados = []
                    formLayout = [
                        [sg.Text('Afiliação:', size=(15, 1), font=("Cooper Hewitt", 12, "bold"), justification="left", background_color=claro, text_color=escuro),
                        sg.InputText(key='-AFILIAÇÃO-', size=(65, 10))],
                        [sg.Text('Deseja ordenar por data de publicação ou por título?', font=("Cooper Hewitt", 12), background_color=claro, text_color=escuro),
                        sg.Radio("Data de publicação", "OPCAO", default=False, key="-OPC1-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro),
                        sg.Radio("Título", "OPCAO", default=True, key="-OPC2-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro)],
                        [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))],
                        [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                        [sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                    ]

                    wform = sg.Window('Digite a afiliação', formLayout, size=(700, 400), modal=True, resizable=False, background_color=claro)
                    reading_form = True

                    while reading_form:
                        event_form, values_form = wform.read()

                        if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                            reading_form = False  
                            wform.close()
                        elif event_form == 'Consultar':
                            if values_form['-AFILIAÇÃO-']:
                                if values_form['-OPC1-']:
                                    res = fc.filterafiliation_ordenadodate(BD, values_form['-AFILIAÇÃO-'])
                                    if res:
                                        resultados.extend(res)  
                                        window["-DADOS-"].update("Publicação consultada com sucesso!")
                                    else:
                                        resultados.append("A publicação que procurou não existe!")
                                    wform['-RESULTADOS-'].update(values=resultados)

                                else:
                                    res = fc.filterafiliation_ordenadotitle(BD, values_form['-AFILIAÇÃO-'])
                                    if res:
                                        resultados.extend(res)  
                                        window["-DADOS-"].update("Publicação consultada com sucesso!")
                                    else:
                                        resultados.append("A publicação que procurou não existe!")
                                    wform['-RESULTADOS-'].update(values=resultados)
                    
                elif event == 'Data de publicação': 
                    resultados =[]
                    layout_date = [
                        [sg.Text('Data de publicação', size=(25, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro)],
                        [sg.CalendarButton('Escolha a Data', target='-DATA-', font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                        sg.InputText("", key='-DATA-', readonly=True, font=("Cooper Hewitt", 12))],
                        [sg.Text('Deseja ordenar por data de publicação ou por título?', font=("Cooper Hewitt", 12), background_color=claro, text_color=escuro),
                        sg.Radio("Data de publicação", "OPCAO", default=False, key="-OPC1-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro),
                        sg.Radio("Título", "OPCAO", default=True, key="-OPC2-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro)],
                        [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))],
                        [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                        [sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                    ]

                    wform = sg.Window('Digite a data de publicação', layout_date, size=(700, 400), modal=True, background_color=claro)
                    
                    reading_form = True
                    while reading_form:
                        event_form, values_form = wform.read()

                        if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                            reading_form = False  
                            wform.close()
                        elif event_form == 'Consultar':
                            if values_form['-DATA-']:
                                if values_form['-OPC1-']:
                                    res = fc.filterdata_ordenadodate(BD, values_form['-DATA-'])
                                    if res:
                                        resultados.extend(res)  
                                        window["-DADOS-"].update("Publicação consultada com sucesso!")
                                    else:
                                        resultados.append("A publicação que procurou não existe!")
                                    wform['-RESULTADOS-'].update(values=resultados)

                                else:
                                    res = fc.filterdata_ordenadotitle(BD, values_form['-DATA-'])
                                    if res:
                                        resultados.extend(res)  
                                        window["-DADOS-"].update("Publicação consultada com sucesso!")
                                    else:
                                        resultados.append("A publicação que procurou não existe!")
                                    wform['-RESULTADOS-'].update(values=resultados)
                    

                elif event == "Palavras-chave":
                    resultados = []
                    formLayout = [
                        [sg.Text('Palavras-chave:', size=(15, 1), font=("Cooper Hewitt", 12, "bold"), justification="left", background_color=claro, text_color=escuro),
                        sg.InputText(key='-PALAVRAS-', size=(65, 10))],
                        [sg.Text('Deseja ordenar por data de publicação ou por título?', font=("Cooper Hewitt", 12), background_color=claro, text_color=escuro),
                        sg.Radio("Data de publicação", "OPCAO", default=False, key="-OPC1-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro),
                        sg.Radio("Título", "OPCAO", default=True, key="-OPC2-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro)],
                        [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))],
                        [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                        [sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                    ]

                    wform = sg.Window('Digite as palavras-chaves', formLayout, size=(700, 400), modal=True, resizable=False, background_color=claro)
                    reading_form = True

                    while reading_form:
                        event_form, values_form = wform.read()

                        if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                            reading_form = False  
                            wform.close()
                        elif event_form == 'Consultar':
                            if values_form['-PALAVRAS-']:
                                if values_form['-OPC1-']:
                                    res = fc.filterpalavrachave_ordenadodate(BD, values_form['-PALAVRAS-'])
                                    if res:
                                        resultados.extend(res)  
                                        window["-DADOS-"].update("Publicação consultada com sucesso!")
                                    else:
                                        resultados.append("A publicação que procurou não existe!")
                                    wform['-RESULTADOS-'].update(values=resultados)

                                else:
                                    res = fc.filterpalavrachave_ordenadotitle(BD, values_form['-PALAVRAS-'])
                                    if res:
                                        resultados.extend(res)  
                                        window["-DADOS-"].update("Publicação consultada com sucesso!")
                                    else:
                                        resultados.append("A publicação que procurou não existe!")
                                    wform['-RESULTADOS-'].update(values=resultados)
        
        #Analisar Publicações                            
        elif eventos == "-LISTAGEM-":
        
            window["-DADOS-"].update("A listar...")
            
            if BD == None:
                janelaErro ("Introduza primeiro uma base de dados!")
            
            elif Guardada == 0:
                janelaErro ("Guarde primeiro a base de dados!")

            else:

                layout_listagem = [
                    [sg.Text ('Deseja listar publicações por:', size= (45,1), expand_x= True, font=("Cooper Hewitt", 15, "bold"),background_color=claro,text_color=escuro)],
                    [sg.Button ('Autores', size=(15,1),button_color=(claro,escuro),font = ("Cooper Hewitt",12)),sg.Button ('Palavras-chave', size=(15,1),button_color=(claro,escuro),font = ("Cooper Hewitt",12)),sg.Button ('Retornar ao Menu',size=(15,1),font=("Cooper Hewitt", 12), button_color= (claro,tijolo))],     
                ]
            
                window_listagem = sg.Window(title="Listar publicações", resizable=False, background_color=claro, finalize=True, layout=layout_listagem)
                
                stop_listagem = False

                while not stop_listagem:
                    eventos_listagem, valores_listagem = window_listagem.read()    

                    if eventos_listagem in (sg.WINDOW_CLOSED, 'Retornar ao Menu'):
                        stop_listagem = True
                        window_listagem.close()
                    
                    elif eventos_listagem == 'Autores':
                        resultado = [] 
                        window_listagem.close()
                        autores_ordenados = []
                        layout_listagem_autores = [
                            [sg.Text('Escolha como pretende que os autores estejam ordenados:', font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro)],
                            [sg.Radio("Ordem alfabética", "OPCAO", font=("Cooper Hewitt", 12), default=True, enable_events=True, key="-OPC1-",background_color=escuro, text_color=claro),
                            sg.Radio("Frequência", "OPCAO", font=("Cooper Hewitt", 12), default=False, enable_events=True, key="-OPC2-", background_color=escuro, text_color=claro)],
                            [sg.Combo(autores_ordenados, default_value="", size = (80,10), key="-AUT-"),sg.Button("Listar", size=(10,1), font=("Cooper Hewitt", 12), pad=((10,0),(5,10)),button_color=escuro)],
                            [sg.Listbox(values = resultado, size=(80, 10), key="-RESL-")],
                            [sg.Button('Cancelar', font=("Cooper Hewitt", 12), button_color=(claro,tijolo))]
                            ]

            
                        window_listagem_autores = sg.Window("Listar publicações por autor", layout_listagem_autores, background_color=claro)
                        stopform4 = False
                        while stopform4 == False:
                            event, values = window_listagem_autores.read()

                            if event in (sg.WINDOW_CLOSED, 'Cancelar'):
                                stopform4 = True
                                window_listagem_autores.close()

                            if event == "-OPC1-":
                                autores_ordenados = fc.listAuthors(BD)
                                window_listagem_autores["-AUT-"].update(values=autores_ordenados, value=autores_ordenados[0], size=(80, 10))
                            elif event == "-OPC2-":
                                autores_ordenados = fc.distribPub(BD)
                                window_listagem_autores["-AUT-"].update(values=autores_ordenados, value=autores_ordenados[0], size=(80, 10))

                            if event == "Listar":
                                autor_selecionado = values["-AUT-"]
                                publicacoes_do_autor = fc.articleporathor(BD, autor_selecionado)
                                resultado.extend(publicacoes_do_autor)  
                                window_listagem_autores["-RESL-"].update(values=resultado)

                        window_listagem_autores.close()

                    elif eventos_listagem == 'Palavras-chave':
                        resultado = [] 
                        window_listagem.close()
                        palavras_ordenadas = []
                        layout_listagem_palavras = [
                            [sg.Text('Escolha como pretende que as palavras-chave estejam ordenadas:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                            [sg.Radio("Ordem alfabética", "OPCAO", font=("Baskerville", 12), default=True, enable_events=True, key="-OPC1-",background_color=escuro, text_color=claro),
                            sg.Radio("Frequência", "OPCAO", font=("Baskerville", 12), default=False, enable_events=True, key="-OPC2-",background_color=escuro, text_color=claro)],
                            [sg.Combo(palavras_ordenadas, default_value="", size = (80,10), key="-AUT-"),sg.Button("Listar", size=(10,1), font=("Baskerville", 12), pad=((10,0),(5,10)),button_color=escuro)],
                            [sg.Listbox(values = resultado, size=(80, 10), key="-RESL-")],
                            [sg.Button('Cancelar', font=("Cooper Hewitt", 12), button_color=(claro,tijolo))]
                            ]

            
                        window_listagem_palavras = sg.Window("Listar publicações por palavras-chave", layout_listagem_palavras, background_color=claro)
                        stopform4 = False
                        while stopform4 == False:
                            event, values = window_listagem_palavras.read()

                            if event in (sg.WINDOW_CLOSED, 'Cancelar'):
                                stopform4 = True
                                window_listagem_autores.close()

                
                            if event == "-OPC1-":
                                palavras_ordenadas = fc.listKeywords(BD)
                                window_listagem_palavras["-AUT-"].update(values=palavras_ordenadas, value=palavras_ordenadas[0], size=(80, 10))
                            elif event == "-OPC2-":
                                palavras_ordenadas = fc.distribpalavra(BD)
                                window_listagem_palavras["-AUT-"].update(values=palavras_ordenadas, value=palavras_ordenadas[0], size=(80, 10))
                            
                            if event == "Listar":
                                palavra_selecionada = values["-AUT-"]
                                publicacoes_por_palavra = fc.articleporpal(BD, palavra_selecionada)
                                resultado.extend(publicacoes_por_palavra)  
                                window_listagem_palavras["-RESL-"].update(values=resultado)

                        window_listagem_palavras.close() 
        #importar
        elif eventos == "-IMPORTAR-":
            window["-DADOS-"].update('A importar Dataset...')

            if BD == None:
                janelaErro ("Introduza primeiro uma base de dados!")
        
            elif Guardada == 0:
                janelaErro ("Guarde primeiro a base de dados!")

            else:
                formLayout2 = [
                    [
                    sg.Text("Base de dados:", font=("Cooper Hewitt", 12), pad=(0, 30), text_color=claro, background_color=escuro),
                    sg.InputText(key="-FICHEIRO-", readonly=True, enable_events=True, text_color=escuro),
                    sg.FileBrowse(file_types=[("JSON (*.json)", "*.json")], size=(8, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                    sg.Button(key="-CARREGAR-", button_text="Carregar", size=(12, 1), disabled=True, font=("Cooper Hewitt", 12), button_color=(claro, escuro))  
                    ]
                ]

                wform2 = sg.Window('Importar base de dados',formLayout2, size=(650,100), background_color=claro)

                stopform2 = False
                while not stopform2:
                    inputEvent2, inputValues2 = wform2.read()
                    if inputValues2 == sg.WINDOW_CLOSED:
                        window["-DADOS-"].update("")
                        stopform2 = True
                    elif inputEvent2 == '-FICHEIRO-':
                        wform2["-CARREGAR-"].update(disabled=False)
                    elif inputEvent2 == "-CARREGAR-":
                        if inputValues2['Browse']:
                            BD = fc.importar_dados(inputValues2['Browse'],BD)
                            nome = inputValues2['Browse']
                            stopform2 = True
                            window["-DADOS-"].update("Base de dados adicionada com sucesso!")
                            wform2.close()  
        #Exportação Parcial de  Dados
        elif eventos == "-EXPORTAR-":
            window["-DADOS-"].update("A exportar dados...")
            
            layout = [
                [sg.Text("Escolha o critério para consultar as publicações:", font=("Cooper Hewitt", 12),background_color=claro,text_color=escuro)],
                [sg.Button('Título', key='-TITULO-', font=("Cooper Hewitt", 12),button_color=(claro, escuro)),
                 sg.Button('Data de Publicação', key='-DATA-', font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                 sg.Button('Autor', key='-AUTOR-', font=("Cooper Hewitt", 12), button_color=(claro, escuro))],
                [sg.Text("", size=(40, 1), key="-RESULT-", font=("Cooper Hewitt", 12),background_color=claro, text_color=escuro)],
                [sg.Text("Digite o valor de consulta:", font=("Cooper Hewitt", 12),background_color=claro,text_color=escuro)],
                [sg.InputText(key="-INPUT-", size=(30, 1), font=("Cooper Hewitt", 12))],
                [sg.Button("Procurar", font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                 sg.Button("Cancelar", font=("Cooper Hewitt", 12), button_color=(claro, tijolo))],
                [sg.Button("Exportar", font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
            ]
    
            window_exportar = sg.Window("Consultar e Exportar Publicações", layout, resizable=False, background_color=claro)

            filtro_selecionado = None
            dados_filtrados = []
            stop_exportar = False
            while stop_exportar == False:
                evento, valores = window_exportar.read()

                if evento in [sg.WIN_CLOSED, "Cancelar"]:
                    stop_exportar = True
                    window_exportar.close()
                    

                if evento == '-TITULO-':
                    filtro_selecionado = 'title'
                    window_exportar["-RESULT-"].update("Filtro aplicado: Título.")
        
                elif evento == '-DATA-':
                    filtro_selecionado = 'publish_date'
                    window_exportar["-RESULT-"].update("Filtro aplicado: Data de Publicação.")
        
                elif evento == '-AUTOR-':
                    filtro_selecionado = 'authors'
                    window_exportar["-RESULT-"].update("Filtro aplicado: Autor.")
        
                elif evento == "Procurar":
                    valor_consulta = valores["-INPUT-"]
                    if filtro_selecionado and valor_consulta.strip():
                        dados_filtrados = fc.filtrar_publicacoes(filtro_selecionado, valor_consulta, BD)
                        if dados_filtrados:
                            window_exportar["-RESULT-"].update(f"Encontradas {len(dados_filtrados)} publicações.", text_color=tijolo)
                        else:
                            window_exportar["-RESULT-"].update("Nenhuma publicação encontrada.", text_color=escuro)
                    else:
                        window_exportar["-RESULT-"].update("Por favor, insira um valor de consulta válido.", text_color=escuro)
        
                elif evento == "Exportar":
                    if dados_filtrados:
                        nome_arquivo = sg.popup_get_file("Escolha onde salvar o arquivo", save_as=True, file_types=(("JSON", "*.json"),),background_color=claro,text_color=escuro)
                        if nome_arquivo:
                            resultado = fc.exportar_dados(nome_arquivo, dados_filtrados)
                            sg.popup(resultado,background_color=claro,text_color=escuro)
                        else:
                            sg.popup("Nome de arquivo inválido.",background_color=claro,text_color=escuro)
                    else:
                        sg.popup("Nenhuma publicação para exportar.",background_color=claro,text_color=escuro)

                    window.close()
            #Atualizar Publicação
            #Criar Publicação
        elif eventos == "-CRIAR-":
            window["-DADOS-"].update('A inserir nova publicação...')

            if BD == None:
                janelaErro ("Introduza primeiro uma base de dados!")
        
            elif Guardada == 0:
                janelaErro ("Guarde primeiro a base de dados!")
            
            else:
                autores = []

                formLayout3 = [
                    [sg.Column([
                    [sg.Text('*Título:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-title-')],
                    [sg.Text('*Resumo:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-abstract-')],
                    [sg.Text('*Palavras-chave:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-keywords-')],
                    [sg.Text('*Autores:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro)],
                    [sg.Text('*Nome:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-name-')],
                    [sg.Text('*Afiliação:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-affiliation-')],
                    [sg.Listbox(values=autores, size=(70, 10), key='-AUTORES-', pad=((0, 0), (15, 10)), enable_events=True),sg.Button('Adicionar Autor', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-ADICIONAR-',size=(20,1))],
                    [sg.Text('*Data de publicação:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.CalendarButton('Escolha a data', target='-data_publicação-', key='calendario',font=("Cooper Hewitt", 12), format='%Y-%m-%d', button_color=(claro, escuro), size=(20,1))],
                    [sg.InputText('', key='-data_publicação-', pad=((480, 0), (0, 0)))],
                    [sg.Text('*doi:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-doi-')],
                    [sg.Text('*pdf:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-pdf-')],
                    [sg.Text('*url:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-url-')],
                    [sg.Text('* Indica um campo obrigatório', font=("Bid Shoulders Display", 12), background_color=claro, text_color=escuro, expand_x=True, enable_events=True)],
                    [sg.Button('Salvar', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-SALVAR-',size=(10,1)),sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12), key='-CANCELAR-', size=(10,1))]
                    ], size=(800, 1000), background_color=claro)]
                    ]
                wform3 = sg.Window('Criar uma nova publicação', formLayout3, background_color=claro, resizable=False)
        
                stopform3 = False
                            
                while stopform3 == False:
                    inputEvent3, inputValues3 = wform3.read()

                                
                    if inputEvent3 in [sg.WIN_CLOSED, 'Exit', '-CANCELAR-']:
                        stopform3 = True
                        wform3.close()
                                
                    elif inputEvent3 == '-ADICIONAR-':
                        nome = inputValues3['-name-']
                        afiliacao = inputValues3['-affiliation-']

                        if nome and afiliacao:
                            autores.append(f"{nome} : {afiliacao}")
                            wform3["-AUTORES-"].update(autores)
                            wform3["-name-"].update("")
                            wform3["-affiliation-"].update("")
                        else:
                            janelaErro("Preencha o nome e a afiliação do autor!")

                    elif (inputValues3['-title-'] == '') or (inputValues3['-abstract-'] == '') or (inputValues3['-keywords-'] == '') or (inputValues3['-data_publicação-'] == '') or (inputValues3['-doi-'] == '') or (inputValues3['-pdf-'] == '') or (inputValues3['-url-'] == '') or not autores:
                            janelaErro('Preencha todos os campos obrigatorios (*)!')

                            
                    else:
                        
                        novatarefa = { 
                                    'abstract': inputValues3['-abstract-'],
                                    'keywords': inputValues3['-keywords-'],
                                    'authors': autores,
                                    'doi': inputValues3['-doi-'], 
                                    'pdf': inputValues3['-pdf-'], 
                                    'publish_date': inputValues3['-data_publicação-'], 
                                    'title': inputValues3['-title-'], 
                                    'url': inputValues3['-url-'],
                                        }
                            
                            
                        BD = fc.criarpublicacao(BD, novatarefa)
                        window["-DADOS-"].update('Tarefa adicionada com sucesso!')
                        wform3.close()
        #Estatísticas
        elif eventos == "-ESTATISTICAS-":  
            if BD== None:
                window["-DADOS-"].update("Primeiro carregue a base de dados!")
            else:
                window["-DADOS-"].update("A produzir dados estatísticos...")
                formLayout = [ 
                    [sg.Text('Gráfico que apresenta distribuição por:', font=("Cambria", 12), background_color=claro, text_color=escuro, pad=(0, 10))],
                    [sg.Column([
                        [sg.Button("ano", font=("Cooper Hewitt", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("mês de um determinado ano", font=("Cooper Hewitt", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("número de publicações por autor(top20)", font=("Cooper Hewitt", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("publicações de um autor por ano", font=("Cooper Hewitt", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("palavras-chave pela frequência(top20)", font=("Cooper Hewitt", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("palavras-chave mais frequentes por ano", font=("Cooper Hewitt", 12), pad=(0, 5), button_color=(claro, escuro))]
                    ], background_color=claro, element_justification="left", pad=(0, 10))]
                ]

                janelanov = sg.Window('Dados estatísticos', formLayout, background_color=claro, element_justification="left")

                stopForm = False
                while not stopForm:
                    inputEvent, inputValues = janelanov.read()
                    if inputEvent == sg.WIN_CLOSED:
                        stopForm=True
                        window["-DADOS-"].update("")
                    else:
                        if inputEvent== "ano":
                            mp.pubano(BD)
                        elif inputEvent == "mês de um determinado ano":
                            window["-DADOS-"].update("A produzir dados estatísticos...")
                            layout_por_ano = [
                                [sg.Text('Escolha o ano para exibir:', size=(45, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                [sg.Combo(values=fc.listanos(BD), key='-ANO-', font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro, size=(20, 1))],
                                [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                            ]
                            window_por_ano = sg.Window(title="Selecione o ano", layout=layout_por_ano, resizable=True, background_color=claro)

                            continuar = True  # Variável de controlo
                            while continuar:
                                event, values = window_por_ano.read()
                                if event in (sg.WINDOW_CLOSED, 'Cancelar'):
                                    continuar = False
                                elif event == 'Consultar':
                                    ano = values['-ANO-']
                                    if ano:
                                        mp.fc.mesano(BD,ano)  # Certifique-se de que a função mesano está corretamente definida
                                        continuar = False  # Sai do ciclo após o processamento
                                    else:
                                        sg.popup("Por favor, selecione um ano.", title="Erro", background_color=claro, text_color=escuro)
                            window_por_ano.close()
                        elif inputEvent== "número de publicações por autor(top20)":
                           npubautor(BD) 
                        elif inputEvent == "publicações de um autor por ano":
                            window["-DADOS-"].update("A produzir dados estatísticos...")
                            formLayout = [
                                [sg.Text('Nome do autor:', size=(15, 1), font=("Baskerville", 12), justification="left", background_color=claro, text_color=escuro),
                                sg.InputText(key='-AUTOR-', size=(45, 1))],
                                [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                            ]

                            wform = sg.Window('Digite o autor', formLayout, size=(600, 150), modal=True, background_color=claro)
                            continue_reading = True
                            while continue_reading:
                                event, values = wform.read()

                                if event in (sg.WINDOW_CLOSED, 'Cancelar'):  # Fechar janela ou cancelar
                                    continue_reading = False

                                elif event == 'Consultar':
                                    autor = values.get('-AUTOR-')  # Obtém o nome do autor
                                    if autor:
                                        pubautorano(BD, autor)  # Chamada à função (certifique-se de que está definida corretamente)
                                    else:
                                        sg.popup("Por favor, insira o nome do autor.", title="Erro", background_color=claro, text_color=escuro)

                            wform.close()
                        elif inputEvent== "palavras-chave pela frequência(top20)":
                            palavrafreq(BD)
                        else:
                            window["-DADOS-"].update("A produzir dados estatísticos...")
                            layout_por_ano = [
                                [sg.Text('Escolha o ano para exibir:', size=(45, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                [sg.Combo(values=listanos(BD), key='-ANO-', font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro, size=(20, 1))],
                                [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                            ]
                            window_por_ano = sg.Window(title="Selecione o ano", layout=layout_por_ano, resizable=True, background_color=claro)

                            continuar = True  # Variável de controlo
                            while continuar:
                                event, values = window_por_ano.read()
                                if event in (sg.WINDOW_CLOSED, 'Cancelar'):
                                    continuar = False
                                elif event == 'Consultar':
                                    ano = values['-ANO-']
                                    if ano:
                                        fc.palavrafreqano(BD,ano)   # Certifique-se de que a função mesano está corretamente definida
                                        continuar = False  # Sai do ciclo após o processamento
                                    else:
                                        sg.popup("Por favor, selecione um ano.", title="Erro", background_color=claro, text_color=escuro)
                            window_por_ano.close()  
                        window["-DADOS-"].update("Dados estatísticos calculados com sucesso!")            
        #Eliminar
        elif eventos == "-ELIMINAR-":
            window["-DADOS-"].update("Preparar para eliminar...")
            if BD is None:
                janelaErro("Introduza primeiro uma base de dados!")
                return
            elif Guardada == 0:
                janelaErro("Guarde primeiro a base de dados!")
                return

            layout8 = [
                [sg.Text('Deseja consultar a publicação por:', size=(45, 1), expand_x=True, font=("Cambria", 15, "bold"), 
                        background_color=claro, text_color=escuro)],
                [sg.Button('Título', size=(17, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                sg.Button('Autor', size=(17, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                sg.Button('Afiliação', size=(17, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                sg.Button('Data de publicação', size=(17, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                sg.Button('Palavras-chave', size=(17, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                sg.Button('Retornar ao Menu', font=("Cooper Hewitt", 12), size=(17, 1), button_color=(claro, tijolo))]
            ]

            window8 = sg.Window(title="Eliminar Publicação", resizable=True, background_color=claro).Layout(layout8)

            continue_reading = True
            while continue_reading:
                event, values = window8.read()
                if event in (sg.WINDOW_CLOSED, 'Retornar ao Menu'):
                    continue_reading = False  

                elif event == "Título":
                    formLayout = [
                        [sg.Text('Título:', size=(15, 1), font=("Baskerville", 12), justification="left", background_color=claro, text_color=escuro),
                        sg.InputText(key='-TITULO-', size=(45, 1))],
                        [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                        sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                    ]

                    wform = sg.Window('Digite o título', formLayout, size=(600, 150), modal=True, background_color=claro)
                    reading_form = True

                    while reading_form:
                        event_form, values_form = wform.read()

                        if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                            reading_form = False  # Sai do loop do formulário
                        elif event_form == 'Consultar':
                            titulo = values_form.get('-TITULO-')
                            print(f"Título inserido: {titulo}")  # Verificar o valor do título inserido
                            if titulo != '':
                                # Filtra os dados pelo título
                                resultados = fc.filtertitle(BD, titulo)  # Função externa para filtrar os dados
                                print(f"Resultados encontrados: {resultados}")  # Verificar os resultados encontrados
                                if resultados:
                                    # Layout da janela de resultados
                                    layout_resultados = [
                                        [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                        [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),
                                        sg.Button('Eliminar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                    ]

                                    # Janela para exibir resultados
                                    janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                    janela_aberta = True

                                    while janela_aberta:
                                        evento_resultados, valores_resultados = janela_resultados.read()
                                        if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                            janela_aberta = False  # Sai do loop de resultados
                                            janela_resultados.close()
                                        elif evento_resultados == 'Eliminar':
                                            # Obtém o valor selecionado na Listbox
                                            publicacao_selecionada = valores_resultados.get('-RESULTADOS-')
                                            if publicacao_selecionada:
                                                publicacao_selecionada = publicacao_selecionada[0]  # Obtém o item selecionado
                                                confirmacao = sg.popup_yes_no(
                                                    f"Tem certeza de que deseja apagar esta publicação?",
                                                    title="Confirmação",
                                                    background_color=claro,
                                                    text_color=escuro
                                                )
                                                if confirmacao == 'Yes':
                                                    # Remove a publicação diretamente da fonte de dados (BD)
                                                    BD.remove(publicacao_selecionada)  # Supondo que BD é a fonte de dados original
                                                    sg.popup("Publicação removida com sucesso!", title="Sucesso", background_color=claro, text_color=escuro)
                                                    resultados.remove(publicacao_selecionada)  # Remove também dos resultados exibidos
                                                    janela_resultados['-RESULTADOS-'].update(values=resultados)  # Atualiza a lista
                                                else:
                                                    sg.popup("Operação cancelada.", title="Cancelado", background_color=claro, text_color=escuro)
                                            else:
                                                sg.popup("Por favor, selecione uma publicação para eliminar.", title="Erro", background_color=claro, text_color=escuro)
                                else:
                                    sg.popup("Nenhum resultado encontrado.", title="Informação", background_color=claro, text_color=escuro)
                            else:
                                sg.popup("Por favor, insira o título.", title="Erro", background_color=claro, text_color=escuro)


                        wform.close()
                elif event == "Autor":
                            formLayout = [
                                [sg.Text('Autor:', size=(15, 1), font=("Baskerville", 12), justification="left", background_color=claro, text_color=escuro),
                                sg.InputText(key='-AUTOR-', size=(45, 1))],
                                [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                            ]

                            wform = sg.Window('Digite o autor', formLayout, size=(600, 150), modal=True, background_color=claro)
                            reading_form = True

                            while reading_form:
                                event_form, values_form = wform.read()

                                if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                                    reading_form = False  # Sai do loop do formulário

                                elif event_form == 'Consultar':
                                    autor = values_form.get('-AUTOR-')
                                    print(f"autor inserido: {autor}")  # Adicione esta linha para verificar o valor de titulos
                                    if autor != '':
                                        # Filtra os dados pelo título
                                        resultados = fc.filterauthor(BD, autor)  # Função externa para filtrar os dados
                                        print(f"Resultados encontrados: {resultados}")  # Adicione esta linha para verificar os resultados
                                        if resultados:
                                            # Layout da janela de resultados
                                            layout_resultados = [
                                                [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                                [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                                [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),sg.Button('Eliminar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                            ]

                                            # Janela para exibir resultados
                                            janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                            janela_aberta = True

                                            while janela_aberta:
                                                evento_resultados, valores_resultados = janela_resultados.read()
                                                if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                                    janela_aberta = False  # Sai do loop de resultados
                                                    janela_resultados.close()
                                                elif evento_resultados == 'Eliminar':
                                                    # Obtém o valor selecionado na Listbox
                                                    publicacao_selecionada = valores_resultados.get('-RESULTADOS-')
                                                    if publicacao_selecionada:
                                                        publicacao_selecionada = publicacao_selecionada[0]  # Obtém o item selecionado
                                                        confirmacao = sg.popup_yes_no(
                                                            f"Tem certeza de que deseja apagar esta publicação?",
                                                            title="Confirmação",
                                                            background_color=claro,
                                                            text_color=escuro
                                                        )
                                                        if confirmacao == 'Yes':
                                                            # Remove a publicação diretamente da fonte de dados (BD)
                                                            BD.remove(publicacao_selecionada)  # Supondo que BD é a fonte de dados original
                                                            sg.popup("Publicação removida com sucesso!", title="Sucesso", background_color=claro, text_color=escuro)
                                                            resultados.remove(publicacao_selecionada)  # Remove também dos resultados exibidos
                                                            janela_resultados['-RESULTADOS-'].update(values=resultados)  # Atualiza a lista
                                                        else:
                                                            sg.popup("Operação cancelada.", title="Cancelado", background_color=claro, text_color=escuro)
                                            else:
                                                sg.popup("Por favor, selecione uma publicação para eliminar.", title="Erro", background_color=claro, text_color=escuro)
                                        else:
                                            sg.popup("Nenhum resultado encontrado.", title="Informação", background_color=claro, text_color=escuro)
                                    else:
                                        sg.popup("Por favor, insira o título.", title="Erro", background_color=claro, text_color=escuro)
                elif event == "Afiliação":
                            formLayout = [
                                [sg.Text('Afiliação:', size=(15, 1), font=("Baskerville", 12), justification="left", background_color=claro, text_color=escuro),
                                sg.InputText(key='-AFILIACAO-', size=(45, 1))],
                                [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                            ]

                            wform = sg.Window('Digite a afiliação', formLayout, size=(600, 150), modal=True, background_color=claro)
                            reading_form = True

                            while reading_form:
                                event_form, values_form = wform.read()

                                if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                                    reading_form = False  # Sai do loop do formulário

                                elif event_form == 'Consultar':
                                    afiliacao = values_form.get('-AFILIACAO-')
                                    print(f"afiliação inserido: {afiliacao}")  # Adicione esta linha para verificar o valor de titulos
                                    if afiliacao!= '':
                                        # Filtra os dados pelo título
                                        resultados = fc.filterafiliation(BD, afiliacao)  # Função externa para filtrar os dados
                                        print(f"Resultados encontrados: {resultados}")  # Adicione esta linha para verificar os resultados
                                        if resultados:
                                            # Layout da janela de resultados
                                            layout_resultados = [
                                                [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                                [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                                [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),sg.Button('Eliminar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                            ]

                                            # Janela para exibir resultados
                                            janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                            janela_aberta = True

                                            while janela_aberta:
                                                evento_resultados, valores_resultados = janela_resultados.read()
                                                if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                                    janela_aberta = False  # Sai do loop de resultados
                                                    janela_resultados.close()
                                                elif evento_resultados == 'Eliminar':
                                                    # Obtém o valor selecionado na Listbox
                                                    publicacao_selecionada = valores_resultados.get('-RESULTADOS-')
                                                    if publicacao_selecionada:
                                                        publicacao_selecionada = publicacao_selecionada[0]  # Obtém o item selecionado
                                                        confirmacao = sg.popup_yes_no(
                                                            f"Tem certeza de que deseja apagar esta publicação?",
                                                            title="Confirmação",
                                                            background_color=claro,
                                                            text_color=escuro
                                                        )
                                                        if confirmacao == 'Yes':
                                                            # Remove a publicação diretamente da fonte de dados (BD)
                                                            BD.remove(publicacao_selecionada)  # Supondo que BD é a fonte de dados original
                                                            sg.popup("Publicação removida com sucesso!", title="Sucesso", background_color=claro, text_color=escuro)
                                                            resultados.remove(publicacao_selecionada)  # Remove também dos resultados exibidos
                                                            janela_resultados['-RESULTADOS-'].update(values=resultados)  # Atualiza a lista
                                                        else:
                                                            sg.popup("Operação cancelada.", title="Cancelado", background_color=claro, text_color=escuro)
                                            else:
                                                sg.popup("Por favor, selecione uma publicação para eliminar.", title="Erro", background_color=claro, text_color=escuro)
                                        else:
                                            sg.popup("Nenhum resultado encontrado.", title="Informação", background_color=claro, text_color=escuro)
                                    else:
                                        sg.popup("Por favor, insira a afiliação.", title="Erro", background_color=claro, text_color=escuro)
                            wform.close()
                elif event == 'Data de publicação':
                    layout_date = [
                        [sg.Text('Data de publicação', size=(25, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                        [sg.CalendarButton('Escolha a Data', target='-DATA-', font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                        sg.InputText("", key='-DATA-', readonly=True, font=("Cooper Hewitt", 12))],
                        [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                        sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                    ]

                    window10 = sg.Window(title="Consulte pela data de publicação", resizable=True, background_color=claro).Layout(layout_date)
                    reading_date = True

                    while reading_date:
                        eventos10, valores10 = window10.read()
                        if eventos10 in [sg.WIN_CLOSED, 'Sair']:
                            reading_date = False  # Sai do loop da janela de data
                        elif eventos10 == 'Consultar':
                            data = values_form.get('-DATA-')
                            if data:
                                resultados = fc.filterdata(BD, data)  # Função externa para filtrar os dados
                                if resultados:
                                    # Layout da janela de resultados
                                    layout_resultados = [
                                        [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                        [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),sg.Button('Eliminar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                    ]

                                    # Janela para exibir resultados
                                    janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                    janela_aberta = True

                                    while janela_aberta:
                                        evento_resultados, valores_resultados = janela_resultados.read()
                                        if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                            janela_aberta = False  # Sai do loop de resultados
                                            janela_resultados.close()
                                        elif evento_resultados == 'Eliminar':
                                            # Obtém o valor selecionado na Listbox
                                            publicacao_selecionada = valores_resultados.get('-RESULTADOS-')
                                            if publicacao_selecionada:
                                                publicacao_selecionada = publicacao_selecionada[0]  # Obtém o item selecionado
                                                confirmacao = sg.popup_yes_no(
                                                    f"Tem certeza de que deseja apagar esta publicação?",
                                                    title="Confirmação",
                                                    background_color=claro,
                                                    text_color=escuro
                                                )
                                                if confirmacao == 'Yes':
                                                    # Remove a publicação diretamente da fonte de dados (BD)
                                                    BD.remove(publicacao_selecionada)  # Supondo que BD é a fonte de dados original
                                                    sg.popup("Publicação removida com sucesso!", title="Sucesso", background_color=claro, text_color=escuro)
                                                    resultados.remove(publicacao_selecionada)  # Remove também dos resultados exibidos
                                                    janela_resultados['-RESULTADOS-'].update(values=resultados)  # Atualiza a lista
                                                else:
                                                    sg.popup("Operação cancelada.", title="Cancelado", background_color=claro, text_color=escuro)
                                            else:
                                                sg.popup("Por favor, selecione uma publicação para eliminar.", title="Erro", background_color=claro, text_color=escuro)
                                # Filtra os dados pela data de publicação

                                else:
                                    sg.popup("Nenhum resultado encontrado.", title="Informação", background_color=claro, text_color=escuro)
                            else:
                                sg.popup("Por favor, insira a data.", title="Erro", background_color=claro, text_color=escuro)
                    window10.close()
                elif event == "Palavras-chave":
                            formLayout = [
                                [sg.Text('Palavras-chave:', size=(15, 1), font=("Baskerville", 12), justification="left", background_color=claro, text_color=escuro),
                                sg.InputText(key='-PALAVRASCHAVE-', size=(45, 1))],
                                [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                            ]

                            wform = sg.Window('Digite as palavras-chave', formLayout, size=(600, 150), modal=True, background_color=claro)
                            reading_form = True

                            while reading_form:
                                event_form, values_form = wform.read()

                                if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                                    reading_form = False  # Sai do loop do formulário
                                elif event_form == 'Consultar':
                                    palavraschave = values_form.get('-PALAVRASCHAVE-')
                                    if palavraschave != '':
                                        # Filtra os dados pelo título
                                        resultados = fc.filterpalavrachave(BD, palavraschave)  # Função externa para filtrar os dados
                                        if resultados:
                                            # Layout da janela de resultados
                                            layout_resultados = [
                                                [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                                [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                                [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),sg.Button('Eliminar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                            ]

                                            # Janela para exibir resultados
                                            janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                            janela_aberta = True

                                            while janela_aberta:
                                                evento_resultados, valores_resultados = janela_resultados.read()
                                                if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                                    janela_aberta = False  # Sai do loop de resultados
                                                    janela_resultados.close()
                                                elif evento_resultados == 'Eliminar':
                                                    # Obtém o valor selecionado na Listbox
                                                    publicacao_selecionada = valores_resultados.get('-RESULTADOS-')
                                                    if publicacao_selecionada:
                                                        publicacao_selecionada = publicacao_selecionada[0]  # Obtém o item selecionado
                                                        confirmacao = sg.popup_yes_no(
                                                            f"Tem certeza de que deseja apagar esta publicação?",
                                                            title="Confirmação",
                                                            background_color=claro,
                                                            text_color=escuro
                                                        )
                                                        if confirmacao == 'Yes':
                                                            # Remove a publicação diretamente da fonte de dados (BD)
                                                            BD.remove(publicacao_selecionada)  # Supondo que BD é a fonte de dados original
                                                            sg.popup("Publicação removida com sucesso!", title="Sucesso", background_color=claro, text_color=escuro)
                                                            resultados.remove(publicacao_selecionada)  # Remove também dos resultados exibidos
                                                            janela_resultados['-RESULTADOS-'].update(values=resultados)  # Atualiza a lista
                                                        else:
                                                            sg.popup("Operação cancelada.", title="Cancelado", background_color=claro, text_color=escuro)
                                            else:
                                                sg.popup("Por favor, selecione uma publicação para eliminar.", title="Erro", background_color=claro, text_color=escuro)
                                        else:
                                            sg.popup("Nenhum resultado encontrado.", title="Informação", background_color=claro, text_color=escuro)
                                    else:
                                        sg.popup("Por favor, insira o título.", title="Erro", background_color=claro, text_color=escuro)
                            wform.close()
                            window8.close()                               

interface_grafica()