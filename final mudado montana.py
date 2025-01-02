import FreeSimpleGUI as sg
import tkinter as tk
import tkinter as ttk
#Carregar BD
import json
def carregar_dataset(fnome):
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    if bd == "":
        print("Nenhum ficheiro foi especificado.")
    else:
        print(f"Dados carregados com sucesso. Foram lidas um total de {len(bd)} publicações.")
    return bd 

#----- Armazenamento de Dados -----#

def guardar_dataset(nome,dataset):
    ficheiro = open(nome,'w',encoding='utf-8')
    json.dump(dataset,ficheiro,ensure_ascii=False,indent=2)
    ficheiro.close()

#----- Consultar Publicação -----#
##Ordenar publicações encontradas pela data de publicação
def ordenadate(d):
    date = []
    for pub in d:
        if "publish_date" not in pub.keys():
            pub['publish_date'] = "0000-00-00"
            date.append(pub)
        else:
            date.append(pub)
    return sorted(date, key = lambda x:x.get('publish_date'))

##Ordenar publicações encontradas pelos títulos 
def ordenatitle(d):
    return sorted(d, key = lambda x:x.get('title'))

##Pesquisa de publicações por título 

def filtertitle(fnome, titulo):
    d = []
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
        if pub.get('title') == titulo:
            d.append(pub)
    return d

##Pesquisa de publicações por autor

def filterauthor(fnome, autor):
    d = []
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
        for a in pub['authors']:
            if a.get('name') == autor:
                d.append(pub)
    return d


##Pesquisa de publicações por afiliação
def filterafiliation(fnome, afiliação):
    d = []
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
        for a in pub['authors']:
            if a.get("affiliation") == afiliação:
                d.append(pub)
    return d

##Pesquisa de publicações por data de publiblicação:
import json
def filterdata(fnome, data):
    d = []
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
        if pub.get("publish_date") == data:
                d.append(pub)
    return d

##Pesquisa de publicações por palavras chaves:
import json
def filterpalavrachave(fnome, palavrachave):
    d = []
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
            palavras = pub.get("keywords")  
            if palavras:
                listapal = palavras.split(",")
                for pal in listapal:
                    if pal.strip().lower() == palavrachave.lower():  
                        d.append(pub)
    return d

#------ Exportação Parcial de Dados------#

def exportar_dados(nome_arquivo, dados):
    try:
        # Escreve os dados no arquivo JSON
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        return f"Dados exportados com sucesso para {nome_arquivo}."
    except Exception as e:
        return f"Erro ao exportar os dados: {e}"


#---Filtrar pub-----
def filtrar_publicacoes(filtro, valor, BD):
    dados_filtrados = []
    for pub in BD:
        campo = pub.get(filtro)
        
        if filtro == 'authors':  # Caso seja necessário filtrar por autores
            if isinstance(campo, list):  # Verifica se o campo é uma lista
                for autor in campo:
                    if isinstance(autor, dict):  # Garante que é um dicionário
                        nome = autor.get('name', '')
                        if isinstance(nome, str) and valor.lower() in nome.lower():
                            dados_filtrados.append(pub)
                            break  # Encontra um autor correspondente, adiciona a publicação e interrompe
            
        elif isinstance(campo, str):  # Para outros casos que retornam strings
            if valor.lower() in campo.lower():
                dados_filtrados.append(pub)
    
    return dados_filtrados






# Cores personalizadas
escuro = '#8C6057'
claro = '#FAF3E0'
tijolo = '#DC143C'

#Janela de erro
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





# Interface gráfica
def interface_grafica():
    # Layout do lado esquerdo: título centralizado verticalmente
    esquerda_layout = [
        # Espaço expansível para centralização vertical
        [sg.Push(background_color=claro)],
        # Título centralizado
        [sg.Text("Sistema de Consulta e Análise de Publicações Científicas",
                 font=("Cambria", 30, "bold"), text_color=escuro, background_color=claro,
                 justification="center", size=(25, 2), expand_x=True)],
        # Espaço expansível para centralização vertical
        [sg.Push(background_color=claro)],
        # Botões Sair e Help alinhados horizontalmente
        [sg.Push(background_color=claro),
         sg.Button("Sair", size=(10, 1), font=("Cambria", 14),
                   button_color=(claro,tijolo), key="-SAIR-"),
         sg.Button("Help", size=(10, 1), font=("Cambria", 14),
                   button_color=(claro, escuro), key="-HELP-"),
         sg.Push(background_color=claro)]
    ]
    
    # Layout do menu: 10 opções em 2 colunas
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
              sg.Button("Eliminar Publicação", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-ELIMINAR-")]],
              
              
            background_color=claro, element_justification="center"
        )],
        # Janela de dados centralizada abaixo do menu
        [sg.Text("", size=(60, 1), font=("Cambria", 16), justification="center", key="-DADOS-",
                 background_color=claro, text_color=escuro)]
    ]
    

    # Layout principal
    layout = [
        [sg.Column(esquerda_layout, background_color=claro, vertical_alignment="center", element_justification="left"),
         sg.VSep(),
         sg.Column(menu_layout, background_color=claro, vertical_alignment="center", element_justification="center", expand_y=True)]
    ]

    # Criar a janela
    window = sg.Window("Sistema de Consulta e Análise de Publicações Científicas", layout,resizable=False,
                       background_color=claro,location=(0,0))
    stop = False
    while stop == False:

        eventos, valores = window.read()
        
        if eventos in [sg.WIN_CLOSED, 'Exit']:
            stop = True

        elif eventos == '-SAIR-':
            stop = True
            window.close()


        elif eventos == "-CARREGAR-":  
            window["-DADOS-"].update("A carregar a base de dados...")
            formLayout = [
                [
                sg.Text("Base de dados:", font=("Cooper Hewitt", 12), pad=(0, 30), text_color=claro, background_color=escuro),
                sg.InputText(key="-FICHEIRO-", readonly=True, enable_events=True, text_color=escuro),
                sg.FileBrowse(file_types=[("JSON (*.json)", "*.json")], size=(8, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                sg.Button(key="-CARREGAR-", button_text="Carregar", size=(12, 1), disabled=True, font=("Cooper Hewitt", 12), button_color=(claro, escuro)) 
                ]
            ]

            wform = sg.Window('Carregamento da base de dados',formLayout, size=(650,100), background_color=claro)

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
                        BD = carregar_dataset(inputValues['Browse'])
                        nome = inputValues['Browse']
                        stopform = True
                        window["-DADOS-"].update("Base de dados carregada com sucesso!")
                        wform.close()
        elif eventos == "-GRAVAR-":
            window["-DADOS-"].update("A gravar base de dados...")
            
            if BD == None:
                janelaErro("Introduza primeiro uma base de dados!")
            
            else:
                Guardada = 1
                guardar_dataset(nome, BD)
                window["-DADOS-"].update("Base de dados gravada!")

  
        elif eventos == "-CONSULTAR-":
            window["-DADOS-"].update("A consultar publicação...")

            if BD == None:
                janelaErro("Introduza primeiro uma base de dados!")

            elif Guardada == 0:
                janelaErro("Guarde primeiro a base de dados!")

            else:
                layout8 = [
                    [sg.Text('Deseja consultar a publicação por:',
                        size=(45, 1), font=("Cambria", 15, "bold"),
                        background_color=claro, text_color=escuro)],
                    [sg.Button('Título', size=(20, 1), button_color=(claro, escuro),
                        font=("Cooper Hewitt", 12)),
                     sg.Button('Autor', size=(20, 1), button_color=(claro, escuro),
                        font=("Cooper Hewitt", 12)),
                     sg.Button('Afiliação', size=(20, 1), button_color=(claro, escuro),
                        font=("Cooper Hewitt", 12)),
                     sg.Button('Data de Publicação', size=(20, 1), button_color=(claro, escuro),
                        font=("Cooper Hewitt", 12)),
                     sg.Button('Palavras-chave', size=(20, 1), button_color=(claro, escuro),
                        font=("Cooper Hewitt", 12)),
                     sg.Button('Retornar ao Menu', size=(20, 1),
                        font=("Cooper Hewitt", 12), button_color=(claro, tijolo))]
                ]

                window8 = sg.Window(title="Consultar Publicação", layout=layout8, background_color=claro)

                stop8 = False
                while not stop8:
                    eventos8, _ = window8.read()
                    if eventos8 in [sg.WIN_CLOSED, 'Retornar ao Menu']:
                        stop8 = True
                        window8.close()

                    elif eventos8 == 'Título':
                        window8.close()

                        layout9 = [
                            [sg.Text('Deseja ordenar por data de publicação ou por título?',
                                font=("Cooper Hewitt", 12), background_color=escuro,
                                text_color=claro)],
                            [sg.Radio("Data de publicação", "OPCAO", default=False, key="-OPC1-",
                                font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro),
                             sg.Radio("Título", "OPCAO", default=True, key="-OPC2-",
                                font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro)],
                            [sg.Text('Título:', font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro)],
                            [sg.InputText(key='-CON-', size=(58, 0), font=("Cooper Hewitt", 12))],
                            [sg.Button('Procurar', size=(10, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                             sg.Button('Voltar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                        ]

                        window9 = sg.Window(title="Consultar Publicação pelo Título", layout=layout9, background_color=claro)

                        stop9 = False
                        while not stop9:
                            eventos9, valores9 = window9.read()
                            if eventos9 in [sg.WIN_CLOSED, 'Voltar']:
                                stop9 = True
                                window9.close()
                                # Reabrir a janela principal de consulta
                                layout8 = [
                                    [sg.Text('Deseja consultar a publicação por:', size=(45, 1), expand_x=True,
                                        font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                    [sg.Button('Título', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Autor', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Afiliação', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Data de Publicação', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Palavras-chave', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Retornar ao Menu', size=(20, 1), font=("Cooper Hewitt", 12), button_color=(claro, tijolo))],
                                ]
                                window8 = sg.Window(title="Consultar Publicação", resizable=False, background_color=claro).Layout(layout8)

                            elif eventos9 == 'Procurar':
                                titulo_consulta = valores9['-CON-']
                                if titulo_consulta:
                                # Filtrar publicações
                                    resultados = filtertitle(nome, titulo_consulta)
                                    if resultados:
                                        info_resultados = ""
                                        for pub in resultados:
                                            autores_info = "\n".join([f"    - {autor['name']} (Afilição: {autor.get('affiliation', 'N/A')})" for autor in pub.get('authors', [])])
                                            info_resultados += (
                                                f"Título: {pub.get('title', 'Título desconhecido')}\n"
                                                f"Resumo: {pub.get('abstract', 'Resumo não disponível')}\n"
                                                f"Palavras-chave: {pub.get('keywords', ['Nenhuma palavra-chave'])}\n"
                                                f"Autores:\n{autores_info if autores_info else '    Nenhum autor disponível'}\n"
                                                f"DOI: {pub.get('doi', 'DOI não disponível')}\n"
                                                f"PDF: {pub.get('pdf', 'PDF não disponível')}\n"
                                                f"Data de Publicação: {pub.get('publish_date', 'Data desconhecida')}\n"
                                                f"URL: {pub.get('url', 'URL não disponível')}\n"
                                                f"{'-'*40}\n" 
                                            )
                                        layout_resultados = [
                                            [sg.Text("Resultados encontrados!", font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                            [sg.Multiline(info_resultados, size=(80, 20), font=("Cambria", 12), background_color=claro, text_color=escuro, disabled=True)],
                                            [sg.Button("Fechar", font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
                                        ]

                                        janela_resultados = sg.Window("Resultados da Consulta", layout_resultados, background_color=claro, resizable=True)

                                        
                                        while True:
                                            evento_resultados, _ = janela_resultados.read()
                                            if evento_resultados in [sg.WIN_CLOSED, "Fechar"]:
                                                break

                                        janela_resultados.close()
                                    else:
                                        sg.popup("Nenhuma publicação encontrada com esse título!")
                                else:
                                    sg.popup("Por favor, insira um título válido.")


                    elif eventos8 == 'Autor':
                        window8.close()

                        layout9 = [
                            [sg.Text('Deseja ordenar por data de publicação ou por título?',
                                font=("Cooper Hewitt", 12), background_color=escuro,
                                text_color=claro)],
                            [sg.Radio("Data de publicação", "OPCAO", default=False, key="-OPC1-",
                                font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro),
                             sg.Radio("Título", "OPCAO", default=True, key="-OPC2-",
                                font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro)],
                            [sg.Text('Autor:', font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro)],
                            [sg.InputText(key='-CON-', size=(58, 0), font=("Cooper Hewitt", 12))],
                            [sg.Button('Procurar', size=(10, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                             sg.Button('Voltar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                        ]

                        window9 = sg.Window(title="Consultar Publicação pelo Autor", layout=layout9, background_color=claro)

                        stop9 = False
                        while not stop9:
                            eventos9, valores9 = window9.read()
                            if eventos9 in [sg.WIN_CLOSED, 'Voltar']:
                                stop9 = True
                                window9.close()
                                # Reabrir a janela principal de consulta
                                layout8 = [
                                    [sg.Text('Deseja consultar a publicação por:', size=(45, 1), expand_x=True,
                                        font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                    [sg.Button('Título', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Autor', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Afiliação', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Data de Publicação', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Palavras-chave', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Retornar ao Menu', size=(20, 1), font=("Cooper Hewitt", 12), button_color=(claro, tijolo))],
                                ]
                                window8 = sg.Window(title="Consultar Publicação", resizable=False, background_color=claro).Layout(layout8)

                            elif eventos9 == 'Procurar':
                                autor_consulta = valores9['-CON-']
                                if autor_consulta:
                                # Filtrar publicações pelo nome do autor
                                    resultados = filterauthor(nome, autor_consulta)  # Função que filtra publicações pelo autor
                                    if resultados:
                                        info_resultados = ""
                                        for pub in resultados:
                                            autores_info = "\n".join([f"    - {autor['name']} (Afilição: {autor.get('affiliation', 'N/A')})" for autor in pub.get('authors', [])])
                                            info_resultados += (
                                                f"Título: {pub.get('title', 'Título desconhecido')}\n"
                                                f"Resumo: {pub.get('abstract', 'Resumo não disponível')}\n"
                                                f"Palavras-chave: {pub.get('keywords', ['Nenhuma palavra-chave'])}\n"
                                                f"Autores:\n{autores_info if autores_info else '    Nenhum autor disponível'}\n"
                                                f"DOI: {pub.get('doi', 'DOI não disponível')}\n"
                                                f"PDF: {pub.get('pdf', 'PDF não disponível')}\n"
                                                f"Data de Publicação: {pub.get('publish_date', 'Data desconhecida')}\n"
                                                f"URL: {pub.get('url', 'URL não disponível')}\n"
                                                f"{'-'*40}\n"  
                                            )
                                        layout_resultados = [
                                            [sg.Text(f"Publicações de {autor_consulta} encontradas!", font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                            [sg.Multiline(info_resultados, size=(80, 20), font=("Cambria", 12), background_color=claro, text_color=escuro, disabled=True)],
                                            [sg.Button("Fechar", font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
                                        ]

                                        janela_resultados = sg.Window("Resultados da Consulta", layout_resultados, background_color=claro, resizable=True)

                                        while True:
                                            evento_resultados, _ = janela_resultados.read()
                                            if evento_resultados in [sg.WIN_CLOSED, "Fechar"]:
                                                break

                                        janela_resultados.close()
                                    else:
                                        sg.popup(f"Nenhuma publicação encontrada para o autor: {autor_consulta}")
                                else:
                                    sg.popup("Por favor, insira um nome de autor válido.")


                    elif eventos8 == 'Afiliação':
                        window8.close()

                        layout9 = [
                            [sg.Text('Deseja ordenar por data de publicação ou por título?',
                                font=("Cooper Hewitt", 12), background_color=escuro,
                                text_color=claro)],
                            [sg.Radio("Data de publicação", "OPCAO", default=False, key="-OPC1-",
                                font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro),
                             sg.Radio("Título", "OPCAO", default=True, key="-OPC2-",
                                font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro)],
                            [sg.Text('Afiliação:', font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro)],
                            [sg.InputText(key='-CON-', size=(58, 0), font=("Cooper Hewitt", 12))],
                            [sg.Button('Procurar', size=(10, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                             sg.Button('Voltar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                        ]

                        window9 = sg.Window(title="Consultar Publicação pela Afiliação", layout=layout9, background_color=claro)

                        stop9 = False
                        while not stop9:
                            eventos9, valores9 = window9.read()
                            if eventos9 in [sg.WIN_CLOSED, 'Voltar']:
                                stop9 = True
                                window9.close()
                                # Reabrir a janela principal de consulta
                                layout8 = [
                                    [sg.Text('Deseja consultar a publicação por:', size=(45, 1), expand_x=True,
                                        font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                    [sg.Button('Título', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Autor', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Afiliação', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Data de Publicação', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Palavras-chave', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Retornar ao Menu', size=(20, 1), font=("Cooper Hewitt", 12), button_color=(claro, tijolo))],
                                ]
                                window8 = sg.Window(title="Consultar Publicação", resizable=False, background_color=claro).Layout(layout8)

                            elif eventos9 == 'Procurar':
                                afiliacao_consulta = valores9['-CON-']
                                if afiliacao_consulta:
                                    # Filtrar publicações pela afiliação
                                    resultados = filterafiliation(nome, afiliacao_consulta)  # Função que filtra publicações pela afiliação
                                    if resultados:
                                        info_resultados = ""
                                        for pub in resultados:
                        
                                            autores_info = "\n".join([f"    - {autor['name']} (Afiliado(a) a: {autor.get('affiliation', 'N/A')})" for autor in pub.get('authors', [])])
                                            info_resultados += (
                                                f"Título: {pub.get('title', 'Título desconhecido')}\n"
                                                f"Resumo: {pub.get('abstract', 'Resumo não disponível')}\n"
                                                f"Palavras-chave: {pub.get('keywords', ['Nenhuma palavra-chave'])}\n"
                                                f"Autores:\n{autores_info if autores_info else '    Nenhum autor disponível'}\n"
                                                f"DOI: {pub.get('doi', 'DOI não disponível')}\n"
                                                f"PDF: {pub.get('pdf', 'PDF não disponível')}\n"
                                                f"Data de Publicação: {pub.get('publish_date', 'Data desconhecida')}\n"
                                                f"URL: {pub.get('url', 'URL não disponível')}\n"
                                                f"{'-'*40}\n"
                                            )
                                        layout_resultados = [
                                            [sg.Text(f"Publicações relacionadas à afiliação '{afiliacao_consulta}' encontradas!", font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                            [sg.Multiline(info_resultados, size=(80, 20), font=("Cambria", 12), background_color=claro, text_color=escuro, disabled=True)],
                                            [sg.Button("Fechar", font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
                                        ]

                                        janela_resultados = sg.Window("Resultados da Consulta", layout_resultados, background_color=claro, resizable=True)

                                        while True:
                                            evento_resultados, _ = janela_resultados.read()
                                            if evento_resultados in [sg.WIN_CLOSED, "Fechar"]:
                                                break

                                        janela_resultados.close()
                                    else:
                                        sg.popup(f"Nenhuma publicação encontrada para a afiliação: {afiliacao_consulta}")
                                else:
                                    sg.popup("Por favor, insira uma afiliação válida.")


                    elif eventos8 == 'Data de Publicação':
                        window8.close()

                        layout9 = [
                            [sg.Text('Deseja ordenar por data de publicação ou por título?',
                                font=("Cooper Hewitt", 12), background_color=escuro,
                                text_color=claro)],
                            [sg.Radio("Data de publicação", "OPCAO", default=False, key="-OPC1-",
                                font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro),
                             sg.Radio("Título", "OPCAO", default=True, key="-OPC2-",
                                font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro)],
                            [sg.Text('Data(AAAA-MM-DD):', font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro)],
                            [sg.InputText(key='-CON-', size=(58, 0), font=("Cooper Hewitt", 12))],
                            [sg.Button('Procurar', size=(10, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                             sg.Button('Voltar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                        ]

                        window9 = sg.Window(title="Consultar Publicação pela Data", layout=layout9, background_color=claro)

                        stop9 = False
                        while not stop9:
                            eventos9, valores9 = window9.read()
                            if eventos9 in [sg.WIN_CLOSED, 'Voltar']:
                                stop9 = True
                                window9.close()
                                # Reabrir a janela principal de consulta
                                layout8 = [
                                    [sg.Text('Deseja consultar a publicação por:', size=(45, 1), expand_x=True,
                                        font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                    [sg.Button('Título', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Autor', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Afiliação', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Data de Publicação', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Palavras-chave', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Retornar ao Menu', size=(20, 1), font=("Cooper Hewitt", 12), button_color=(claro, tijolo))],
                                ]
                                window8 = sg.Window(title="Consultar Publicação", resizable=False, background_color=claro).Layout(layout8)

                            elif eventos9 == 'Procurar':
                                data_consulta = valores9['-CON-']
                                if data_consulta:
                                # Filtrar publicações
                                    resultados = filterdata(nome, data_consulta)
                                    if resultados:
                                        info_resultados = ""
                                        for pub in resultados:
                                            data_info = "\n".join([f"    - {autor['name']} (Afilição: {autor.get('affiliation', 'N/A')})" for autor in pub.get('authors', [])])
                                            info_resultados += (
                                                f"Título: {pub.get('title', 'Título desconhecido')}\n"
                                                f"Resumo: {pub.get('abstract', 'Resumo não disponível')}\n"
                                                f"Palavras-chave: {pub.get('keywords', ['Nenhuma palavra-chave'])}\n"
                                                f"Autores:\n{data_info if data_info else '    Nenhum autor disponível'}\n"
                                                f"DOI: {pub.get('doi', 'DOI não disponível')}\n"
                                                f"PDF: {pub.get('pdf', 'PDF não disponível')}\n"
                                                f"Data de Publicação: {pub.get('publish_date', 'Data desconhecida')}\n"
                                                f"URL: {pub.get('url', 'URL não disponível')}\n"
                                                f"{'-'*40}\n" 
                                            )
                                        layout_resultados = [
                                            [sg.Text("Resultados encontrados!", font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                            [sg.Multiline(info_resultados, size=(80, 20), font=("Cambria", 12), background_color=claro, text_color=escuro, disabled=True)],
                                            [sg.Button("Fechar", font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
                                        ]

                                        janela_resultados = sg.Window("Resultados da Consulta", layout_resultados, background_color=claro, resizable=True)

                                        
                                        while True:
                                            evento_resultados, _ = janela_resultados.read()
                                            if evento_resultados in [sg.WIN_CLOSED, "Fechar"]:
                                                break

                                        janela_resultados.close()
                                    else:
                                        sg.popup("Nenhuma publicação encontrada com essa data!")
                                else:
                                    sg.popup("Por favor, insira uma data válida.")
                    

                    elif eventos8 == 'Palavras-chave':
                        window8.close()

                        layout9 = [
                            [sg.Text('Deseja ordenar por data de publicação ou por título?',
                                font=("Cooper Hewitt", 12), background_color=escuro,
                                text_color=claro)],
                            [sg.Radio("Data de publicação", "OPCAO", default=False, key="-OPC1-",
                                font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro),
                             sg.Radio("Título", "OPCAO", default=True, key="-OPC2-",
                                font=("Cooper Hewitt", 12), background_color=escuro, text_color=claro)],
                            [sg.Text('Palavras-chave:', font=("Cooper Hewitt", 15, "bold"), background_color=claro, text_color=escuro)],
                            [sg.InputText(key='-CON-', size=(58, 0), font=("Cooper Hewitt", 12))],
                            [sg.Button('Procurar', size=(10, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                             sg.Button('Voltar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                        ]

                        window9 = sg.Window(title="Consultar Publicação por palavras-chave", layout=layout9, background_color=claro)

                        stop9 = False
                        while not stop9:
                            eventos9, valores9 = window9.read()
                            if eventos9 in [sg.WIN_CLOSED, 'Voltar']:
                                stop9 = True
                                window9.close()
                                # Reabrir a janela principal de consulta
                                layout8 = [
                                    [sg.Text('Deseja consultar a publicação por:', size=(45, 1), expand_x=True,
                                        font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                    [sg.Button('Título', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Autor', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Afiliação', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Data de Publicação', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Palavras-chave', size=(20, 1), button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                                     sg.Button('Retornar ao Menu', size=(20, 1), font=("Cooper Hewitt", 12), button_color=(claro, tijolo))],
                                ]
                                window8 = sg.Window(title="Consultar Publicação", resizable=False, background_color=claro).Layout(layout8)

                            elif eventos9 == 'Procurar':
                                palavra_consulta = valores9['-CON-']
                                if palavra_consulta:
                                # Filtrar publicações
                                    resultados = filterpalavrachave(nome, palavra_consulta)
                                    if resultados:
                                        info_resultados = ""
                                        for pub in resultados:
                                            palavra_info = "\n".join([f"    - {autor['name']} (Afilição: {autor.get('affiliation', 'N/A')})" for autor in pub.get('authors', [])])
                                            info_resultados += (
                                                f"Título: {pub.get('title', 'Título desconhecido')}\n"
                                                f"Resumo: {pub.get('abstract', 'Resumo não disponível')}\n"
                                                f"Palavras-chave: {pub.get('keywords', ['Nenhuma palavra-chave'])}\n"
                                                f"Autores:\n{palavra_info if palavra_info else '    Nenhum autor disponível'}\n"
                                                f"DOI: {pub.get('doi', 'DOI não disponível')}\n"
                                                f"PDF: {pub.get('pdf', 'PDF não disponível')}\n"
                                                f"Data de Publicação: {pub.get('publish_date', 'Data desconhecida')}\n"
                                                f"URL: {pub.get('url', 'URL não disponível')}\n"
                                                f"{'-'*40}\n" 
                                            )
                                        layout_resultados = [
                                            [sg.Text("Resultados encontrados!", font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                            [sg.Multiline(info_resultados, size=(80, 20), font=("Cambria", 12), background_color=claro, text_color=escuro, disabled=True)],
                                            [sg.Button("Fechar", font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
                                        ]

                                        janela_resultados = sg.Window("Resultados da Consulta", layout_resultados, background_color=claro, resizable=True)

                                        
                                        while True:
                                            evento_resultados, _ = janela_resultados.read()
                                            if evento_resultados in [sg.WIN_CLOSED, "Fechar"]:
                                                break

                                        janela_resultados.close()
                                    else:
                                        sg.popup("Nenhuma publicação encontrada com essas palavras-chave!")
                                else:
                                    sg.popup("Por favor, insira palavras-chave válidas.")


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

            while True:
                evento, valores = window_exportar.read()

                if evento in [sg.WIN_CLOSED, "Cancelar"]:
                    window_exportar.close()
                    break

                if evento == '-TITULO-':
                    filtro_selecionado = 'title'
                    window_exportar["-RESULT-"].update("Você escolheu filtrar por Título.")
        
                elif evento == '-DATA-':
                    filtro_selecionado = 'publish_date'
                    window_exportar["-RESULT-"].update("Você escolheu filtrar por Data de Publicação.")
        
                elif evento == '-AUTOR-':
                    filtro_selecionado = 'authors'
                    window_exportar["-RESULT-"].update("Você escolheu filtrar por Autor.")
        
                elif evento == "Procurar":
                    valor_consulta = valores["-INPUT-"]
                    if filtro_selecionado and valor_consulta.strip():
                        dados_filtrados = filtrar_publicacoes(filtro_selecionado, valor_consulta, BD)
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
                            resultado = exportar_dados(nome_arquivo, dados_filtrados)
                            sg.popup(resultado,background_color=claro,text_color=escuro)
                        else:
                            sg.popup("Nome de arquivo inválido.",background_color=claro,text_color=escuro)
                    else:
                        sg.popup("Nenhuma publicação para exportar.",background_color=claro,text_color=escuro)

                    window.close()

        elif eventos == 'Help':
                     
            coluna = [

                [sg.Text("Sistema de Consulta e Análise de Publicações científicas", font=("Cambria", 24, "bold"), justification="center", background_color=claro, text_color=escuro)],
                [sg.Text("Bem-vindo à aplicação Task Master! Aqui serás capaz de organizar e manusear todas as tuas tarefas! Vamos explicar-te todas as funções que esta aplicação te traz!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nCarregar BD", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Nesta opção terás de carregar uma base de dados com todas as tarefas que tenhas para depois podermos usá-la no resto das opções!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nGravar BD", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Utiliza esta opção para gravar a base de dados que carregaste. Isso é especialmente útil após efetuares alterações nas tarefas.", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nAcrescentar dataset", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Adiciona mais bases de dados àquelas que já introduziste na aplicação. Desta forma, podes expandir o teu conjunto de dados!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nInserir nova tarefa", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Aqui, podes adicionar novas tarefas facilmente. Elas serão automaticamente integradas no dataset.", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nConsultar tarefa", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Efetua consultas específicas às tuas tarefas, utilizando critérios como prioridade, categoria, estado, data de vencimento e título!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nListagem", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Visualiza e lista todas as tarefas com base em parâmetros específicos.", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nAlterar tarefa", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Realiza todas as alterações necessárias nas tuas tarefas nesta opção!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nEliminar tarefa", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Elimina as tarefas que precisas de remover com facilidade.", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nRelatórios", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Explora um dashboard estatístico que apresenta gráficos que mostram o progresso das tuas tarefas.", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nContagem", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Conta o número total de tarefas ou o número delas com base em prioridade, categoria ou estado.", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nSair", font=("Cambria", 16, "bold"), background_color=claro, text_color=escuro)],
                [sg.Text("Fecha a aplicação. Não te esqueças de gravar o dataset após fazer alterações!", font=("Cambria", 14), background_color=claro, text_color=escuro)],
                [sg.Text("\nObrigada por utilizares o Task Master!", font=("Cambria", 16), background_color=claro, text_color=escuro)]
            ]

            layout_help = [[sg.Column(coluna, scrollable=True, vertical_scroll_only=True, size=(1300, 600), background_color=claro)]]


            window_help = sg.Window("Ajuda", layout_help, resizable=True, background_color=claro)  
            

            stop_help = False

            while not stop_help:
                eventos_help, valores_help = window_help.read()

                if eventos_help == sg.WINDOW_CLOSED:
                    stop_help = True
                    window_help.close()




      
# Executar a interface gráfica
interface_grafica()