import json
import matplotlib.pyplot as plt
import FreeSimpleGUI as sg


#Carregar BD
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

#Consultar
def filtertitle(bd, titulo):
    resultados = []
    titulo = titulo.lower()
    for pub in bd:
        if titulo in pub.get('title', '').lower():
            resultados.append(pub)
    return resultados

def filterauthor(bd, autor):
    d = []
    for pub in bd:
        for a in pub['authors']:
            if a.get('name') == autor:
                d.append(pub)
    return d

def filterafiliation(fnome, afiliação):
    d = []
    for pub in fnome:
        for a in pub['authors']:
            if a.get("affiliation") == afiliação:
                d.append(pub)
    return d

def filterdata(bd, data):
    d = []
    data = data.strip().split()[0]
    for pub in bd:
        pub_date = pub.get("publish_date", "").strip()
        if pub_date:
            pub_date = pub_date.split()[0]
            if pub_date == data:
                d.append(pub)
    return d

def filterpalavrachave(bd, palavraschave):
    d = []
    for pub in bd:
            palavras = pub.get("keywords")  
            if palavras:
                listapal = palavras.split(",")
                for pal in listapal:
                    if pal.strip().lower() == palavraschave.lower():  
                        d.append(pub)
    return d

##Ordenar publicações encontradas pelos títulos 
def ordenatitle(d):
    return sorted(d, key = lambda x:x.get('title'))

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

def filtertitle_ordenadodate(bd, titulo):
    resultados = []
    titulo = titulo.lower()
    for pub in bd:
        if titulo in pub.get('title', '').lower():
            resultados.append(pub)
    return ordenadate(resultados)

def filtertitle_ordenadotitle(bd, titulo):
    resultados = []
    titulo = titulo.lower()
    for pub in bd:
        if titulo in pub.get('title', '').lower():
            resultados.append(pub)
    return ordenatitle(resultados)

def filterauthor_ordenadotitle(bd, autor):
    d = []
    for pub in bd:
        for a in pub['authors']:
            if a.get('name') == autor:
                d.append(pub)
    return ordenatitle(d)

def filterauthor_ordenadodate(bd, autor):
    d = []
    for pub in bd:
        for a in pub['authors']:
            if a.get('name') == autor:
                d.append(pub)
    return ordenadate(d)

def filterafiliation_ordenadotitle(fnome, afiliação):
    d = []
    for pub in fnome:
        for a in pub['authors']:
            if a.get("affiliation") == afiliação:
                d.append(pub)
    return ordenatitle(d)

def filterafiliation_ordenadodate(fnome, afiliação):
    d = []
    for pub in fnome:
        for a in pub['authors']:
            if a.get("affiliation") == afiliação:
                d.append(pub)
    return ordenadate(d)

def filterdata_ordenadotitle(bd, data):
    d = []
    data = data.strip().split()[0]
    for pub in bd:
        pub_date = pub.get("publish_date", "").strip()
        if pub_date:
            pub_date = pub_date.split()[0]
            if pub_date == data:
                d.append(pub)
    return ordenatitle(d)

def filterdata_ordenadodate(bd, data):
    d = []
    data = data.strip().split()[0]
    for pub in bd:
        pub_date = pub.get("publish_date", "").strip()
        if pub_date:
            pub_date = pub_date.split()[0]
            if pub_date == data:
                d.append(pub)
    return ordenadate(d)

def filterpalavrachave_ordenadodate(bd, palavraschave):
    d = []
    for pub in bd:
            palavras = pub.get("keywords")  
            if palavras:
                listapal = palavras.split(",")
                for pal in listapal:
                    if pal.strip().lower() == palavraschave.lower():  
                        d.append(pub)
    return ordenadate(d)

def filterpalavrachave_ordenadotitle(bd, palavraschave):
    d = []
    for pub in bd:
            palavras = pub.get("keywords")  
            if palavras:
                listapal = palavras.split(",")
                for pal in listapal:
                    if pal.strip().lower() == palavraschave.lower():  
                        d.append(pub)
    return ordenatitle(d)
#Analisar publicações
def listAuthors(BD):
    autores = []
    for pub in BD:
        for autor in pub['authors']:
            if autor["name"] not in autores:
                autores.append(autor["name"])
    return sorted(autores)

def distribPub(BD):
    d = {}
    for pub in BD:
        for autor in pub['authors']:
            if autor['name'] not in d:
                d[autor['name']] = 1
            else:
                d[autor['name']] += 1
    ordena = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in ordena]

def articleporathor(BD, autor):
    d = []
    for pub in BD:
        for autores in pub['authors']:
            if autores['name'] == autor:
                d.append(pub)
    return d

def articleporathor(BD, autor):
    d = []
    for pub in BD:
        for autores in pub['authors']:
            if autores['name'] == autor:
                d.append(pub)
    return d

##listar palavras chaves
import json
def listKeywords(BD):
    palavras_chaves = []
    for pub in BD:
        palavras = pub.get("keywords")
        if palavras:
            listapal = palavras.split(",")
            for pal in listapal:
                if pal not in palavras_chaves:
                    palavras_chaves.append(pal.strip().strip("."))
    return sorted(palavras_chaves)

import json
def topOrdena(par):
    return par[1]

def distribpalavra(BD):
    d = {}
    for pub in BD:
        palavras = pub.get("keywords")
        if palavras:
            listapal = palavras.split(",")
            for pal in listapal:
                pal = pal.strip().strip(".")
                if pal not in d:
                    d[pal] = 1
                else:
                    d[pal] = d[pal] + 1
        ordena = sorted(list(d.items()), key = topOrdena, reverse = True)
    return [pal[0] for pal in ordena]

def articleporpal(BD, palavra):
    d = []
    for pub in BD:
        palavras = pub.get("keywords")
        if palavras:
            listapal = palavras.split(",")
            for pal in listapal:
                pal = pal.strip().strip(".")
                if pal==palavra:
                    d.append(pub)
    return d

##Importação de dados
def importar_dados(ficheiro, dados_existentes):
    with open(ficheiro, encoding="utf-8") as f:
        novo_dataset = json.load(f)
    if isinstance(novo_dataset, list) and all(isinstance(registo, dict) for registo in novo_dataset):
        for registo in novo_dataset:
            if registo not in dados_existentes:
                dados_existentes.append(registo)
        print("Novos registos foram importados com sucesso")
    else:
        print("Erro: O ficheiro não possui a estrutura esperada.")
    
    return dados_existentes

def criarpublicacao(bd, nova_publicação):
    bd.append(nova_publicação)
    return bd

#---Filtrar pub-----
def filtrar_publicacoes(filtro, valor, BD):
    dados_filtrados = []
    for pub in BD:
        campo = pub.get(filtro)
        
        if filtro == 'authors':  
            if isinstance(campo, list):  
                
                autores_correspondentes = [
                    autor for autor in campo 
                    if isinstance(autor, dict) and valor.lower() in autor.get('name', '').lower()
                ]
                if autores_correspondentes:  
                    dados_filtrados.append(pub)
        
        elif isinstance(campo, str):  
            if valor.lower() in campo.lower():
                dados_filtrados.append(pub)
    
    return dados_filtrados

#------ Exportação Parcial de Dados------#

def exportar_dados(nome_arquivo, dados):

    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    return f"Dados exportados com sucesso para {nome_arquivo}."

##----- Estatística de Publicações -----#
##GRÁFICO1 : Distribuição de publicações de um autor por anos
def topOrdena(par):
    return par[0]

def distribpubdeautorporano(fnome, autor):
    d = {}
    for pub in fnome:
        for a in pub['authors']:
            if a['name'] == autor:
                data = pub.get('publish_date')
                if data:
                    ano = data.split("-")[0]
                    if ano not in d:
                        d[ano] = 1
                    else:
                        d[ano] = d[ano] + 1
        ordena = sorted(list(d.items()), key = topOrdena)
        di = dict(ordena)
    return di 

import matplotlib.pyplot as plt
def pubautorano(fnome,autor):
    valores = list(distribpubdeautorporano(fnome,autor).values())
    labels = list(distribpubdeautorporano(fnome,autor).keys())

    plt.figure(figsize=(5, 5))
    plt.bar(labels, valores, color = "gold")

    # Defina o título do gráfico
    plt.title(f'Distribuição de publicação por ano de {autor}')

    # Roteação dos rótulos do eixo x para torná-los mais legíveis
    plt.xticks(rotation=35, ha='right',fontsize=8)

    for i, v in enumerate(valores):
        plt.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

    # Exiba o gráfico de barras
    plt.tight_layout()
    plt.show()


##GRÁFICO2: Distribuição de publicações por ano
import json
def topordena(par):
    return par[0]

def distribpubporano(fnome):
    d = {}
    for pub in fnome:
        data = pub.get('publish_date')
        if data:
            ano = data.split("-")[0]
            if ano not in d:
                d[ano] = 1
            else:
                d[ano] = d[ano] + 1
    lista = sorted(list(d.items()), key = topordena)
    return dict(lista)

import matplotlib.pyplot as plt
def pubano(fnome):
    valores = list(distribpubporano(fnome).values())
    labels = list(distribpubporano(fnome).keys())

    plt.figure(figsize=(5, 5))
    plt.bar(labels, valores)

    # Defina o título do gráfico
    plt.title('Distribuição de publicações por ano')

    # Roteação dos rótulos do eixo x para torná-los mais legíveis
    plt.xticks(rotation=45, ha='right')

    for i, v in enumerate(valores):
        plt.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

    # Exiba o gráfico de barras
    plt.tight_layout()
    plt.show()

##GRÁFICO3 : Distribuição por mês de um determinado ano
def distribmesnoano(fnome, ano):
    d = {}
    encontrado = False
    for pub in fnome:
        data = pub.get('publish_date')
        if data:
            anos = data.split("-")[0]
            mes = data.split("-")[1]
            if anos == ano:
                encontrado = True
                if mes not in d:
                    d[mes] = 1
                else:
                    d[mes] = d[mes] + 1
    if encontrado == False:
        print(f"Em {ano} não houve publicações.")
    lista = sorted(list(d.items()), key = topordena)
    return dict(lista)

import matplotlib.pyplot as plt
def mesano(fnome, ano):
    valores = list(distribmesnoano(fnome, ano).values())
    labels = list(distribmesnoano(fnome, ano).keys())

    plt.figure(figsize=(5, 5))
    plt.bar(labels, valores, color = "darkseagreen")

    # Defina o título do gráfico
    plt.title(f'Distribuição de publicações por mês de {ano}')

    # Roteação dos rótulos do eixo x para torná-los mais legíveis
    #plt.xticks(rotation=45, ha='right')

    for i, v in enumerate(valores):
        plt.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

    # Exiba o gráfico de barras
    plt.tight_layout()
    plt.show()

##GRÁFICO4 : Número de publicações por autor (top 20 autores)

import json
def topOrdena(par):
    return par[1]

def distribautores(fnome):
    d = {}
    for pub in fnome:
        for autor in pub['authors']:
            if autor['name'] not in d:
                d[autor['name']] = 1
            else:
                d[autor['name']] = d[autor['name']] + 1
        ordena = sorted(list(d.items()), key = topOrdena, reverse = True)
        top20 = ordena[:20]
        di = dict(top20)   
    return di 

import matplotlib.pyplot as plt
def npubautor(fnome):
    valores = list(distribautores(fnome).values())
    labels = list(distribautores(fnome).keys())

    plt.figure(figsize=(5, 5))
    plt.bar(labels, valores, color = "orange")

    # Defina o título do gráfico
    plt.title('Distribuição de publicações por autor Top20')

    # Roteação dos rótulos do eixo x para torná-los mais legíveis
    plt.xticks(rotation=90, ha='right', fontsize=8)

    for i, v in enumerate(valores):
        plt.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

    # Exiba o gráfico de barras
    plt.tight_layout()
    plt.show()

##GRÁFICO5 : Distribuição de palavras-chave pela frequência (top20 palavras-chaves)
import json
def topOrdena(par):
    return par[1]

def distribpalavra(fnome):
    d = {}
    for pub in fnome:
        palavras = pub.get("keywords")
        if palavras:
            listapal = palavras.split(",")
            for pal in listapal:
                pal = pal.strip().strip(".")
                if pal not in d:
                    d[pal] = 1
                else:
                    d[pal] = d[pal] + 1
        ordena = sorted(list(d.items()), key = topOrdena, reverse = True)
        top20 = ordena[:20]
        di = dict(top20)
    return di

import matplotlib.pyplot as plt

def palavrafreq(fnome):
    valores = list(distribpalavra(fnome).values())
    labels = list(distribpalavra(fnome).keys())

    plt.figure(figsize=(5, 5))
    plt.bar(labels, valores, color = "gold")

    # Defina o título do gráfico
    plt.title('Distribuição de palavra-chaves pela frequência Top20')

    # Roteação dos rótulos do eixo x para torná-los mais legíveis
    plt.xticks(rotation=90, ha='right',fontsize=8)

    for i, v in enumerate(valores):
        plt.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

    # Exiba o gráfico de barras
    plt.tight_layout()
    plt.show()

    import json
    def topOrdena(par):
        return par[1]

#Gráfico Distribuição de palavras-chaves mais frequentes por ano

def topOrdena(par):
    return par[1]

def distribpalavraporano(fnome, ano):
    d = {}
    for pub in fnome:
        data = pub.get('publish_date')
        if data:
            a = data.split("-")[0]
            if a == ano:
                palavras = pub.get("keywords")
                if palavras:
                    listapal = palavras.split(",")
                    for pal in listapal:
                        pal = pal.strip().strip(".")
                        if pal not in d:
                            d[pal] = 1
                        else:
                            d[pal] = d[pal] + 1
    ordena = sorted(list(d.items()), key = topOrdena, reverse = True)
    top20 = ordena[:20]
    di = dict(top20)
    return di 

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random

def palavrafreqano(fnome, ano):
    cores_nomeadas = list(mcolors.CSS4_COLORS.keys())
    print(cores_nomeadas)
    random.shuffle(cores_nomeadas)
    x = list(distribpalavraporano(fnome, ano).values())
    labels = list(distribpalavraporano(fnome, ano).keys())
    cores_personalizadas = cores_nomeadas[:len(labels)]

    plt.figure(figsize=(9, 9))
    plt.pie(x, labels=labels, radius=50, autopct='%1.1f%%', shadow=True, colors=cores_personalizadas,
        wedgeprops={"linewidth": 1, "edgecolor": "white"})

    plt.axis('equal')
    plt.title(f'Distribuição de palavras-chave mais frequentes de {ano}')
    plt.show()

def listanos(fnome):
    a = []
    for pub in fnome:
        data = pub.get('publish_date')
        if data:
            ano = data.split("-")[0]  
            if ano not in a: 
                a.append(ano) 
    return sorted(a)

def consultar():
    if eventos == "-CONSULTAR-":
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