import FreeSimpleGUI as sg
import Funções as fc
import threading 

#----- Definição das cores ----- 
escuro = '#8C6057'
claro = '#FAF3E0'
tijolo = '#DC143C'

#----- Janela Erro -----
def janelaErro(tipoerro):
    layout=[
        [sg.Text(tipoerro,background_color=claro,font = ("Cooper Hewitt",12), text_color=escuro)], 
        [sg.Button("Ok", button_color=(claro,escuro),font = ('Cooper Hewitt',12))]
        ]
    window_janela= sg.Window(title="Janela Erro",background_color=claro, modal=True, finalize = True, default_element_size=(15,1)).Layout(layout)

    stop_janela=False  
    while not stop_janela:
        evento_janela, valor_janela = window_janela.read()
        if evento_janela == "Ok" or evento_janela == sg.WIN_CLOSED:
            stop_janela = True
            window_janela.close()

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
            window.close()

        elif eventos == '-SAIR-':
            stop = True
            window.close()

        elif eventos == '-HELP-':
            
            coluna = [

                [sg.Text("Sistema de Consulta e Análise de Publicações Científicas", font=("Cambria", 24, "bold"), justification="center", background_color=claro, text_color=escuro)],
                [sg.Text("Aqui está o guião para te ajudar na utilização da aplicação! Vamos explicar-te todas as funções que esta aplicação te oferece!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nCarregar BD", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Nesta opção terás de carregar uma base de dados com todas as publicações que tem para depois podermos usá-la no resto das opções!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nGravar BD", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Utiliza esta opção para gravar a base de dados que carregaste. Isso é especialmente útil após efetuares alterações nas publicações.", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nConsultar Publicação", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Poderás pesquisar as publicações conforme alguns critérios sendo estes título, autor, afiliação, data de publicação e palavras-chave!\nAinda conseguirás ordenar as publicações que pesquisaste por data ou pelo seu título!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nAnalisar publicação", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Aqui poderás escolher de que forma queres analasiar a publicação, se por autor, se por palavras-chave.\nCaso escolhas pesquisar pelo autor poderás ainda selecionar se pretendes que estes apareçam ordenados pela frequênca dos seus artigos publicados ou por ordem alfabética.\nPara a opção das palavras-chave poderás ordenar por ocorrência nos artigos ou por ordem alfabética.", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nImportar Dados", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Esta opção permite que a qualquer momento importes novos registos de um outro ficheiro na base de dados.", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nExportação Parcial", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Poderás exportar  os ficheiros da base de dados, selecionados por ti, para um novo ficheiro com o mesmo formato!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nAtualizar Publicações", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Realiza todas as alterações necessárias nas publicações nesta opção!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nCriar Publicação", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Nesta opção poderás criar uma nova publicação inserindo os seus dados!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nEstatísticas", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Explora diferentes gráficos que mostram vários dados sobre as publicações da base de dados.", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nEliminar Publicação", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Poderás selecionar esta opção caso queiras eliminar alguma publicação da base de dados!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nSair", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Fecha a aplicação. Não te esqueças de gravar o dataset após fazer alterações!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nObrigada por utilizares este sistema!", font=("Cambria", 16), background_color=claro, text_color=escuro)],
                [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
            ]

            layout_help = [[sg.Column(coluna, scrollable=True, vertical_scroll_only=True, size=(1300, 600), background_color=claro)]]


            window_help = sg.Window("Help", layout_help, resizable=False, background_color=claro, location =(0,0))  
            
            janela_aberta = True
            while janela_aberta == True:
                eventos_help, valores_help = window_help.read()
                if eventos_help in [sg.WINDOW_CLOSED, 'Fechar']:
                    janela_aberta = False
                    window_help.close()

    
        #----- Carregar Dataset -----
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
        
        #----- Guardar Dataset -----
        elif eventos == "-GRAVAR-":
            window["-DADOS-"].update("A gravar base de dados...")
            
            if BD == None:
                janelaErro("Introduza primeiro uma base de dados!")
            
            else:
                Guardada = 1
                fc.guardar_dataset(nome, BD)
                window["-DADOS-"].update("Base de dados gravada!")
        
        #----- Consultar publicações -----
        elif eventos == "-CONSULTAR-":
            window["-DADOS-"].update("Preparar para consultar...")
            if BD is None:
                janelaErro("Introduza primeiro uma base de dados!")
                
            elif Guardada == 0:
                janelaErro("Guarde primeiro a base de dados!")
                
            else:
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
                            [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True, enable_events=True)],
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

                                    elif values_form['-OPC2-']:
                                        res = fc.filtertitle_ordenadotitle(BD, values_form['-TITULO-'])
                                        if res:
                                            resultados.extend(res)  
                                            window["-DADOS-"].update("Publicação consultada com sucesso!")
                                        else:
                                            resultados.append("A publicação que procurou não existe!")
                                        wform['-RESULTADOS-'].update(values=resultados)

                            if event_form == '-RESULTADOS-':
                                if values_form['-RESULTADOS-']:
                                    wform.close()
                                    publicação_selecionada = values_form['-RESULTADOS-'][0]

                                    detalhes_publicação_layout = [
                                        [sg.Text("Detalhes da Publicação Selecionada:", font=("Cooper Hewitt", 14, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Título: {publicação_selecionada.get('title')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Resumo: {publicação_selecionada.get('abstract')}", size=(80, 5),font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Palavras-chave: {publicação_selecionada.get('keywords')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text("Autores:", font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Multiline("\n".join([
                                            f"{autor['name']} - {autor.get('affiliation')}" 
                                            for autor in publicação_selecionada.get('authors', [])
                                        ]), size=(80, 5), background_color=claro, text_color=escuro, disabled=True)],
                                        [sg.Text(f"Data de Publicação: {publicação_selecionada.get('publish_date')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"DOI: {publicação_selecionada.get('doi')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"PDF: {publicação_selecionada.get('pdf')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"URL: {publicação_selecionada.get('url')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Button('Fechar', size=(10, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
                                    ]

                                    window_detalhes_pub = sg.Window('Detalhes da Publicação Selecionada', detalhes_publicação_layout, grab_anywhere=False,
                                            finalize=True, background_color=claro)

                                    stop_detalhes_pub = False

                                    while stop_detalhes_pub == False:
                                        event_detalhes_pub, values_detalhes_pub = window_detalhes_pub.read()

                                        if event_detalhes_pub in (sg.WIN_CLOSED, 'Fechar'):
                                            stop_detalhes_pub = True
                                            window_detalhes_pub.close()



                            
                    elif event == "Autor":
                        resultados = []
                        formLayout = [
                            [sg.Text('Autor:', size=(15, 1), font=("Cooper Hewitt", 12, "bold"), justification="left", background_color=claro, text_color=escuro),
                            sg.InputText(key='-AUTOR-', size=(65, 10))],
                            [sg.Text('Deseja ordenar por data de publicação ou por título?', font=("Cooper Hewitt", 12), background_color=claro, text_color=escuro),
                            sg.Radio("Data de publicação", "OPCAO", default=False, key="-OPC1-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro),
                            sg.Radio("Título", "OPCAO", default=True, key="-OPC2-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro)],
                            [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))],
                            [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True, enable_events=True)],
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

                                    elif values_form['-OPC2-']:
                                        res = fc.filterauthor_ordenadotitle(BD, values_form['-AUTOR-'])
                                        if res:
                                            resultados.extend(res)  
                                            window["-DADOS-"].update("Publicação consultada com sucesso!")
                                        else:
                                            resultados.append("A publicação que procurou não existe!")
                                        wform['-RESULTADOS-'].update(values=resultados)
                            if event_form == '-RESULTADOS-':
                                if values_form['-RESULTADOS-']:
                                    wform.close()
                                    publicação_selecionada = values_form['-RESULTADOS-'][0]

                                    detalhes_publicação_layout = [
                                        [sg.Text("Detalhes da Publicação Selecionada:", font=("Cooper Hewitt", 14, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Título: {publicação_selecionada.get('title')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Resumo: {publicação_selecionada.get('abstract')}", size=(80, 5),font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Palavras-chave: {publicação_selecionada.get('keywords')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text("Autores:", font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Multiline("\n".join([
                                            f"{autor['name']} - {autor.get('affiliation')}" 
                                            for autor in publicação_selecionada.get('authors', [])
                                        ]), size=(80, 5), background_color=claro, text_color=escuro, disabled=True)],
                                        [sg.Text(f"Data de Publicação: {publicação_selecionada.get('publish_date')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"DOI: {publicação_selecionada.get('doi')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"PDF: {publicação_selecionada.get('pdf')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"URL: {publicação_selecionada.get('url')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Button('Fechar', size=(10, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
                                    ]

                                    window_detalhes_pub = sg.Window('Detalhes da Publicação Selecionada', detalhes_publicação_layout, grab_anywhere=False,
                                            finalize=True, background_color=claro)

                                    stop_detalhes_pub = False

                                    while stop_detalhes_pub == False:
                                        event_detalhes_pub, values_detalhes_pub = window_detalhes_pub.read()

                                        if event_detalhes_pub in (sg.WIN_CLOSED, 'Fechar'):
                                            stop_detalhes_pub = True
                                            window_detalhes_pub.close()

                        
                    elif event == "Afiliação":
                        resultados = []
                        formLayout = [
                            [sg.Text('Afiliação:', size=(15, 1), font=("Cooper Hewitt", 12, "bold"), justification="left", background_color=claro, text_color=escuro),
                            sg.InputText(key='-AFILIAÇÃO-', size=(65, 10))],
                            [sg.Text('Deseja ordenar por data de publicação ou por título?', font=("Cooper Hewitt", 12), background_color=claro, text_color=escuro),
                            sg.Radio("Data de publicação", "OPCAO", default=False, key="-OPC1-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro),
                            sg.Radio("Título", "OPCAO", default=True, key="-OPC2-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro)],
                            [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))],
                            [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True, enable_events=True)],
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

                                    elif values_form['-OPC2-']:
                                        res = fc.filterafiliation_ordenadotitle(BD, values_form['-AFILIAÇÃO-'])
                                        if res:
                                            resultados.extend(res)  
                                            window["-DADOS-"].update("Publicação consultada com sucesso!")
                                        else:
                                            resultados.append("A publicação que procurou não existe!")
                                        wform['-RESULTADOS-'].update(values=resultados)
                            if event_form == '-RESULTADOS-':
                                if values_form['-RESULTADOS-']:
                                    wform.close()
                                    publicação_selecionada = values_form['-RESULTADOS-'][0]

                                    detalhes_publicação_layout = [
                                        [sg.Text("Detalhes da Publicação Selecionada:", font=("Cooper Hewitt", 14, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Título: {publicação_selecionada.get('title')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Resumo: {publicação_selecionada.get('abstract')}", size=(80, 5),font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Palavras-chave: {publicação_selecionada.get('keywords')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text("Autores:", font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Multiline("\n".join([
                                            f"{autor['name']} - {autor.get('affiliation')}" 
                                            for autor in publicação_selecionada.get('authors', [])
                                        ]), size=(80, 5), background_color=claro, text_color=escuro, disabled=True)],
                                        [sg.Text(f"Data de Publicação: {publicação_selecionada.get('publish_date')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"DOI: {publicação_selecionada.get('doi')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"PDF: {publicação_selecionada.get('pdf')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"URL: {publicação_selecionada.get('url')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Button('Fechar', size=(10, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
                                    ]

                                    window_detalhes_pub = sg.Window('Detalhes da Publicação Selecionada', detalhes_publicação_layout, grab_anywhere=False,
                                            finalize=True, background_color=claro)

                                    stop_detalhes_pub = False

                                    while stop_detalhes_pub == False:
                                        event_detalhes_pub, values_detalhes_pub = window_detalhes_pub.read()

                                        if event_detalhes_pub in (sg.WIN_CLOSED, 'Fechar'):
                                            stop_detalhes_pub = True
                                            window_detalhes_pub.close()

                        
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
                            [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True, enable_events=True)],
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

                                    elif values_form['-OPC2-']:
                                        res = fc.filterdata_ordenadotitle(BD, values_form['-DATA-'])
                                        if res:
                                            resultados.extend(res)  
                                            window["-DADOS-"].update("Publicação consultada com sucesso!")
                                        else:
                                            resultados.append("A publicação que procurou não existe!")
                                        wform['-RESULTADOS-'].update(values=resultados)
                            if event_form == '-RESULTADOS-':
                                if values_form['-RESULTADOS-']:
                                    wform.close()
                                    publicação_selecionada = values_form['-RESULTADOS-'][0]

                                    detalhes_publicação_layout = [
                                        [sg.Text("Detalhes da Publicação Selecionada:", font=("Cooper Hewitt", 14, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Título: {publicação_selecionada.get('title')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Resumo: {publicação_selecionada.get('abstract')}", size=(80, 5),font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Palavras-chave: {publicação_selecionada.get('keywords')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text("Autores:", font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Multiline("\n".join([
                                            f"{autor['name']} - {autor.get('affiliation')}" 
                                            for autor in publicação_selecionada.get('authors', [])
                                        ]), size=(80, 5), background_color=claro, text_color=escuro, disabled=True)],
                                        [sg.Text(f"Data de Publicação: {publicação_selecionada.get('publish_date')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"DOI: {publicação_selecionada.get('doi')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"PDF: {publicação_selecionada.get('pdf')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"URL: {publicação_selecionada.get('url')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Button('Fechar', size=(10, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
                                    ]

                                    window_detalhes_pub = sg.Window('Detalhes da Publicação Selecionada', detalhes_publicação_layout, grab_anywhere=False,
                                            finalize=True, background_color=claro)

                                    stop_detalhes_pub = False

                                    while stop_detalhes_pub == False:
                                        event_detalhes_pub, values_detalhes_pub = window_detalhes_pub.read()

                                        if event_detalhes_pub in (sg.WIN_CLOSED, 'Fechar'):
                                            stop_detalhes_pub = True
                                            window_detalhes_pub.close()

                        

                    elif event == "Palavras-chave":
                        resultados = []
                        formLayout = [
                            [sg.Text('Palavras-chave:', size=(15, 1), font=("Cooper Hewitt", 12, "bold"), justification="left", background_color=claro, text_color=escuro),
                            sg.InputText(key='-PALAVRAS-', size=(65, 10))],
                            [sg.Text('Deseja ordenar por data de publicação ou por título?', font=("Cooper Hewitt", 12), background_color=claro, text_color=escuro),
                            sg.Radio("Data de publicação", "OPCAO", default=False, key="-OPC1-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro),
                            sg.Radio("Título", "OPCAO", default=True, key="-OPC2-", font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro)],
                            [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))],
                            [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True, enable_events=True)],
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

                                    elif values_form['-OPC2-']:
                                        res = fc.filterpalavrachave_ordenadotitle(BD, values_form['-PALAVRAS-'])
                                        if res:
                                            resultados.extend(res)  
                                            window["-DADOS-"].update("Publicação consultada com sucesso!")
                                        else:
                                            resultados.append("A publicação que procurou não existe!")
                                        wform['-RESULTADOS-'].update(values=resultados)
                            if event_form == '-RESULTADOS-':
                                if values_form['-RESULTADOS-']:
                                    wform.close()
                                    publicação_selecionada = values_form['-RESULTADOS-'][0]

                                    detalhes_publicação_layout = [
                                        [sg.Text("Detalhes da Publicação Selecionada:", font=("Cooper Hewitt", 14, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Título: {publicação_selecionada.get('title')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Resumo: {publicação_selecionada.get('abstract')}", size=(80, 5),font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Palavras-chave: {publicação_selecionada.get('keywords')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text("Autores:", font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Multiline("\n".join([
                                            f"{autor['name']} - {autor.get('affiliation')}" 
                                            for autor in publicação_selecionada.get('authors', [])
                                        ]), size=(80, 5), background_color=claro, text_color=escuro, disabled=True)],
                                        [sg.Text(f"Data de Publicação: {publicação_selecionada.get('publish_date')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"DOI: {publicação_selecionada.get('doi')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"PDF: {publicação_selecionada.get('pdf')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"URL: {publicação_selecionada.get('url')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Button('Fechar', size=(10, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
                                    ]

                                    window_detalhes_pub = sg.Window('Detalhes da Publicação Selecionada', detalhes_publicação_layout, grab_anywhere=False,
                                            finalize=True, background_color=claro)

                                    stop_detalhes_pub = False

                                    while stop_detalhes_pub == False:
                                        event_detalhes_pub, values_detalhes_pub = window_detalhes_pub.read()

                                        if event_detalhes_pub in (sg.WIN_CLOSED, 'Fechar'):
                                            stop_detalhes_pub = True
                                            window_detalhes_pub.close()

        
        #----- Analisar Publicações -----                            
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
                            [sg.Listbox(values = resultado, size=(80, 10), key="-RESL-", enable_events = True )],
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

                            if event == '-RESL-':
                                if values['-RESL-']:
                                    wform.close()
                                    publicação_selecionada = values['-RESL-'][0]

                                    detalhes_publicação_layout = [
                                        [sg.Text("Detalhes da Publicação Selecionada:", font=("Cooper Hewitt", 14, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Título: {publicação_selecionada.get('title')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Resumo: {publicação_selecionada.get('abstract')}", size=(80, 5),font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Palavras-chave: {publicação_selecionada.get('keywords')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text("Autores:", font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Multiline("\n".join([
                                            f"{autor['name']} - {autor.get('affiliation')}" 
                                            for autor in publicação_selecionada.get('authors', [])
                                        ]), size=(80, 5), background_color=claro, text_color=escuro, disabled=True)],
                                        [sg.Text(f"Data de Publicação: {publicação_selecionada.get('publish_date')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"DOI: {publicação_selecionada.get('doi')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"PDF: {publicação_selecionada.get('pdf')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"URL: {publicação_selecionada.get('url')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Button('Fechar', size=(10, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
                                    ]

                                    window_detalhes_pub = sg.Window('Detalhes da Publicação Selecionada', detalhes_publicação_layout, grab_anywhere=False,
                                            finalize=True, background_color=claro, resizable=False)

                                    stop_detalhes_pub = False

                                    while stop_detalhes_pub == False:
                                        event_detalhes_pub, values_detalhes_pub = window_detalhes_pub.read()

                                        if event_detalhes_pub in (sg.WIN_CLOSED, 'Fechar'):
                                            stop_detalhes_pub = True
                                            window_detalhes_pub.close()

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
                            [sg.Listbox(values = resultado, size=(80, 10), key="-RESL-", enable_events=True)],
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
                                palavras_ordenadas = list(fc.distribpalavra(BD))
                                window_listagem_palavras["-AUT-"].update(values=palavras_ordenadas, value=palavras_ordenadas[0], size=(80, 10))
                            
                            if event == "Listar":
                                palavra_selecionada = values["-AUT-"]
                                publicacoes_por_palavra = fc.articleporpal(BD, palavra_selecionada)
                                resultado.extend(publicacoes_por_palavra)  
                                window_listagem_palavras["-RESL-"].update(values=resultado)
                            
                            if event == '-RESL-':
                                if values['-RESL-']:
                                    wform.close()
                                    publicação_selecionada = values['-RESL-'][0]

                                    detalhes_publicação_layout = [
                                        [sg.Text("Detalhes da Publicação Selecionada:", font=("Cooper Hewitt", 14, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Título: {publicação_selecionada.get('title')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Resumo: {publicação_selecionada.get('abstract')}", size=(80, 5),font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"Palavras-chave: {publicação_selecionada.get('keywords')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text("Autores:", font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Multiline("\n".join([
                                            f"{autor['name']} - {autor.get('affiliation')}" 
                                            for autor in publicação_selecionada.get('authors', [])
                                        ]), size=(80, 5), background_color=claro, text_color=escuro, disabled=True)],
                                        [sg.Text(f"Data de Publicação: {publicação_selecionada.get('publish_date')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"DOI: {publicação_selecionada.get('doi')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"PDF: {publicação_selecionada.get('pdf')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Text(f"URL: {publicação_selecionada.get('url')}",font=("Cooper Hewitt", 10), background_color=claro, text_color=escuro)],
                                        [sg.Button('Fechar', size=(10, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
                                    ]

                                    window_detalhes_pub = sg.Window('Detalhes da Publicação Selecionada', detalhes_publicação_layout, grab_anywhere=False,
                                            finalize=True, background_color=claro, resizable=False)

                                    stop_detalhes_pub = False

                                    while stop_detalhes_pub == False:
                                        event_detalhes_pub, values_detalhes_pub = window_detalhes_pub.read()

                                        if event_detalhes_pub in (sg.WIN_CLOSED, 'Fechar'):
                                            stop_detalhes_pub = True
                                            window_detalhes_pub.close()

                        window_listagem_palavras.close() 
        #----- Importar Ficheiro -----
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
        #----- Exportação Parcial de  Dados-----
        elif eventos == "-EXPORTAR-":
            window["-DADOS-"].update("A exportar dados...")
            
            layout = [
                [sg.Text("Escolha o critério para consultar as publicações:", font=("Cooper Hewitt", 12),background_color=claro,text_color=escuro)],
                [sg.Button('Título', key='-TITULO-', font=("Cooper Hewitt", 12),button_color=(claro, escuro)),
                 sg.Button('Data de Publicação', key='-DATA-', font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                 sg.Button('Autor', key='-AUTOR-', font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                 sg.Button('Afiliação', key='-AFILIAÇÃO-', font=("Cooper Hewitt", 12),button_color=(claro, escuro)),
                 sg.Button('Palavra-chave', key='-PALAVRA-', font=("Cooper Hewitt", 12),button_color=(claro, escuro)),],
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
                    filtro_selecionado = 'name'
                    window_exportar["-RESULT-"].update("Filtro aplicado: Autor.")

                elif evento == '-AFILIAÇÃO-':
                    filtro_selecionado = 'affiliation'
                    window_exportar["-RESULT-"].update("Filtro aplicado: Afiliação.")

                elif evento == '-PALAVRA-':
                    filtro_selecionado = 'keywords'
                    window_exportar["-RESULT-"].update("Filtro aplicado: Palavra-chave.")

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
                        layout_exportar = [
                            [sg.Text("Escolha onde salvar o arquivo:", font=("Cooper Hewitt", 12), background_color=claro, text_color=escuro)],
                            [sg.InputText(key="-FILENAME-", size=(40, 1), font=("Cooper Hewitt", 12)),
                            sg.FileSaveAs("Procurar", file_types=(("JSON", "*.json"),), button_color=(claro, escuro), font=("Cooper Hewitt", 12))],
                            [sg.Button("Salvar", button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                            sg.Button("Cancelar", button_color=(claro,tijolo), font=("Cooper Hewitt", 12))]
                        ]

                        janela_salvar = sg.Window("Salvar Como", layout_exportar, background_color=claro)

                        salvar_como_ativo = True

                        while salvar_como_ativo == True:
                            evento_salvar, valores_salvar = janela_salvar.read()

                            if evento_salvar in (sg.WIN_CLOSED, "Cancelar"):
                                salvar_como_ativo = False
                                janela_salvar.close()

                            elif evento_salvar == "Salvar":
                                nome_arquivo = valores_salvar["-FILENAME-"]
                                if nome_arquivo:
                                    resultado = fc.exportar_dados(nome_arquivo, dados_filtrados)
                                    layout_popup = [
                                        [sg.Text(resultado, font=("Cooper Hewitt", 12), background_color=claro, text_color=escuro)],
                                        [sg.Button("OK", button_color=(claro,escuro), font=("Cooper Hewitt", 12))]
                                    ]
                                
                                    janela_popup = sg.Window("Mensagem", layout_popup, background_color=claro, modal=True, finalize=True)
                                    
                                    
                                    popup_ativo = True

                                    while popup_ativo == True:
                                        evento_popup, _ = janela_popup.read()

                                        if evento_popup in (sg.WIN_CLOSED, "OK"):
                                            popup_ativo = False  
                                            janela_popup.close()

                                    

                                else:
                                    sg.popup(
                                        "Por favor, insira um nome de arquivo válido (com extensão .json).",
                                        background_color=claro,
                                        text_color=escuro,
                                        button_color=(claro, escuro),  
                                        font=("Cooper Hewitt", 12)
                                    )

                    else:  
                        sg.popup("Nenhuma publicação para exportar.",
                                 background_color=claro,
                                 text_color=escuro,
                                 button_color=(claro, escuro),  
                                 font=("Cooper Hewitt", 12)
                        )

                        if evento in (sg.WIN_CLOSED, "Cancelar") and not salvar_como_ativo:
                            stop_exportar = True

                     
        #----- Atualizar Publicação -----
        elif eventos == "-ATUALIZAR-":
            window["-DADOS-"].update("Preparar para atualizar...")
            if BD is None:
                janelaErro("Introduza primeiro uma base de dados!")
                
            elif Guardada == 0:
                janelaErro("Guarde primeiro a base de dados!")
            
            else:
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

                window8 = sg.Window(title="Atualizar Publicação", resizable=True, background_color=claro).Layout(layout8)

                continue_reading = True
                while continue_reading:
                    event, values = window8.read()
                    if event in (sg.WINDOW_CLOSED, 'Retornar ao Menu'):
                        continue_reading = False  
                        window8.close()
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
                                reading_form = False  
                                wform.close()
                            elif event_form == 'Consultar':
                                titulo = values_form.get('-TITULO-')
                                if titulo != '':
                                    resultados = fc.filtertitle(BD, titulo)  
                                    if resultados:

                                        layout_resultados = [
                                            [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                            [sg.Listbox(values=[res for res in resultados], size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                            [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),
                                            sg.Button('Alterar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                        ]

                                        
                                        janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                        janela_aberta = True

                                        while janela_aberta:
                                            evento_resultados, valores_resultados = janela_resultados.read()
                                            if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                                janela_aberta = False
                                                janela_resultados.close()
                                            elif evento_resultados == 'Alterar':
                                                titulo = ""
                                                resumo = ""
                                                palavraschaves = ""
                                                autores = []
                                                data = ""
                                                doi = ""
                                                pdf = ""
                                                url = ""
                                                titulo_selecionado = valores_resultados["-RESULTADOS-"][0]
                                
                                                if isinstance(titulo_selecionado, dict):
                                                        titulo = titulo_selecionado.get('title')
                                                        resumo = titulo_selecionado.get('abstract')
                                                        palavraschaves = titulo_selecionado.get('keywords')
                                                        autores = titulo_selecionado.get('authors')
                                                        data = titulo_selecionado.get('publish_date')
                                                        pdf = titulo_selecionado.get('pdf')
                                                        doi = titulo_selecionado.get('doi')
                                                        url = titulo_selecionado.get('url')
                                                janela_aberta = False
                                                janela_resultados.close()
                                                if titulo_selecionado:
                    
                                                    formLayout3 = [
                                                        [sg.Column([
                                                        [sg.Text('*Título:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=titulo,key='novo_titulo')],
                                                        [sg.Text('*Resumo:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=resumo,key='novo_resumo')],
                                                        [sg.Text('*Palavras-chave:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=palavraschaves,key='novas_palavras')],
                                                        [sg.Text('*Autores:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro)],
                                                        [sg.Text('*Nome:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-name-')],
                                                        [sg.Text('*Afiliação:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-affiliation-')],
                                                        [sg.Listbox(values=autores, size=(70, 10), key='-AUTORES-', pad=((0, 0), (15, 10)), enable_events=True),sg.Button('Adicionar Autor', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-ADICIONAR-',size=(15,1)),sg.Button('Remover Autor', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-REMOVER-',size=(15,1))],
                                                        [sg.Text('*Data de publicação:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.CalendarButton('Escolha a data', target='-data_publicação-', key='calendario',font=("Cooper Hewitt", 12), format='%Y-%m-%d', button_color=(claro, escuro), size=(20,1))],
                                                        [sg.InputText(default_text=data,key='nova_data', pad=((480, 0), (0, 0)))],
                                                        [sg.Text('*doi:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=doi,key='novo_doi')],
                                                        [sg.Text('*pdf:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=pdf,key='novo_pdf')],
                                                        [sg.Text('*url:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=url,key='novo_url')],
                                                        [sg.Text('* Indica um campo obrigatório', font=("Bid Shoulders Display", 12), background_color=claro, text_color=escuro, expand_x=True, enable_events=True)],
                                                        [sg.Button('Salvar', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-SALVAR-',size=(10,1)),sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12), key='-CANCELAR-', size=(10,1))]
                                                        ], size=(800, 1000), background_color=claro)]
                                                        ]

                                                    wform3 = sg.Window('Alterar uma publicação', formLayout3, background_color=claro, resizable=True)
                                                    stopform3 = False

                                                    while not stopform3:
                                                        inputEvent3, inputValues3 = wform3.read()

                                                        if inputEvent3 in [sg.WIN_CLOSED, '-CANCELAR-']:
                                                            stopform3 = True

                                                        elif inputEvent3 == '-ADICIONAR-':
                                                            nome = inputValues3['-name-']
                                                            afiliacao = inputValues3['-affiliation-']

                                                            if nome and afiliacao:  
                                                                autor = {'name': nome, 'affiliation': afiliacao}  
                                                                autores.append(f"{autor}") 
                                                                wform3["-AUTORES-"].update(autores)  
                                                                wform3["-name-"].update("")  
                                                                wform3["-affiliation-"].update("")  
                                                            else:
                                                                janelaErro("Preencha o nome e a afiliação do autor!") 

                                                        elif inputEvent3 == '-REMOVER-':
                                                            if inputValues3['-AUTORES-']:  
                                                                autor_selecionado = inputValues3['-AUTORES-'][0]  
                                                                if autor_selecionado in autores:  
                                                                    autores.remove(autor_selecionado)  
                                                                    wform3["-AUTORES-"].update(autores)  
                                                                else:
                                                                    janelaErro("Autor não encontrado na lista!")  
                                                            else:
                                                                janelaErro("Selecione um autor para remover!") 

                                                        elif any(inputValues3[k] == '' for k in ['novo_titulo', 'novo_resumo', 'novas_palavras', 'nova_data', 'novo_doi', 'novo_pdf', 'novo_url']) or not autores:
                                                            janelaErro('Preencha todos os campos obrigatórios (*)!')
                                                        
                                                        elif inputEvent3 == '-SALVAR-':
                                                        
                                                            novatarefa = { 
                                                                'abstract': inputValues3['novo_resumo'],
                                                                'keywords': inputValues3['novas_palavras'],
                                                                'authors': autores,
                                                                'doi': inputValues3['novo_doi'], 
                                                                'pdf': inputValues3['novo_pdf'], 
                                                                'publish_date': inputValues3['nova_data'],
                                                                'title': inputValues3['novo_titulo'], 
                                                                'url': inputValues3['novo_url'],
                                                            }

                                                            publicacoes = fc.alterarDetalhesPub(inputValues3['novo_titulo'],inputValues3['novo_resumo'],inputValues3['novas_palavras'],autores,inputValues3['nova_data'],inputValues3['novo_doi'],inputValues3['novo_pdf'],inputValues3['novo_url'], BD)
                                                            sg.popup('Publicação alterada com sucesso!',  
                                                                    background_color=claro,
                                                                    text_color=escuro,
                                                                    button_color=(claro, escuro),  
                                                                    font=("Cooper Hewitt", 12)
                                                                    )
                                                            stopform3 = True
                                                    wform3.close()
                                    else:
                                        janelaErro("Nenhum resultado encontrado.")
                                else:
                                    janelaErro("Por favor, insira o título.")

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
                                reading_form = False 
                                wform.close()

                            elif event_form == 'Consultar':
                                autor = values_form.get('-AUTOR-')
        
                                if autor != '':
                                    
                                    resultados = fc.filterauthor(BD, autor)  
                            
                                    if resultados:

                                        layout_resultados = [
                                            [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                            [sg.Listbox(values=[res for res in resultados], size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                            [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),
                                            sg.Button('Alterar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                        ]

                                    
                                        janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                        janela_aberta = True

                                        while janela_aberta:
                                            evento_resultados, valores_resultados = janela_resultados.read()
                                            if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                                janela_aberta = False
                                                janela_resultados.close()
                                            elif evento_resultados == 'Alterar':
        
                                                titulo = ""
                                                resumo = ""
                                                palavraschaves = ""
                                                autores = []
                                                data = ""
                                                doi = ""
                                                pdf = ""
                                                url = ""
                                                
                                                titulo_selecionado = valores_resultados["-RESULTADOS-"][0]
                                                
                                
                                                if isinstance(titulo_selecionado, dict):
                                                
                                                        titulo = titulo_selecionado.get('title')
                                                        resumo = titulo_selecionado.get('abstract')
                                                        palavraschaves = titulo_selecionado.get('keywords')
                                                        autores = titulo_selecionado.get('authors')
                                                        data = titulo_selecionado.get('publish_date')
                                                        pdf = titulo_selecionado.get('pdf')
                                                        doi = titulo_selecionado.get('doi')
                                                        url = titulo_selecionado.get('url')
                                                janela_aberta = False
                                                janela_resultados.close()
                                                if titulo_selecionado:
        
                                                    formLayout3 = [
                                                        [sg.Column([
                                                        [sg.Text('*Título:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=titulo,key='novo_titulo')],
                                                        [sg.Text('*Resumo:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=resumo,key='novo_resumo')],
                                                        [sg.Text('*Palavras-chave:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=palavraschaves,key='novas_palavras')],
                                                        [sg.Text('*Autores:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro)],
                                                        [sg.Text('*Nome:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-name-')],
                                                        [sg.Text('*Afiliação:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-affiliation-')],
                                                        [sg.Listbox(values=autores, size=(70, 10), key='-AUTORES-', pad=((0, 0), (15, 10)), enable_events=True),sg.Button('Adicionar Autor', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-ADICIONAR-',size=(15,1)),sg.Button('Remover Autor', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-REMOVER-',size=(15,1))],
                                                        [sg.Text('*Data de publicação:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.CalendarButton('Escolha a data', target='-data_publicação-', key='calendario',font=("Cooper Hewitt", 12), format='%Y-%m-%d', button_color=(claro, escuro), size=(20,1))],
                                                        [sg.InputText(default_text=data,key='nova_data', pad=((480, 0), (0, 0)))],
                                                        [sg.Text('*doi:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=doi,key='novo_doi')],
                                                        [sg.Text('*pdf:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=pdf,key='novo_pdf')],
                                                        [sg.Text('*url:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=url,key='novo_url')],
                                                        [sg.Text('* Indica um campo obrigatório', font=("Bid Shoulders Display", 12), background_color=claro, text_color=escuro, expand_x=True, enable_events=True)],
                                                        [sg.Button('Salvar', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-SALVAR-',size=(10,1)),sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12), key='-CANCELAR-', size=(10,1))]
                                                        ], size=(800, 1000), background_color=claro)]
                                                        ]

                                                    wform3 = sg.Window('Alterar uma publicação', formLayout3, background_color=claro, resizable=True)
                                                    stopform3 = False

                                                    while not stopform3:
                                                        inputEvent3, inputValues3 = wform3.read()

                                                        if inputEvent3 in [sg.WIN_CLOSED, '-CANCELAR-']:
                                                            stopform3 = True

                                                        elif inputEvent3 == '-ADICIONAR-':
                                                            nome = inputValues3['-name-']
                                                            afiliacao = inputValues3['-affiliation-']

                                                            if nome and afiliacao:  
                                                                autor = {'name': nome, 'affiliation': afiliacao}  
                                                                autores.append(f"{autor}") 
                                                                wform3["-AUTORES-"].update(autores)  
                                                                wform3["-name-"].update("")  
                                                                wform3["-affiliation-"].update("")  
                                                            else:
                                                                janelaErro("Preencha o nome e a afiliação do autor!") 

                                                        elif inputEvent3 == '-REMOVER-':
                                                            if inputValues3['-AUTORES-']:  
                                                                autor_selecionado = inputValues3['-AUTORES-'][0]  
                                                                if autor_selecionado in autores:  
                                                                    autores.remove(autor_selecionado)  
                                                                    wform3["-AUTORES-"].update(autores)  
                                                                else:
                                                                    janelaErro("Autor não encontrado na lista!") 
                                                            else:
                                                                janelaErro("Selecione um autor para remover!") 

                                                        elif any(inputValues3[k] == '' for k in ['novo_titulo', 'novo_resumo', 'novas_palavras', 'nova_data', 'novo_doi', 'novo_pdf', 'novo_url']) or not autores:
                                                            janelaErro('Preencha todos os campos obrigatórios (*)!')
                                                    
                                                        elif inputEvent3 == '-SALVAR-':
                                                            
                                                            novatarefa = { 
                                                                'abstract': inputValues3['novo_resumo'],
                                                                'keywords': inputValues3['novas_palavras'],
                                                                'authors': autores,
                                                                'doi': inputValues3['novo_doi'], 
                                                                'pdf': inputValues3['novo_pdf'], 
                                                                'publish_date': inputValues3['nova_data'],
                                                                'title': inputValues3['novo_titulo'], 
                                                                'url': inputValues3['novo_url'],
                                                            }

                                                            publicacoes = fc.alterarDetalhesPub(inputValues3['novo_titulo'],inputValues3['novo_resumo'],inputValues3['novas_palavras'],autores,inputValues3['nova_data'],inputValues3['novo_doi'],inputValues3['novo_pdf'],inputValues3['novo_url'], BD)
                                                            sg.popup('Publicação alterada com sucesso!',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                            stopform3 = True
                                                    wform3.close()
                                    else:
                                        janelaErro("Nenhum resultado encontrado.")
                                else:
                                    janelaErro("Por favor, insira o autor.")

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
                                reading_form = False  
                                wform.close()

                            elif event_form == 'Consultar':
                                afiliacao = values_form.get('-AFILIACAO-')
                            
                                if afiliacao!= '':
                        
                                    resultados = fc.filterafiliation(BD, afiliacao)  
                            
                                    if resultados:

                                        layout_resultados = [
                                            [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                            [sg.Listbox(values=[res for res in resultados], size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                            [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),
                                            sg.Button('Alterar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                        ]

                                    
                                        janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                        janela_aberta = True

                                        while janela_aberta:
                                            evento_resultados, valores_resultados = janela_resultados.read()
                                            if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                                janela_aberta = False
                                                janela_resultados.close()
                                            elif evento_resultados == 'Alterar':
                                                
                                                titulo = ""
                                                resumo = ""
                                                palavraschaves = ""
                                                autores = []
                                                data = ""
                                                doi = ""
                                                pdf = ""
                                                url = ""
                                                titulo_selecionado = valores_resultados["-RESULTADOS-"][0]
                                
                                                if isinstance(titulo_selecionado, dict):
                                                    
                                                        titulo = titulo_selecionado.get('title')
                                                        resumo = titulo_selecionado.get('abstract')
                                                        palavraschaves = titulo_selecionado.get('keywords')
                                                        autores = titulo_selecionado.get('authors')
                                                        data = titulo_selecionado.get('publish_date')
                                                        pdf = titulo_selecionado.get('pdf')
                                                        doi = titulo_selecionado.get('doi')
                                                        url = titulo_selecionado.get('url')
                                                janela_aberta = False
                                                janela_resultados.close()
                                                if titulo_selecionado:
                                            
                                                    formLayout3 = [
                                                        [sg.Column([
                                                        [sg.Text('*Título:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=titulo,key='novo_titulo')],
                                                        [sg.Text('*Resumo:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=resumo,key='novo_resumo')],
                                                        [sg.Text('*Palavras-chave:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=palavraschaves,key='novas_palavras')],
                                                        [sg.Text('*Autores:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro)],
                                                        [sg.Text('*Nome:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-name-')],
                                                        [sg.Text('*Afiliação:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-affiliation-')],
                                                        [sg.Listbox(values=autores, size=(70, 10), key='-AUTORES-', pad=((0, 0), (15, 10)), enable_events=True),sg.Button('Adicionar Autor', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-ADICIONAR-',size=(15,1)),sg.Button('Remover Autor', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-REMOVER-',size=(15,1))],
                                                        [sg.Text('*Data de publicação:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.CalendarButton('Escolha a data', target='-data_publicação-', key='calendario',font=("Cooper Hewitt", 12), format='%Y-%m-%d', button_color=(claro, escuro), size=(20,1))],
                                                        [sg.InputText(default_text=data,key='nova_data', pad=((480, 0), (0, 0)))],
                                                        [sg.Text('*doi:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=doi,key='novo_doi')],
                                                        [sg.Text('*pdf:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=pdf,key='novo_pdf')],
                                                        [sg.Text('*url:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=url,key='novo_url')],
                                                        [sg.Text('* Indica um campo obrigatório', font=("Bid Shoulders Display", 12), background_color=claro, text_color=escuro, expand_x=True, enable_events=True)],
                                                        [sg.Button('Salvar', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-SALVAR-',size=(10,1)),sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12), key='-CANCELAR-', size=(10,1))]
                                                        ], size=(800, 1000), background_color=claro)]
                                                        ]

                                                    wform3 = sg.Window('Alterar uma publicação', formLayout3, background_color=claro, resizable=True)
                                                    stopform3 = False

                                                    while not stopform3:
                                                        inputEvent3, inputValues3 = wform3.read()

                                                        if inputEvent3 in [sg.WIN_CLOSED, '-CANCELAR-']:
                                                            stopform3 = True

                                                        elif inputEvent3 == '-ADICIONAR-':
                                                            nome = inputValues3['-name-']
                                                            afiliacao = inputValues3['-affiliation-']

                                                            if nome and afiliacao:  
                                                                autor = {'name': nome, 'affiliation': afiliacao}  
                                                                autores.append(f"{autor}") 
                                                                wform3["-AUTORES-"].update(autores)  
                                                                wform3["-name-"].update("")  
                                                                wform3["-affiliation-"].update("")  
                                                            else:
                                                                janelaErro("Preencha o nome e a afiliação do autor!") 

                                                        elif inputEvent3 == '-REMOVER-':
                                                            if inputValues3['-AUTORES-']:  
                                                                autor_selecionado = inputValues3['-AUTORES-'][0]  
                                                                if autor_selecionado in autores:  
                                                                    autores.remove(autor_selecionado)  
                                                                    wform3["-AUTORES-"].update(autores)  
                                                                else:
                                                                    janelaErro("Autor não encontrado na lista!")  
                                                            else:
                                                                janelaErro("Selecione um autor para remover!") 

                                                        elif any(inputValues3[k] == '' for k in ['novo_titulo', 'novo_resumo', 'novas_palavras', 'nova_data', 'novo_doi', 'novo_pdf', 'novo_url']) or not autores:
                                                            janelaErro('Preencha todos os campos obrigatórios (*)!')
                                                    
                                                        elif inputEvent3 == '-SALVAR-':
                                                            
                                                            novatarefa = { 
                                                                'abstract': inputValues3['novo_resumo'],
                                                                'keywords': inputValues3['novas_palavras'],
                                                                'authors': autores,
                                                                'doi': inputValues3['novo_doi'], 
                                                                'pdf': inputValues3['novo_pdf'], 
                                                                'publish_date': inputValues3['nova_data'],
                                                                'title': inputValues3['novo_titulo'], 
                                                                'url': inputValues3['novo_url'],
                                                            }

                                                            publicacoes = fc.alterarDetalhesPub(inputValues3['novo_titulo'],inputValues3['novo_resumo'],inputValues3['novas_palavras'],autores,inputValues3['nova_data'],inputValues3['novo_doi'],inputValues3['novo_pdf'],inputValues3['novo_url'], BD)
                                                            sg.popup('Publicação alterada com sucesso!',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                            stopform3 = True
                                                    wform3.close()
                                    else:
                                        janelaErro("Nenhum resultado encontrado.")
                                else:
                                    janelaErro("Por favor, insira a afiliação.")

                    elif event == 'Data de publicação': 
                        layout_date = [
                            [sg.Text('Data de publicação', size=(25, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                            [sg.CalendarButton('Escolha a Data', target='-DATA-', font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                            sg.InputText("", key='-DATA-', readonly=True, font=("Cooper Hewitt", 12))],
                            [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                            sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                        ]

                        wform = sg.Window('Digite a data de publicação', layout_date, size=(600, 150), modal=True, background_color=claro)
                        reading_form = True

                        while reading_form:
                            event_form, values_form = wform.read()

                            if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                                reading_form = False  
                                wform.close()

                            elif event_form == 'Consultar':
                                data = values_form.get('-DATA-')
                                if data:
                                    resultados = fc.filterdata(BD, data)
                    
                                    if resultados:

                                        layout_resultados = [
                                            [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                            [sg.Listbox(values=[res for res in resultados], size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                            [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),
                                            sg.Button('Alterar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                        ]

                                        
                                        janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                        janela_aberta = True

                                        while janela_aberta:
                                            evento_resultados, valores_resultados = janela_resultados.read()
                                            if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                                janela_aberta = False
                                                janela_resultados.close()
                                            elif evento_resultados == 'Alterar':
                                                
                                                titulo = ""
                                                resumo = ""
                                                palavraschaves = ""
                                                autores = []
                                                data = ""
                                                doi = ""
                                                pdf = ""
                                                url = ""
                                                titulo_selecionado = valores_resultados["-RESULTADOS-"][0]
                                
                                                if isinstance(titulo_selecionado, dict):
                                                    
                                                        titulo = titulo_selecionado.get('title')
                                                        resumo = titulo_selecionado.get('abstract')
                                                        palavraschaves = titulo_selecionado.get('keywords')
                                                        autores = titulo_selecionado.get('authors')
                                                        data = titulo_selecionado.get('publish_date')
                                                        pdf = titulo_selecionado.get('pdf')
                                                        doi = titulo_selecionado.get('doi')
                                                        url = titulo_selecionado.get('url')
                                                janela_aberta = False
                                                janela_resultados.close()
                                                if titulo_selecionado:
                            
                                                    formLayout3 = [
                                                        [sg.Column([
                                                        [sg.Text('*Título:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=titulo,key='novo_titulo')],
                                                        [sg.Text('*Resumo:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=resumo,key='novo_resumo')],
                                                        [sg.Text('*Palavras-chave:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=palavraschaves,key='novas_palavras')],
                                                        [sg.Text('*Autores:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro)],
                                                        [sg.Text('*Nome:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-name-')],
                                                        [sg.Text('*Afiliação:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-affiliation-')],
                                                        [sg.Listbox(values=autores, size=(70, 10), key='-AUTORES-', pad=((0, 0), (15, 10)), enable_events=True),sg.Button('Adicionar Autor', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-ADICIONAR-',size=(15,1)),sg.Button('Remover Autor', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-REMOVER-',size=(15,1))],
                                                        [sg.Text('*Data de publicação:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.CalendarButton('Escolha a data', target='-data_publicação-', key='calendario',font=("Cooper Hewitt", 12), format='%Y-%m-%d', button_color=(claro, escuro), size=(20,1))],
                                                        [sg.InputText(default_text=data,key='nova_data', pad=((480, 0), (0, 0)))],
                                                        [sg.Text('*doi:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=doi,key='novo_doi')],
                                                        [sg.Text('*pdf:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=pdf,key='novo_pdf')],
                                                        [sg.Text('*url:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=url,key='novo_url')],
                                                        [sg.Text('* Indica um campo obrigatório', font=("Bid Shoulders Display", 12), background_color=claro, text_color=escuro, expand_x=True, enable_events=True)],
                                                        [sg.Button('Salvar', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-SALVAR-',size=(10,1)),sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12), key='-CANCELAR-', size=(10,1))]
                                                        ], size=(800, 1000), background_color=claro)]
                                                        ]

                                                    wform3 = sg.Window('Alterar uma publicação', formLayout3, background_color=claro, resizable=True)
                                                    stopform3 = False

                                                    while not stopform3:
                                                        inputEvent3, inputValues3 = wform3.read()

                                                        if inputEvent3 in [sg.WIN_CLOSED, '-CANCELAR-']:
                                                            stopform3 = True

                                                        elif inputEvent3 == '-ADICIONAR-':
                                                            nome = inputValues3['-name-']
                                                            afiliacao = inputValues3['-affiliation-']

                                                            if nome and afiliacao:  
                                                                autor = {'name': nome, 'affiliation': afiliacao}  
                                                                autores.append(f"{autor}") 
                                                                wform3["-AUTORES-"].update(autores)  
                                                                wform3["-name-"].update("")  
                                                                wform3["-affiliation-"].update("")  
                                                            else:
                                                                janelaErro("Preencha o nome e a afiliação do autor!") 

                                                        elif inputEvent3 == '-REMOVER-':
                                                            if inputValues3['-AUTORES-']:  
                                                                autor_selecionado = inputValues3['-AUTORES-'][0]  
                                                                if autor_selecionado in autores:  
                                                                    autores.remove(autor_selecionado)  
                                                                    wform3["-AUTORES-"].update(autores)  
                                                                else:
                                                                    janelaErro("Autor não encontrado na lista!")  
                                                            else:
                                                                janelaErro("Selecione um autor para remover!") 

                                                        elif any(inputValues3[k] == '' for k in ['novo_titulo', 'novo_resumo', 'novas_palavras', 'nova_data', 'novo_doi', 'novo_pdf', 'novo_url']) or not autores:
                                                            janelaErro('Preencha todos os campos obrigatórios (*)!')
                                                    
                                                        elif inputEvent3 == '-SALVAR-':
                                                            
                                                            novatarefa = { 
                                                                'abstract': inputValues3['novo_resumo'],
                                                                'keywords': inputValues3['novas_palavras'],
                                                                'authors': autores,
                                                                'doi': inputValues3['novo_doi'], 
                                                                'pdf': inputValues3['novo_pdf'], 
                                                                'publish_date': inputValues3['nova_data'],
                                                                'title': inputValues3['novo_titulo'], 
                                                                'url': inputValues3['novo_url'],
                                                            }

                                                            publicacoes = fc.alterarDetalhesPub(inputValues3['novo_titulo'],inputValues3['novo_resumo'],inputValues3['novas_palavras'],autores,inputValues3['nova_data'],inputValues3['novo_doi'],inputValues3['novo_pdf'],inputValues3['novo_url'], BD)
                                                            sg.popup('Publicação alterada com sucesso!',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                            stopform3 = True
                                                    wform3.close()
                                    else:
                                        janelaErro("Nenhum resultado encontrado.")
                                else:
                                    janelaErro("Por favor, insira a data.")

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
                                reading_form = False  
                                wform.close()

                            elif event_form == 'Consultar':
                                palavraschave = values_form.get('-PALAVRASCHAVE-')
                                if palavraschave != '':
                                    
                                    resultados = fc.filterpalavrachave(BD, palavraschave)  
                                
                                    if resultados:
                                    
                                        layout_resultados = [
                                            [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                            [sg.Listbox(values=[res for res in resultados], size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                            [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),
                                            sg.Button('Alterar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                        ]

                                    
                                        janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                        janela_aberta = True

                                        while janela_aberta:
                                            evento_resultados, valores_resultados = janela_resultados.read()
                                            if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                                janela_aberta = False
                                                janela_resultados.close()
                                            elif evento_resultados == 'Alterar':
                                                
                                                titulo = ""
                                                resumo = ""
                                                palavraschaves = ""
                                                autores = []
                                                data = ""
                                                doi = ""
                                                pdf = ""
                                                url = ""
                                                titulo_selecionado = valores_resultados["-RESULTADOS-"][0]
                                
                                                if isinstance(titulo_selecionado, dict):
                                                    
                                                        titulo = titulo_selecionado.get('title')
                                                        resumo = titulo_selecionado.get('abstract')
                                                        palavraschaves = titulo_selecionado.get('keywords')
                                                        autores = titulo_selecionado.get('authors')
                                                        data = titulo_selecionado.get('publish_date')
                                                        pdf = titulo_selecionado.get('pdf')
                                                        doi = titulo_selecionado.get('doi')
                                                        url = titulo_selecionado.get('url')
                                                janela_aberta = False
                                                janela_resultados.close()
                                                if titulo_selecionado:
                                                        
                                                    formLayout3 = [
                                                        [sg.Column([
                                                        [sg.Text('*Título:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=titulo,key='novo_titulo')],
                                                        [sg.Text('*Resumo:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=resumo,key='novo_resumo')],
                                                        [sg.Text('*Palavras-chave:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=palavraschaves,key='novas_palavras')],
                                                        [sg.Text('*Autores:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro)],
                                                        [sg.Text('*Nome:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-name-')],
                                                        [sg.Text('*Afiliação:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-affiliation-')],
                                                        [sg.Listbox(values=autores, size=(70, 10), key='-AUTORES-', pad=((0, 0), (15, 10)), enable_events=True),sg.Button('Adicionar Autor', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-ADICIONAR-',size=(15,1)),sg.Button('Remover Autor', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-REMOVER-',size=(15,1))],
                                                        [sg.Text('*Data de publicação:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.CalendarButton('Escolha a data', target='-data_publicação-', key='calendario',font=("Cooper Hewitt", 12), format='%Y-%m-%d', button_color=(claro, escuro), size=(20,1))],
                                                        [sg.InputText(default_text=data,key='nova_data', pad=((480, 0), (0, 0)))],
                                                        [sg.Text('*doi:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=doi,key='novo_doi')],
                                                        [sg.Text('*pdf:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=pdf,key='novo_pdf')],
                                                        [sg.Text('*url:', size=(10, 1), expand_x=True, font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText(default_text=url,key='novo_url')],
                                                        [sg.Text('* Indica um campo obrigatório', font=("Bid Shoulders Display", 12), background_color=claro, text_color=escuro, expand_x=True, enable_events=True)],
                                                        [sg.Button('Salvar', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-SALVAR-',size=(10,1)),sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12), key='-CANCELAR-', size=(10,1))]
                                                        ], size=(800, 1000), background_color=claro)]
                                                        ]

                                                    wform3 = sg.Window('Alterar uma publicação', formLayout3, background_color=claro, resizable=True)
                                                    stopform3 = False

                                                    while not stopform3:
                                                        inputEvent3, inputValues3 = wform3.read()

                                                        if inputEvent3 in [sg.WIN_CLOSED, '-CANCELAR-']:
                                                            stopform3 = True

                                                        elif inputEvent3 == '-ADICIONAR-':
                                                            nome = inputValues3['-name-']
                                                            afiliacao = inputValues3['-affiliation-']

                                                            if nome and afiliacao:  
                                                                autor = {'name': nome, 'affiliation': afiliacao}  
                                                                autores.append(f"{autor}") 
                                                                wform3["-AUTORES-"].update(autores)  
                                                                wform3["-name-"].update("")  
                                                                wform3["-affiliation-"].update("")  
                                                            else:
                                                                janelaErro("Preencha o nome e a afiliação do autor!") 

                                                        elif inputEvent3 == '-REMOVER-':
                                                            if inputValues3['-AUTORES-']:  
                                                                autor_selecionado = inputValues3['-AUTORES-'][0]  
                                                                if autor_selecionado in autores:  
                                                                    autores.remove(autor_selecionado)  
                                                                    wform3["-AUTORES-"].update(autores)  
                                                                else:
                                                                    janelaErro("Autor não encontrado na lista!")  
                                                            else:
                                                                janelaErro("Selecione um autor para remover!") 

                                                        elif any(inputValues3[k] == '' for k in ['novo_titulo', 'novo_resumo', 'novas_palavras', 'nova_data', 'novo_doi', 'novo_pdf', 'novo_url']) or not autores:
                                                            janelaErro('Preencha todos os campos obrigatórios (*)!')
                                                    
                                                        elif inputEvent3 == '-SALVAR-':
                                                            
                                                            novatarefa = { 
                                                                'abstract': inputValues3['novo_resumo'],
                                                                'keywords': inputValues3['novas_palavras'],
                                                                'authors': autores,
                                                                'doi': inputValues3['novo_doi'], 
                                                                'pdf': inputValues3['novo_pdf'], 
                                                                'publish_date': inputValues3['nova_data'],
                                                                'title': inputValues3['novo_titulo'], 
                                                                'url': inputValues3['novo_url'],
                                                            }

                                                            publicacoes = fc.alterarDetalhesPub(inputValues3['novo_titulo'],inputValues3['novo_resumo'],inputValues3['novas_palavras'],autores,inputValues3['nova_data'],inputValues3['novo_doi'],inputValues3['novo_pdf'],inputValues3['novo_url'], BD)
                                                            sg.popup('Publicação alterada com sucesso!',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                            stopform3 = True
                                                    wform3.close()
                                    else:
                                        janelaErro("Nenhum resultado encontrado.")
                                else:
                                    janelaErro("Por favor, insira a palavra-chave.")    

        #----- Criar Publicação -----
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
                            autor = {'name': inputValues3['-name-'], 'affiliation':inputValues3['-affiliation-'] }  
                            autores.append(autor) 
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
                        window["-DADOS-"].update('Publicação adicionada com sucesso!')
                        wform3.close()

        #-----Estatísticas----
        elif eventos == "-ESTATISTICAS-":  
            if BD== None:
                window["-DADOS-"].update("Primeiro carregue a base de dados!")
            else:
                window["-DADOS-"].update("A produzir dados estatísticos...")
                formLayout = [ 
                    [sg.Text('Gráficos:', font=("Cambria", 16), background_color=claro, text_color=escuro, pad=(0, 10))],
                    [sg.Column([
                        [sg.Button("Distribuição de Publicações por ano", font=("Cooper Hewitt", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("Distribuição de Publicações por mês de um determinado ano", font=("Cooper Hewitt", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("Número de publicações por autor(top20)", font=("Cooper Hewitt", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("Distribuição de publicações de um autor por anos", font=("Cooper Hewitt", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("Distribuição de palavras-chave pela frequência(top20)", font=("Cooper Hewitt", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("Distribuição de palavras-chave mais frequentes por ano", font=("Cooper Hewitt", 12), pad=(0, 5), button_color=(claro, escuro))]
                    ], background_color=claro, element_justification="left", pad=(0, 10))]
                ]

                janelanov = sg.Window('Dados estatísticos', formLayout, background_color=claro, element_justification="left",resizable=True)

                stopForm = False
                while not stopForm:
                    inputEvent, inputValues = janelanov.read()
                    if inputEvent == sg.WIN_CLOSED:
                        stopForm=True
                        window["-DADOS-"].update("")
                    else:
                        if inputEvent== "Distribuição de Publicações por ano":
                            threading.Thread(target=fc.pubano, args=(BD,), daemon = True).start()
                        elif inputEvent == "Distribuição de Publicações por mês de um determinado ano":
                            window["-DADOS-"].update("A produzir dados estatísticos...")
                            layout_por_ano = [
                                [sg.Text('Escolha o ano para exibir:', size=(45, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                [sg.Combo(values=fc.listanos(BD), key='-ANO-', font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro, size=(20, 1))],
                                [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                            ]
                            window_por_ano = sg.Window(title="Selecione o ano", layout=layout_por_ano, resizable=True, background_color=claro)

                            continuar = True  
                            while continuar:
                                event, values = window_por_ano.read()
                                if event in (sg.WINDOW_CLOSED, 'Cancelar'):
                                    continuar = False
                                elif event == 'Consultar':
                                    ano = values['-ANO-']
                                    if ano:
                                        threading.Thread(target=fc.mesano, args=(BD, ano), daemon = True).start() 
                                        continuar = False  
                                    else:
                                        sg.popup("Por favor, selecione um ano.", title="Erro", background_color=claro, text_color=escuro)
                            window_por_ano.close()
                        elif inputEvent== "Número de publicações por autor(top20)":
                            threading.Thread(target=fc.npubautor, args=(BD,),daemon = True).start()
                        elif inputEvent == "Distribuição de publicações de um autor por anos":
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

                                if event in (sg.WINDOW_CLOSED, 'Cancelar'):  
                                    continue_reading = False

                                elif event == 'Consultar':
                                    autor = values.get('-AUTOR-')  
                                    if autor:
                                        threading.Thread(target=fc.pubautorano, args=(BD,autor),daemon = True).start()
                                        
                                          
                                    else:
                                        sg.popup("Por favor, insira o nome do autor.", title="Erro", background_color=claro, text_color=escuro)

                            wform.close()
                        elif inputEvent== "Distribuição de palavras-chave pela frequência(top20)":
                            threading.Thread(target=fc.palavrafreq, args=(BD,),daemon = True).start()
                        else:
                            window["-DADOS-"].update("A produzir dados estatísticos...")
                            layout_por_ano = [
                                [sg.Text('Escolha o ano para exibir:', size=(45, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                [sg.Combo(values=fc.listanos(BD), key='-ANO-', font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro, size=(20, 1))],
                                [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                            ]
                            window_por_ano = sg.Window(title="Selecione o ano", layout=layout_por_ano, resizable=True, background_color=claro)

                            continuar = True 
                            while continuar:
                                event, values = window_por_ano.read()
                                if event in (sg.WINDOW_CLOSED, 'Cancelar'):
                                    continuar = False
                                elif event == 'Consultar':
                                    ano = values['-ANO-']
                                    if ano:
                                        threading.Thread(target=fc.palavrafreqano, args=(BD,ano),daemon = True).start()  
                                        continuar = False  
                                    else:
                                        sg.popup("Por favor, selecione um ano.", title="Erro", background_color=claro, text_color=escuro)
                            window_por_ano.close()  
                        window["-DADOS-"].update("Dados estatísticos calculados com sucesso!")
            



        #----- Eliminar ------
        elif eventos == "-ELIMINAR-":
            window["-DADOS-"].update("Preparar para eliminar...")
            if BD is None:
                janelaErro("Introduza primeiro uma base de dados!")
                
            elif Guardada == 0:
                janelaErro("Guarde primeiro a base de dados!")
                
            else:
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
                        window8.close() 

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
                                reading_form = False  
                            elif event_form == 'Consultar':
                                titulo = values_form.get('-TITULO-')
                                print(f"Título inserido: {titulo}")  
                                if titulo != '':
                                    
                                    resultados = fc.filtertitle(BD, titulo) 
                                    print(f"Resultados encontrados: {resultados}")  
                                    if resultados:
                                        
                                        layout_resultados = [
                                            [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                            [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                            [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),
                                            sg.Button('Eliminar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                        ]

                                        
                                        janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                        janela_aberta = True

                                        while janela_aberta:
                                            evento_resultados, valores_resultados = janela_resultados.read()
                                            if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                                janela_aberta = False  
                                                janela_resultados.close()
                                            elif evento_resultados == 'Eliminar':
                                                
                                                publicacao_selecionada = valores_resultados.get('-RESULTADOS-')
                                                if publicacao_selecionada:
                                                    publicacao_selecionada = publicacao_selecionada[0]  
                                                    confirmacao = sg.popup_yes_no(
                                                        "Tem certeza de que deseja apagar esta publicação?",
                                                        title="Confirmação",
                                                        background_color=claro,
                                                        text_color=escuro,
                                                        button_color=(claro, escuro),
                                                        font=("Cooper Hewitt",12)
                                                    )
                                                    if confirmacao == 'Yes':
                                                        
                                                        BD.remove(publicacao_selecionada)
                                                        sg.popup('Publicação removida com sucesso!',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )  
                                                        
                                                        resultados.remove(publicacao_selecionada)  
                                                        janela_resultados['-RESULTADOS-'].update(values=resultados)  
                                                    else:
                                                        sg.popup('Operação cancelada.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                        
                                                else:
                                                    sg.popup('Por favor, selecione uma publicação para eliminar.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                    
                                    else:
                                        sg.popup('Nenhum resultado encontrado',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                        
                                else:
                                    sg.popup('Por favor, insira o título.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                


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
                                        reading_form = False 
                                    

                                    elif event_form == 'Consultar':
                                        autor = values_form.get('-AUTOR-')
                                        print(f"autor inserido: {autor}")  
                                        if autor != '':
                                            
                                            resultados = fc.filterauthor(BD, autor)  
                                            print(f"Resultados encontrados: {resultados}")  
                                            if resultados:
                                            
                                                layout_resultados = [
                                                    [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                                    [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                                    [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),sg.Button('Eliminar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                                ]

                                                
                                                janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                                janela_aberta = True

                                                while janela_aberta:
                                                    evento_resultados, valores_resultados = janela_resultados.read()
                                                    if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                                        janela_aberta = False  
                                                        janela_resultados.close()
                                                    elif evento_resultados == 'Eliminar':
                                                    
                                                        publicacao_selecionada = valores_resultados.get('-RESULTADOS-')
                                                        if publicacao_selecionada:
                                                            publicacao_selecionada = publicacao_selecionada[0]  
                                                            confirmacao = sg.popup_yes_no(
                                                        "Tem certeza de que deseja apagar esta publicação?",
                                                        title="Confirmação",
                                                        background_color=claro,
                                                        text_color=escuro,
                                                        button_color=(claro, escuro),
                                                        font=("Cooper Hewitt",12)
                                                    )
                                                            if confirmacao == 'Yes':
                                                                
                                                                BD.remove(publicacao_selecionada)
                                                                sg.popup('Publicação removida com sucesso!',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )  
                                                                
                                                                resultados.remove(publicacao_selecionada)  
                                                                janela_resultados['-RESULTADOS-'].update(values=resultados)  
                                                            else:
                                                                sg.popup('Operação cancelada.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                                
                                                else:
                                                    sg.popup('Por favor, selecione uma publicação para eliminar.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                    
                                            else:
                                                sg.popup('Nenhum resultado encontrado',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                
                                        else:
                                            sg.popup('Por favor, insira o autor.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                wform.close()             
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
                                        reading_form = False 

                                    elif event_form == 'Consultar':
                                        afiliacao = values_form.get('-AFILIACAO-')
                                        print(f"afiliação inserido: {afiliacao}")  
                                        if afiliacao!= '':
                                            
                                            resultados = fc.filterafiliation(BD, afiliacao) 
                                            print(f"Resultados encontrados: {resultados}")  
                                            if resultados:
                                                
                                                layout_resultados = [
                                                    [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                                    [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                                    [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),sg.Button('Eliminar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                                ]

                                                
                                                janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                                janela_aberta = True

                                                while janela_aberta:
                                                    evento_resultados, valores_resultados = janela_resultados.read()
                                                    if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                                        janela_aberta = False  
                                                        janela_resultados.close()
                                                    elif evento_resultados == 'Eliminar':
                                                        
                                                        publicacao_selecionada = valores_resultados.get('-RESULTADOS-')
                                                        if publicacao_selecionada:
                                                            publicacao_selecionada = publicacao_selecionada[0]  
                                                            confirmacao = sg.popup_yes_no(
                                                        "Tem certeza de que deseja apagar esta publicação?",
                                                        title="Confirmação",
                                                        background_color=claro,
                                                        text_color=escuro,
                                                        button_color=(claro, escuro),
                                                        font=("Cooper Hewitt",12)
                                                    )
                                                            
                                                            if confirmacao == 'Yes':
                                                                
                                                                BD.remove(publicacao_selecionada)
                                                                sg.popup('Publicação removida com sucesso!',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )  
                                                                
                                                                resultados.remove(publicacao_selecionada)  
                                                                janela_resultados['-RESULTADOS-'].update(values=resultados) 
                                                            else:
                                                                sg.popup('Operação cancelada.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                            
                                                else:
                                                    sg.popup('Por favor, selecione uma publicação para eliminar.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                    
                                            else:
                                                sg.popup('Nenhum resultado encontrado',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                            
                                        else:
                                            sg.popup('Por favor, insira a afiliação.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                            
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
                            if eventos10 in [sg.WIN_CLOSED, 'Cancelar']:
                                reading_date = False
                                window10.close()  
                            elif eventos10 == 'Consultar':
                                data = valores10.get('-DATA-')
                                if data:
                                    resultados = fc.filterdata(BD, data)  
                                    if resultados:
                                        
                                        layout_resultados = [
                                            [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                            [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                            [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),sg.Button('Eliminar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                        ]

                                        
                                        janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                        janela_aberta = True

                                        while janela_aberta:
                                            evento_resultados, valores_resultados = janela_resultados.read()
                                            if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                                janela_aberta = False  
                                                janela_resultados.close()
                                            elif evento_resultados == 'Eliminar':
                                            
                                                publicacao_selecionada = valores_resultados.get('-RESULTADOS-')
                                                if publicacao_selecionada:
                                                    publicacao_selecionada = publicacao_selecionada[0]  
                                                    confirmacao = sg.popup_yes_no(
                                                        "Tem certeza de que deseja apagar esta publicação?",
                                                        title="Confirmação",
                                                        background_color=claro,
                                                        text_color=escuro,
                                                        button_color=(claro, escuro),
                                                        font=("Cooper Hewitt",12)
                                                    )
                                                    
                                                    if confirmacao == 'Yes':
                                                        
                                                        BD.remove(publicacao_selecionada)
                                                        sg.popup('Publicação removida com sucess!',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )  
                                                        resultados.remove(publicacao_selecionada)  
                                                        janela_resultados['-RESULTADOS-'].update(values=resultados)  
                                                    else:
                                                        sg.popup('Operação cancelada.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                        
                                                else:
                                                    sg.popup('Por favor, selecione uma publicação para eliminar.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                    
                                    

                                    else:
                                        sg.popup('Nenhum resultado encontrado',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                        
                                else:
                                    sg.popup('Por favor, insira a data.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                    
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
                                        reading_form = False  
                                    elif event_form == 'Consultar':
                                        palavraschave = values_form.get('-PALAVRASCHAVE-')
                                        if palavraschave != '':
                                            
                                            resultados = fc.filterpalavrachave(BD, palavraschave)  
                                            if resultados:
                                                
                                                layout_resultados = [
                                                    [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                                    [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                                    [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),sg.Button('Eliminar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                                ]

                                                
                                                janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                                janela_aberta = True

                                                while janela_aberta:
                                                    evento_resultados, valores_resultados = janela_resultados.read()
                                                    if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                                        janela_aberta = False  
                                                        janela_resultados.close()
                                                    elif evento_resultados == 'Eliminar':
                                                        
                                                        publicacao_selecionada = valores_resultados.get('-RESULTADOS-')
                                                        if publicacao_selecionada:
                                                            publicacao_selecionada = publicacao_selecionada[0]  
                                                            confirmacao = sg.popup_yes_no(
                                                        "Tem certeza de que deseja apagar esta publicação?",
                                                        title="Confirmação",
                                                        background_color=claro,
                                                        text_color=escuro,
                                                        button_color=(claro, escuro),
                                                        font=("Cooper Hewitt",12)
                                                    )
            
                                                            if confirmacao == 'Yes':
                                                                
                                                                BD.remove(publicacao_selecionada) 
                                                                sg.popup('Publicação removida com sucesso!',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                                resultados.remove(publicacao_selecionada)  
                                                                janela_resultados['-RESULTADOS-'].update(values=resultados) 
                                                            else:
                                                                sg.popup('Operação cancelada.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                                
                                                else:
                                                    sg.popup('Por favor, selecione uma publicação para eliminar.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                    
                                            else:
                                                sg.popup('Nenhum resultado encontrado',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )
                                                
                                        else:
                                            sg.popup('Por favor, insira a palavra-chave.',  
                                                                background_color=claro,
                                                                text_color=escuro,
                                                                button_color=(claro, escuro),  
                                                                font=("Cooper Hewitt", 12)
                                                                )

interface_grafica()