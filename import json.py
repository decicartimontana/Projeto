# Interface de linha de comando

#----- Função Menu -----#

def menu():
    print("""Menu:
          1) Carregar Base de Dados
          2) Criar Publicação
          3) Atualizar Publicação
          4) Remover Publicação
          5) Consultar Publicação
          6) Análise de Publicações
          7) Estatística de Publicações
          8) Armazenamento de Dados
          9) Importação de Dados
          10) Exportação Parcial de Dados
          0) Sair""")
    
#print(menu())

#----- Função Carregar Base de Dados -----#

import json
def carregar_dataset(fnome):
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    if bd == "":
        print("Nenhum ficheiro foi especificado.")
    else:
        print(f"Dados carregados com sucesso. Foram lidas um total de {len(bd)} publicações.")
    return bd 

fnome = input("introduz o nome do ficheiro json:")
publicações = carregar_dataset(fnome)
print(publicações)


#----- Criar Publicação -----#

def criarpublicacao(titulo, resumo, palavraschave, doi, autoresafiliacoes, urlpdf, datapublicacao,pdf):
    publicacao = {
        'title': titulo,
        'abstract': resumo,
        'keywords': palavraschave,
        'doi': doi,
        'authors': autoresafiliacoes,
        'url': urlpdf,
        'publish_date': datapublicacao,
        'pdf' : pdf
    }
    return publicacao

def coletardadospublicacao():
    print('Vamos criar uma publicação! Introduza os dados, respeitando as indicações')
    titulo = input('Título: ')
    resumo = input('Resumo: ')
    palavraschave = input('Palavras-chave (separadas por vírgula): ')
    doi = input('DOI: ')
    autoresafiliacoes = [] 
    i=0
    n=int(input('Quantos autores estão associados?'))
    while i<n:
        autor = input('Nome do autor: ')
        afiliacao = input(f'Afiliação de {autor}: ')
        autores = {'name': autor, 'affiliation': afiliacao}
        autoresafiliacoes.append(autores)
        i=i+1
    urlpdf = input('URL do PDF: ')
    datapublicacao = input('Data de publicação (AAAA-MM-DD):')
    pdf = input("pdf:")
    
    publicacao = criarpublicacao(
        titulo=titulo,
        resumo=resumo,
        palavraschave=palavraschave,
        doi=doi,
        autoresafiliacoes=autoresafiliacoes,
        urlpdf=urlpdf,
        datapublicacao=datapublicacao,
        pdf = pdf
    )
    
    return publicacao

publicacaocriada = coletardadospublicacao()
print(publicacaocriada)
print("\nPublicação criada com sucesso!")


#----- Atualizar Publicação -----#

def AtualizarPublicacoes(publicacoes, titulo, novos_dados):
    # Busca a publicação pelo título
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
            return publicacoes
    # Caso o título não seja encontrado
        else: 
            print(f"Publicação com título '{titulo}' não encontrada.")

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
        'authors': autores_afiliacoes
    }
    return dados




#----- Apagar Publicação -----# 

def apagarpublicacao(publicacao, titulo, resumo, palavraschave, doi, autoresafiliacoes, urlpdf, datapublicacao):
    apagar=input('Indique o parâmetro pelo qual pretende aceder ao documento.')
    if apagar=='titulo':
        procurar=input('Título:')
        for palavra in publicacao:
            if procurar in 'Titulo':
                print(titulo)
                confirmacao=input('Confirma ser este a publicação que pretende apagar?')
                if confirmacao=='s':
                    publicacao.remove()
            else:
                print('Não encontrado!')
    elif apagar=='resumo':
        procurar=input('Resumo:')
        for palavra in publicacao:
            if procurar in 'resumo':
                print(resumo) 
                confirmacao=input('Confirma ser este a publicação que pretende apagar?')
                if confirmacao=='s':
                    publicacao.remove()
            else:
                print('Não encontrado!')
    elif apagar=='palavraschave':
        procurar=input('Palavras-chave:')
        for palavra in publicacao:
            if procurar in 'palavraschave':
                print(palavraschave) 
                confirmacao=input('Confirma ser este a publicação que pretende apagar?')
                if confirmacao=='s':
                    publicacao.remove()
            else:
                print('Não encontrado!')
    elif apagar=='doi':
        procurar=input('DOI:')
        for palavra in publicacao:
            if procurar in 'doi':
                print(doi) 
                confirmacao=input('Confirma ser este a publicação que pretende apagar?')
                if confirmacao=='s':
                    publicacao.remove()
            else:
                print('Não encontrado!')
    elif apagar=='autoresafiliacoes':
        procurar=input('Autor:')
        for palavra in publicacao:
            if procurar in 'autoresafiliacoes':
                print(autoresafiliacoes) 
                confirmacao=input('Confirma ser este a publicação que pretende apagar?')
                if confirmacao=='s':
                    publicacao.remove()
            else:
                print('Não encontrado!')
    elif apagar=='urlpdf':
        procurar=('URL do PDF:')
        for palavra in publicacao:
            if procurar in 'urlpdf':
                print(urlpdf) 
                confirmacao=input('Confirma ser este a publicação que pretende apagar?')
                if confirmacao=='s':
                    publicacao.remove()
            else:
                print('Não encontrado!')
    elif apagar=='datapublicacao':
        procurar=input('Data de publicação (AAAA-MM-DD): ')
        for palavra in publicacao:
            if procurar in 'datapublicacao':
                print(datapublicacao)
                confirmacao=input('Confirma ser este a publicação que pretende apagar?')
                if confirmacao=='s':
                    publicacao.remove()
            else:
                print('Não encontrado!')
    else:
        print('O parâmetro inserido não é válido.') 




#----- Consultar Publicação -----#

##Pesquisa de publicações por título
import json
def filtertitle(fnome, titulo):
    d = []
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
        if pub.get('title') == titulo:
            d.append(pub)
    return d

##Pesquisa de publicações por autor
import json
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
import json
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

#------ Análise de Publicações -----#

#----listar autores----#
import json
def listAuthors(fnome):
    autores = []
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
        authors = pub['authors']
        for autor in authors:
            if autor["name"] not in autores:
                a = autor['name'] 
                autores.append(a) 
    return sorted(autores)

print(listAuthors("ata_medica_papers.json"))

#----Frequencia-----#

import json
def topOrdena(par):
    return par[1]

def distribPub(fnome):
    d = {}
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
        for autor in pub['authors']:
            if autor['name'] not in d:
                d[autor['name']] = 1
            else:
                d[autor['name']] = d[autor['name']] + 1
        ordena = sorted(list(d.items()), key = topOrdena, reverse = True)
        di = dict(ordena)
    return di.keys() ##!!!!Atenção return dicionrário ou lista com os nomes ordenados 

print(distribPub("ata_medica_papers.json"))

#------ Publicações de autores ----#
import json
def articleporathor(fnome):
    d = {}
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
        for autor in pub['authors']:
            if autor['name'] not in d:
                d[autor['name']] = [pub]
            else:
                d[autor['name']].append(pub)
    lista = sorted(list(d.items()))
    return dict(lista)

##listar palavras chaves
import json
def listarpalavrachave(fnome):
    palavras_chaves = []
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
        palavras = pub.get("keywords")
        if palavras:
            listapal = palavras.split(",")
            for pal in listapal:
                if pal not in palavras_chaves:
                    palavras_chaves.append(pal.strip())
    return sorted(palavras_chaves)

listarpalavrachave("ata_medica_papers.json")

## Ordena palavras-chaves pelo seu número de ocorrência
import json
def topOrdena(par):
    return par[1]

def distribpalavra(fnome):
    d = {}
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
        palavras = pub.get("keywords")
        if palavras:
            listapal = palavras.split(",")
            for pal in listapal:
                pal = pal.strip()
                if pal not in d:
                    d[pal] = 1
                else:
                    d[pal] = d[pal] + 1
        ordena = sorted(list(d.items()), key = topOrdena, reverse = True)
        di = dict(ordena)
    return di.keys()

distribpalavra("ata_medica_papers.json")

##lista das publicações associadas a cada palavra-chave
import json
def articleporathor(fnome):
    d = {}
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
        palavras = pub.get("keywords")
        if palavras:
            listapal = palavras.split(",")
            for pal in listapal:
                pal = pal.strip()
                if pal not in d:
                    d[pal] = [pub]
                else:
                    d[pal].append(pub)
    lista = sorted(list(d.items()))
    return dict(lista)

articleporathor("ata_medica_papers.json")

##----- Estatística de Publicações -----#

##GRÁFICO : Distribuição de publicações por ano
import json
def topordena(par):
    return par[0]

def distribpubporano(fnome):
    d = {}
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
        data = pub.get('publish_date')
        if data:
            ano = data.split("-")[0]
            if ano not in d:
                d[ano] = 1
            else:
                d[ano] = d[ano] + 1
    lista = sorted(list(d.items()), key = topordena)
    return dict(lista)

distribpubporano("ata_medica_papers.json")

import matplotlib.pyplot as plt

valores = list(distribpubporano("ata_medica_papers.json").values())
labels = list(distribpubporano("ata_medica_papers.json").keys())

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

##GRÁFICO : Distribuição por mês de um determinado ano
def distribmesnoano(fnome, ano):
    d = {}
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    encontrado = False
    for pub in bd:
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
    

distribmesnoano("ata_medica_papers.json", "2014")


import matplotlib.pyplot as plt
ano = input("introduza o ano")
valores = list(distribmesnoano("ata_medica_papers.json", ano).values())
labels = list(distribmesnoano("ata_medica_papers.json", ano).keys())

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

##GRÁFICO : Número de publicações por autor (top 20 autores)

import json
def topOrdena(par):
    return par[1]

def distribautores(fnome):
    d = {}
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
        for autor in pub['authors']:
            if autor['name'] not in d:
                d[autor['name']] = 1
            else:
                d[autor['name']] = d[autor['name']] + 1
        ordena = sorted(list(d.items()), key = topOrdena, reverse = True)
        top20 = ordena[:20]
        di = dict(top20)   
    return di ##!!!!Atenção return dicionrário ou lista com os nomes ordenados 

print(distribautores("ata_medica_papers.json"))

import matplotlib.pyplot as plt

valores = list(distribautores("ata_medica_papers.json").values())
labels = list(distribautores("ata_medica_papers.json").keys())

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

##GRÁFICO : Distribuição de palavras-chave pela frequência (top20 palavras-chaves)
import json
def topOrdena(par):
    return par[1]

def distribpalavra(fnome):
    d = {}
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
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

distribpalavra("ata_medica_papers.json")

import matplotlib.pyplot as plt

valores = list(distribpalavra("ata_medica_papers.json").values())
labels = list(distribpalavra("ata_medica_papers.json").keys())

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

def distribpalavraporano(fnome, ano):
    d = {}
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    for pub in bd:
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

cores_nomeadas = list(mcolors.CSS4_COLORS.keys())
print(cores_nomeadas)
random.shuffle(cores_nomeadas)
ano = input("introduza o ano:")
x = list(distribpalavraporano("ata_medica_papers.json", ano).values())
labels = list(distribpalavraporano("ata_medica_papers.json", ano).keys())
cores_personalizadas = cores_nomeadas[:len(labels)]

plt.figure(figsize=(9, 9))
plt.pie(x, labels=labels, radius=50, autopct='%1.1f%%', shadow=True, colors=cores_personalizadas,
       wedgeprops={"linewidth": 1, "edgecolor": "white"})

plt.axis('equal')
plt.title(f'Distribuição de palavras-chave mais frequentes de {ano}')
plt.show()

#----- Armazenamento de Dados -----#

def guardar_dataset(ficheiro,dados):
    if dados is None:
        print("Não existem dados para guardar")
    else:
        with open(ficheiro, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=2, ensure_ascii=False)
            print("Dados aramzenados com sucesso.")

#----- Importação de Dados -----#

def importar_dados(ficheiro, dados_existentes):
    novo_dataset=carregar_dataset(ficheiro)
    if novo_dataset is None:
        print("Erro ao importar dados.")
        return dados_existentes
    elif novo_dataset and type(novo_dataset)==list:
        registos_validos= True
        for registo in novo_dataset:
            if type(registo)!=dict:
                registos_validos=False
        if registos_validos==True:
            for registo  in novo_dataset:
                dados_existentes.append(registo)
            print("Novos registos foram importados com sucesso")
        else:
            print("Erro o ficheiro que deseja importar não tem a estrutura esperada.")

#------ Exportação Parcial de Dados------#

def exportar_dados(ficheiro,dados_filtrados):
    if not dados_filtrados:
        return "Não há dados para exportar."
    else:
        with open(ficheiro,'w',encoding='utf-8') as arquivo:
            json.dump(dados_filtrados,arquivo,ident=2,ensure_ascii=False)
            print(f"Dados exportados com sucesso para {ficheiro}.")
