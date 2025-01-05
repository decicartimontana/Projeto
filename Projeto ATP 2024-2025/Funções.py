import json
import matplotlib.pyplot as plt
import FreeSimpleGUI as sg


#----- Carregar BD -----
def carregar_dataset(fnome):
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    if bd == "":
        print("Nenhum ficheiro foi especificado.")
    else:
        print(f"Dados carregados com sucesso. Foram lidas um total de {len(bd)} publicações.")
    return bd 

#----- Armazenamento de Dados -----
def guardar_dataset(nome,dataset):
    ficheiro = open(nome,'w',encoding='utf-8')
    json.dump(dataset,ficheiro,ensure_ascii=False,indent=2)
    ficheiro.close()

#----- Consultar Publicação -----
def filtertitle(bd, titulo):
    d = []
    titulo = titulo.lower()
    for pub in bd:
        if titulo in pub.get('title', '').lower():
            d.append(pub)
    return d

def filterauthor(bd, autor):
    d = []
    autor = autor.lower()
    for pub in bd:
        autores_adicionados = False
        authors = pub.get('authors', [])  
        for a in authors:
            name = a.get('name', '').lower()  
            if autor in name and not autores_adicionados:
                d.append(pub)
                autores_adicionados = True  
    return d

def filterafiliation(bd, afiliação):
    d = []
    afiliação= afiliação.lower()
    for pub in bd:
        autores_adicionados = False
        authors = pub.get('authors', [])  
        for a in authors:
            afiliaçãos = a.get('affiliation', '').lower()  
            if afiliação in afiliaçãos and not autores_adicionados:
                d.append(pub)
                autores_adicionados = True  
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

#Ordenar publicações encontradas pelos títulos 
def ordenatitle(d):
    return sorted(d, key = lambda x:x.get('title'))

#Ordenar publicações encontradas pela data de publicação
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
    autor = autor.lower()
    for pub in bd:
        autores_adicionados = False
        authors = pub.get('authors', [])  
        for a in authors:
            name = a.get('name', '').lower()  
            if autor in name and not autores_adicionados:
                d.append(pub)
                autores_adicionados = True 
    return ordenatitle(d)

def filterauthor_ordenadodate(bd, autor):
    d = []
    autor = autor.lower()
    for pub in bd:
        autores_adicionados = False
        authors = pub.get('authors', [])  
        for a in authors:
            name = a.get('name', '').lower()  
            if autor in name and not autores_adicionados:
                d.append(pub)
                autores_adicionados = True 
    return ordenadate(d)

def filterafiliation_ordenadotitle(fnome, afiliação):
    d = []
    for pub in fnome:
        for a in pub['authors']:
            if a.get("affiliation",'') == afiliação:
                d.append(pub)
    return ordenatitle(d)

def filterafiliation_ordenadodate(fnome, afiliação):
    d = []
    for pub in fnome:
        for a in pub['authors']:
            if a.get("affiliation",'') == afiliação:
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

#----- Analisar publicações -----
def listAuthors(BD):
    autores = []
    for pub in BD:
        for autor in pub['authors']:
            if autor["name"] not in autores:
                autores.append(autor["name"].strip(".").strip(" "))
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

        # Verifica para filtro de autores
        if filtro == 'name':
            autores = pub.get('authors') or []
            for autor in autores:  # Itera sobre os autores
                nome = autor.get('name') or ""
                if valor.lower() in nome.lower() and pub not in dados_filtrados:
                    dados_filtrados.append(pub)

        elif filtro == 'affiliation':
            autores = pub.get('authors') or []
            for autor in autores:  # Itera sobre os autores
                afiliacao = autor.get('affiliation') or ""
                if valor.lower() in afiliacao.lower() and pub not in dados_filtrados:
                    dados_filtrados.append(pub)

        # Verifica para outros campos
        elif campo and valor.lower() in str(campo).lower():
            if pub not in dados_filtrados:
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
def pubano(BD):
    valores = list(distribpubporano(BD).values())
    labels = list(distribpubporano(BD).keys())

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

def distribpalavra20(bd):
    d = {}
    for pub in bd:
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

def distribpalavra(bd):
    d = {}
    for pub in bd:
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
        di = dict(ordena)
    return list(di.keys())

import matplotlib.pyplot as plt

def palavrafreq(fnome):
    valores = list(distribpalavra20(fnome).values())
    labels = list(distribpalavra20(fnome).keys())

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

#Atualizar

def AtualizarPublicacoes(publicacoes, titulo, novos_dados):
    atualizado = False
    for publicacao in publicacoes:
        if publicacao['title'] == titulo:
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

def alterarDetalhesPub(novo_titulo,novo_resumo,novas_palavras,novos_autores,nova_data,novo_doi, novo_pdf,novo_url, BD):
    
    for pub in BD:
            pub['title'] = novo_titulo
            pub['abastract'] = novo_resumo
            pub['keywords'] = novas_palavras
            pub['authors'] = novos_autores
            pub['publish_date'] = nova_data
            pub['doi'] = novo_doi
            pub['pdf'] = novo_pdf
            pub['url'] = novo_url


            return True  

    return False 


