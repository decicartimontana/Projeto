import FreeSimpleGUI as sg

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

#eliminar#
def apagarpublicacao(publicacoes, parametro, valor_procurado):
    # Verifica se a lista está vazia
    if not publicacoes:
        print("Nenhuma publicação disponível para apagar.")
        return False

    # Procura a publicação com base no parâmetro fornecido
    for publicacao in publicacoes[:]:  # Itera sobre uma cópia para evitar problemas ao remover
        if publicacao.get(parametro) == valor_procurado:
            print("Publicação encontrada:")
            print(publicacao)
            
            confirmacao = input("Confirma ser esta a publicação que pretende apagar? (s/n): ").strip().lower()
            
            # Repetir até que a entrada seja válida
            while confirmacao not in ('s', 'n'):
                print("Entrada inválida. Por favor, digite 's' para sim ou 'n' para não.")
                confirmacao = input("Confirma ser esta a publicação que pretende apagar? (s/n): ").strip().lower()

            if confirmacao == 's':
                publicacoes.remove(publicacao)
                print("Publicação removida com sucesso!")
                return True
            else:
                print("Operação cancelada pelo usuário.")
                return False

    print("Publicação não encontrada!")
    return False

#Atualizar

def AtualizarPublicacoes(publicacoes, titulo, novos_dados):
    # Busca a publicação pelo título
    atualizado = False
    for publicacao in publicacoes:
        if publicacao['title'] == titulo:
            # Atualiza os campos fornecidos em novos_dados
            if 'publish_date' in novos_dados:
                publicacao['publish_date'] = novos_dados['publish_date']
            if 'abstract' in novos_dados:
                publicacao['abstract'] = novos_dados['abstract']
            if 'keywords' in novos_dados:
                publicacao['keywords'] = novos_dados['keywords']
            if 'authors' in novos_dados:
                publicacao['authors'] = novos_dados['authors']
            if 'doi' in novos_dados:
                publicacao['doi'] = novos_dados['doi']
            if 'pdf' in novos_dados:
                publicacao['pdf'] = novos_dados['pdf']
            if 'url' in novos_dados:
                publicacao['url'] = novos_dados['url']
            atualizado = True
    if not atualizado:
        print(f"Publicação com título '{titulo}' não encontrada.")
    return publicacoes

def novos_dados():
    print('Introduza os novos dados.') 
    resumo = input('Resumo: ')
    palavras_chave = input('Palavras-chave (separadas por vírgula): ').split(',')
    autores_afiliacoes = [] 
    n = int(input('Quantos autores estão associados? '))
    for i in range(n):
        autor = input(f'Nome do autor {i+1}: ')
        afiliacao = input(f'Afiliação de {autor}: ')
        autores_afiliacoes.append({'name': autor, 'affiliation': afiliacao})
    data_publicacao = input('Data de publicação (AAAA-MM-DD): ')
    
    # Criação do dicionário final para atualização
    dados = {
        'publish_date': data_publicacao,
        'abstract': resumo,
        'keywords': [kw.strip() for kw in palavras_chave],
        'authors': autores_afiliacoes,
        'doi': input('DOI: '),
        'pdf': input('PDF: '),
        'url': input('URL: ')
    }
    return dados



#Afiliação
def filterafiliation(fnome, afiliação):
    d = []
    for pub in fnome:
        for a in pub['authors']:
            if a.get("affiliation") == afiliação:
                d.append(pub)
    return d

#Autor
def filterauthor(fnome, autor):
    d = []
    for pub in fnome:
        for a in pub['authors']:
            if a.get('name') == autor:
                d.append(pub)
    return d
#Título
def filtertitle(fnome, titulo):
    # Lista para armazenar os resultados
    resultados = []
    # Converte o título buscado para minúsculas (case-insensitive)
    titulo = titulo.lower()
    for pub in fnome:
        # Busca parcial e case-insensitive no campo 'title'
        if titulo in pub.get('title', '').lower():
            resultados.append(pub)
    return resultados

#data de publicação
def filterdata(fnome, data):
    """
    Filtra publicações por data de publicação, ignorando a hora.
    :param fnome: Lista de dicionários contendo as publicações.
    :param data: Data fornecida pelo usuário (formato 'YYYY-MM-DD').
    :return: Lista de publicações correspondentes.
    """
    d = []
    # Remove espaços em branco e horas da data fornecida pelo usuário
    data = data.strip().split()[0]

    for pub in fnome:
        # Obtém a data da publicação, se existir
        pub_date = pub.get("publish_date", "").strip()
        
        # Garante que a data não está vazia antes de fazer o split
        if pub_date:
            pub_date = pub_date.split()[0]
            
            # Compara as datas no formato 'YYYY-MM-DD'
            if pub_date == data:
                d.append(pub)

    return d



#palavras-chave
def filterpalavrachave(fnome, palavraschave):
    d = []
    for pub in fnome:
            palavras = pub.get("keywords")  
            if palavras:
                listapal = palavras.split(",")
                for pal in listapal:
                    if pal.strip().lower() == palavraschave.lower():  
                        d.append(pub)
    return d

#------Listar anos-------#
def listanos(fnome):
    a = []
    for pub in fnome:
        data = pub.get('publish_date')
        if data:
            ano = data.split("-")[0]  
            if ano not in a: 
                a.append(ano) 
    return sorted(a)
#----- Armazenamento de Dados -----#

def guardar_dataset(nome,dataset):
    ficheiro = open(nome,'w',encoding='utf-8')
    json.dump(dataset,ficheiro,ensure_ascii=False,indent=2)
    ficheiro.close()

##Pesquisa de publicações por título
def filtertitle(fnome, titulo):
    d = []
    titulo = titulo.strip().lower()  # Normaliza o título inserido
    for pub in fnome:
        if pub.get('title', '').strip().lower() == titulo:  # Normaliza o título na base de dados
            d.append(pub)
    return d

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
    window = sg.Window("Sistema de Consulta e Análise de Publicações Científicas", layout,resizable=True,
                       background_color=claro)

    stop = False

    while stop == False:

        eventos, valores = window.read() #ONDE ESTÁ A VALORIÁVEL VALORES????
        
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

        elif eventos == "-ESTATISTICAS-":  
            if BD== None:
                window["-DADOS-"].update("Primeiro carregue a base de dados!")
            else:
                window["-DADOS-"].update("A produzir dados estatísticos...")
                formLayout = [ 
                    [sg.Text('Gráfico que apresenta distribuição por:', font=("Cambria", 12), background_color=claro, text_color=escuro, pad=(0, 10))],
                    [sg.Column([
                        [sg.Button("ano", font=("Cambria", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("mês de um determinado ano", font=("Cambria", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("número de publicações por autor(top20)", font=("Cambria", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("publicações de um autor por ano", font=("Cambria", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("palavras-chave pela frequência(top20)", font=("Cambria", 12), pad=(0, 5), button_color=(claro, escuro))],
                        [sg.Button("palavras-chave mais frequentes por ano", font=("Cambria", 12), pad=(0, 5), button_color=(claro, escuro))]
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
                            pubano(BD)
                        elif inputEvent == "mês de um determinado ano":
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
                                        mesano(BD,ano)  # Certifique-se de que a função mesano está corretamente definida
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
                                        palavrafreqano(BD,ano)   # Certifique-se de que a função mesano está corretamente definida
                                        continuar = False  # Sai do ciclo após o processamento
                                    else:
                                        sg.popup("Por favor, selecione um ano.", title="Erro", background_color=claro, text_color=escuro)
                            window_por_ano.close()  
                        window["-DADOS-"].update("Dados estatísticos calculados com sucesso!")
        elif eventos == "-ATUALIZAR-":
            window["-DADOS-"].update("Preparar para atualizar...")
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

            window8 = sg.Window(title="Atualizar Publicação", resizable=True, background_color=claro).Layout(layout8)

            continue_reading = True
            while continue_reading:
                event, values = window8.read()
                if event in (sg.WINDOW_CLOSED, 'Retornar ao Menu'):
                    continue_reading = False  # Sai do loop principal
                    window8.close()
                elif event == "Título":
                    # Layout do formulário para inserção do título
                    formLayout = [
                        [sg.Text('Título:', size=(15, 1), font=("Baskerville", 12), justification="left", background_color=claro, text_color=escuro),
                        sg.InputText(key='-TITULO-', size=(45, 1))],
                        [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                        sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                    ]

                    # Janela para consultar por título
                    wform = sg.Window('Digite o título', formLayout, size=(600, 150), modal=True, background_color=claro)
                    reading_form = True

                    while reading_form:
                        event_form, values_form = wform.read()

                        if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                            reading_form = False  # Sai do loop do formulário
                            wform.close()

                        elif event_form == 'Consultar':
                            titulo = values_form.get('-TITULO-')
                            resultados = filtertitle(BD, titulo)  # Função externa para filtrar os dados
                            if resultados:
                                    # Layout da janela de resultados
                                    layout_resultados = [
                                        [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                        [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),sg.Button('Alterar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                    ]
                                        

                                    # Janela para exibir resultados
                                    janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                    janela_aberta = True

                                    while janela_aberta:
                                        evento_resultados, valores_resultados = janela_resultados.read()
                                        if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                            janela_aberta = False  # Sai do loop de resultados
                                            janela_resultados.close()
                            else:
                                    sg.popup("Nenhum resultado encontrado.", title="Informação", background_color=claro, text_color=escuro)
                        else:
                                sg.popup("Por favor, insira o título.", title="Erro", background_color=claro, text_color=escuro)
                elif event == "Autor":
                    # Layout do formulário para inserção do título
                    formLayout = [
                        [sg.Text('Autor:', size=(15, 1), font=("Baskerville", 12), justification="left", background_color=claro, text_color=escuro),
                        sg.InputText(key='-AUTOR-', size=(45, 1))],
                        [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                        sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                    ]

                    # Janela para consultar por título
                    wform = sg.Window('Digite o autor', formLayout, size=(600, 150), modal=True, background_color=claro)
                    reading_form = True

                    while reading_form:
                        event_form, values_form = wform.read()

                        if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                            reading_form = False  # Sai do loop do formulário
                            wform.close()

                        elif event_form == 'Consultar':
                            autor = values_form.get('-AUTOR-')
       
                            if autor != '':
                                # Filtra os dados pelo título
                                resultados = filterauthor(BD, autor)  # Função externa para filtrar os dados
                        
                                if resultados:
                                    # Layout da janela de resultados
                                    layout_resultados = [
                                        [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                        [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),sg.Button('Alterar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                    ]

                                    # Janela para exibir resultados
                                    janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                    janela_aberta = True

                                    while janela_aberta:
                                        evento_resultados, valores_resultados = janela_resultados.read()
                                        if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                            janela_aberta = False  # Sai do loop de resultados
                                            janela_resultados.close()
                                else:
                                    sg.popup("Nenhum resultado encontrado.", title="Informação", background_color=claro, text_color=escuro)
                            else:
                                sg.popup("Por favor, insira o título.", title="Erro", background_color=claro, text_color=escuro)
                elif event == "Afiliação":
                    # Layout do formulário para inserção do título
                    formLayout = [
                        [sg.Text('Afiliação:', size=(15, 1), font=("Baskerville", 12), justification="left", background_color=claro, text_color=escuro),
                        sg.InputText(key='-AFILIACAO-', size=(45, 1))],
                        [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                        sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                    ]

                    # Janela para consultar por título
                    wform = sg.Window('Digite a afiliação', formLayout, size=(600, 150), modal=True, background_color=claro)
                    reading_form = True

                    while reading_form:
                        event_form, values_form = wform.read()

                        if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                            reading_form = False  # Sai do loop do formulário
                            wform.close()

                        elif event_form == 'Consultar':
                            afiliacao = values_form.get('-AFILIACAO-')
                            print(f"afiliação inserido: {afiliacao}")  # Adicione esta linha para verificar o valor de titulos
                            if afiliacao!= '':
                                # Filtra os dados pelo título
                                resultados = filterafiliation(BD, afiliacao)  # Função externa para filtrar os dados
                                print(f"Resultados encontrados: {resultados}")  # Adicione esta linha para verificar os resultados
                                if resultados:
                                    # Layout da janela de resultados
                                    layout_resultados = [
                                        [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                        [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),sg.Button('Alterar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                    ]

                                    # Janela para exibir resultados
                                    janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                    janela_aberta = True

                                    while janela_aberta:
                                        evento_resultados, valores_resultados = janela_resultados.read()
                                        if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                            janela_aberta = False  # Sai do loop de resultados
                                            janela_resultados.close()
                                else:
                                    sg.popup("Nenhum resultado encontrado.", title="Informação", background_color=claro, text_color=escuro)
                            else:
                                sg.popup("Por favor, insira a afiliação.", title="Erro", background_color=claro, text_color=escuro)
                
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
                            reading_form = False  # Sai do loop do formulário
                            wform.close()

                        elif event_form == 'Consultar':
                            data = values_form.get('-DATA-')
                            if data:
                                resultados = filterdata(BD, data)  # Função externa para filtrar os dados
                                if resultados:
                                    # Layout da janela de resultados
                                    layout_resultados = [
                                        [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Listbox(values=resultados, size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                        [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),sg.Button('Alterar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                    ]

                                    # Janela para exibir resultados
                                    janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                    janela_aberta = True

                                    while janela_aberta:
                                        evento_resultados, valores_resultados = janela_resultados.read()
                                        if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                            janela_aberta = False  # Sai do loop de resultados
                                            janela_resultados.close()
                                # Filtra os dados pela data de publicação

                                else:
                                    sg.popup("Nenhum resultado encontrado.", title="Informação", background_color=claro, text_color=escuro)
                            else:
                                sg.popup("Por favor, insira a data.", title="Erro", background_color=claro, text_color=escuro)

                elif event == "Palavras-chave":
                    # Layout do formulário para inserção do título
                    formLayout = [
                        [sg.Text('Palavras-chave:', size=(15, 1), font=("Baskerville", 12), justification="left", background_color=claro, text_color=escuro),
                        sg.InputText(key='-PALAVRASCHAVE-', size=(45, 1))],
                        [sg.Button('Consultar', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                        sg.Button('Cancelar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12))]
                    ]

                    # Janela para consultar por título
                    wform = sg.Window('Digite as palavras-chave', formLayout, size=(600, 150), modal=True, background_color=claro)
                    reading_form = True

                    while reading_form:
                        event_form, values_form = wform.read()

                        if event_form in (sg.WINDOW_CLOSED, 'Cancelar'):
                            reading_form = False  # Sai do loop do formulário
                            wform.close()

                        elif event_form == 'Consultar':
                            palavraschave = values_form.get('-PALAVRASCHAVE-')
                            if palavraschave != '':
                                # Filtra os dados pelo título
                                resultados = filterpalavrachave(BD, palavraschave)  # Função externa para filtrar os dados
                                if resultados:
                                    # Layout da janela de resultados
                                    layout_resultados = [
                                        [sg.Text('Resultados encontrados:', font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                        [sg.Listbox(values=[res['title'] for res in resultados], size=(80, 10), key="-RESULTADOS-", horizontal_scroll=True)],
                                        [sg.Button('Fechar', button_color=(claro, tijolo), font=("Cooper Hewitt", 12)),
                                        sg.Button('Alterar', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                    ]

                                    # Janela para exibir resultados
                                    janela_resultados = sg.Window('Resultados', layout_resultados, modal=True, background_color=claro)
                                    janela_aberta = True

                                    while janela_aberta:
                                        evento_resultados, valores_resultados = janela_resultados.read()
                                        if evento_resultados in (sg.WINDOW_CLOSED, 'Fechar'):
                                            janela_aberta = False
                                            janela_resultados.close()
                                        elif evento_resultados == 'Alterar':
                                            titulo_selecionado = valores_resultados.get("-RESULTADOS-")
                                            if titulo_selecionado:
                                                titulo_selecionado = titulo_selecionado[0]  # Seleciona o primeiro título

                                                # Layout para recolher os novos dados (mantém o layout descrito anteriormente)
                                                autores = []
                                                formLayout3 = [
                                                    [sg.Column([
                                                        [sg.Text('*Título:', size=(10, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-title-')],
                                                        [sg.Text('*Resumo:', size=(10, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-abstract-')],
                                                        [sg.Text('*Palavras-chave:', size=(10, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-keywords-')],
                                                        [sg.Text('*Autores:', size=(10, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                                                        [sg.Text('*Nome:', size=(10, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-name-')],
                                                        [sg.Text('*Afiliação:', size=(10, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-affiliation-')],
                                                        [sg.Listbox(values=autores, size=(20, 10), key='-AUTORES-', pad=((0, 0), (15, 10)), enable_events=True), sg.Button('Adicionar Autor', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-ADICIONAR-')],
                                                        [sg.Text('*Data de publicação:', size=(10, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro), 
                                                        sg.CalendarButton('Escolha a data', target='-DATA-', key='calendario', format='%Y-%m-%d', button_color=(claro, escuro))],
                                                        [sg.InputText('', key='-DATA-', background_color=claro, text_color=escuro, pad=((480, 0), (0, 0)))],
                                                        [sg.Text('*doi:', size=(10, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-doi-')],
                                                        [sg.Text('*pdf:', size=(10, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-pdf-')],
                                                        [sg.Text('*url:', size=(10, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro), sg.InputText("", key='-url-')],
                                                        [sg.Text('* Indica um campo obrigatório', font=("Bid Shoulders Display", 12), background_color=claro, text_color=escuro, expand_x=True, enable_events=True)],
                                                        [sg.Button('Salvar', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-SALVAR-'), sg.Button('Cancelar', button_color=(claro, escuro), font=("Cooper Hewitt", 12), key='-CANCELAR-')]
                                                    ], size=(800, 600), background_color=claro)]
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
                                                            autores.append(f"{nome} : {afiliacao}")
                                                            wform3["-AUTORES-"].update(autores)
                                                            wform3["-name-"].update("")
                                                            wform3["-affiliation-"].update("")
                                                        else:
                                                            janelaErro("Preencha o nome e a afiliação do autor!")

                                                    elif any(inputValues3[k] == '' for k in ['-title-', '-abstract-', '-keywords-', '-DATA-', '-doi-', '-pdf-', '-url-']) or not autores:
                                                        janelaErro('Preencha todos os campos obrigatórios (*)!')
                                                    else:
                                                        # Validação do formato da data manualmente
                                                        data = inputValues3['-DATA-'].strip()
                                                        partes = data.split('-')
                                                        if len(partes) == 3 and len(partes[0]) == 4 and len(partes[1]) == 2 and len(partes[2]) == 2:
                                                            ano, mes, dia = partes
                                                            if ano.isdigit() and mes.isdigit() and dia.isdigit():
                                                                if 1 <= int(mes) <= 12 and 1 <= int(dia) <= 31:
                                                                    data_formatada = data  # Data válida
                                                                else:
                                                                    janelaErro("Data inválida! O mês deve estar entre 01 e 12, e o dia entre 01 e 31.")
                                                                    continue
                                                            else:
                                                                janelaErro("Data inválida! Certifique-se de que contém apenas números.")
                                                                continue
                                                        else:
                                                            janelaErro("Data inválida! Use o formato AAAA-MM-DD.")
                                                            continue

                                                        # Atualização do banco de dados
                                                        novatarefa = { 
                                                            'abstract': inputValues3['-abstract-'],
                                                            'keywords': inputValues3['-keywords-'],
                                                            'authors': autores,
                                                            'doi': inputValues3['-doi-'], 
                                                            'pdf': inputValues3['-pdf-'], 
                                                            'publish_date': data_formatada,
                                                            'title': inputValues3['-title-'], 
                                                            'url': inputValues3['-url-'],
                                                        }

                                                        publicacoes = AtualizarPublicacoes(publicacoes, titulo_selecionado, novatarefa)
                                                        sg.popup('Publicação alterada com sucesso!', title='Sucesso', background_color=claro)
                                                        stopform3 = True

                                                wform3.close()



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
                    continue_reading = False  # Sai do loop principal

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
                                resultados = filtertitle(BD, titulo)  # Função externa para filtrar os dados
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
                                        resultados = filterauthor(BD, autor)  # Função externa para filtrar os dados
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
                                        resultados = filterafiliation(BD, afiliacao)  # Função externa para filtrar os dados
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
                                resultados = filterdata(BD, data)  # Função externa para filtrar os dados
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
                                        resultados = filterpalavrachave(BD, palavraschave)  # Função externa para filtrar os dados
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
# Executar a interface gráfica
interface_grafica()
