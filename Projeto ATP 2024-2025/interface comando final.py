import json
import re
import tkinter as tk
import os
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random

    

def interface_comando():
    def help():
        print("\nComandos disponíveis:")
        print("+------------------------------+------------------------------------------------+")
        print("|       Comando                |                 Descrição                      |")
        print("+------------------------------+------------------------------------------------+")
        print("|   1. Carregar Base de Dados  | Carregar uma base de dados                     |")
        print("|   2. Guardar Base de Dados   | Gravar a base de dados que carregada           |")
        print("|   3. Consultar Publicação    | Consulta Publicações na Base de Dados          |")
        print("|   4. Analisar Publicação     | Analisa Publicações conforme alguns critérios  |")
        print("|   5. Importar Dados          | Importa novos registos na Base de Dados        |")
        print("|   6. Exportação Parcial      | Exporta ficheiros da Base de Dados             |")
        print("|   7. Atualizar Publicações   | Alterar informações duma Publicação            |")
        print("|   8. Criar Publicação        | Cria uma nova Publicação                       |")
        print("|   9. Estatísticas            | Alguns dados Estatísticos sobre as Publicações |")
        print("|   10. Eliminar Publicação    | Elimina uma publicação                         |")
        print("|   11. Help                   | Imprime esta mensagem de ajuda                 |")
        print("|   12. Sair                   | Fecha a aplicação                              |")
        print("+------------------------------+------------------------------------------------+")

    #----- Carregar BD -----
    def carregar_dataset(fnome):
        if not fnome.strip():
            print("Nenhum ficheiro foi especificado.")
            return None
        
        if not os.path.isfile(fnome):
            print("Ficheiro não encontrado.")
            return None

        f = open(fnome, encoding="utf-8")
        bd = json.load(f)
        print(f"Dados carregados com sucesso. Foram lidas um total de {len(bd)} publicações.")
        return bd 
    
    #----- Armazenamento de Dados -----
    def guardar_dataset(nome,dataset):
        if dataset is not None:
            ficheiro = open(nome, 'w', encoding='utf-8')
            json.dump(dataset, ficheiro, ensure_ascii=False, indent=2)
            ficheiro.close()
            print(f"Base de dados salva com sucesso em {nome}")
        else:
            print("Carregue uma base de dados primeiro.")

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
        for pub in bd:
            for a in pub['authors']:
                if a.get('name') == autor:
                    d.append(pub)
        return d

    def filterafiliation(bd, afiliação):
        d = []
        for pub in bd:
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
    
    ##--------Consultar Publicação Função------##
    def consultar_pub(bd):
        print("\n===== Consultar Publicação =====")
        print("Escolha o método de consulta:")
        print("1. Consultar por Título.")
        print("2. Consultar por Autor.")
        print("3. Consultar por Afiliação.")
        print("4. Consultar por Data de Publicação.")
        print("5. Consultar por Palvras-chave.")
        
        escolha_metodo = input("Digite o número correspondente ao método de consulta desejado: ")

        if escolha_metodo == "1":
            print("\nSelecione como deseja ordenar:")
            print("1. Ordenar por Título.")
            print("2. Ordenar por Data.")
            resposta1=input("Digite o número correspondente ao método de ordenação que deseja.")
            if resposta1=="1":
                print("Título das publicações será o mesmo!")
                titulo = input("Digite o título da publicação para consulta: ")
                res=filtertitle_ordenadotitle(bd, titulo)
                if res:
                    print("\nPublicações encontradas:")
                    for pub in res:
                        print(pub)  
                else:
                    print("Nenhuma publicação encontrada com esse titulo especificado.")
            elif resposta1== "2":
                titulo = input("Digite o título da publicação para consulta: ")
                res=filtertitle_ordenadodate(bd, titulo)
                if res:
                    print("\nPublicações encontradas:")
                    for pub in res:
                        print(pub)  
                else:
                    print("Nenhuma publicação encontrada com esse titulo especificado.")
            else:
                print("Opção inválida.")
        elif escolha_metodo == "2":
            print("\nSelecione como deseja ordenar:")
            print("1. Ordenar por Título.")
            print("2. Ordenar por Data.")
            resposta2=input("Digite o número correspondente ao método de ordenação que deseja.")
            if resposta2=="1":
                autor=input("Digite o autor da publicação para consulta:")
                res=filterauthor_ordenadotitle(bd, autor)
                if res:
                    print("\nPublicações encontradas:")
                    for pub in res:
                        print(pub)  
                else:
                    print("Nenhuma publicação encontrada com o autor especificado.")
            elif resposta2=="2":
                autor=input("Digite o autor da publicação para consulta:")
                res=filterauthor_ordenadodate(bd, autor)
                if res:
                    print("\nPublicações encontradas:")
                    for pub in res:
                        print(pub)  
                else:
                    print("Nenhuma publicação encontrada com o autor especificado.")
            else:
                print("Opção Inválida.")
        elif escolha_metodo == "3":
            print("\nSelecione como deseja ordenar:")
            print("1. Ordenar por Título.")
            print("2. Ordenar por Data.")
            resposta3=input("Digite o número correspondente ao método de ordenação que deseja.")
            if resposta3=="1":
                afiliação=input("Digite a afiliação da publicação para consulta:")
                res=filterafiliation_ordenadotitle(bd, afiliação)
                if res:
                    print("\nPublicações encontradas:")
                    for pub in res:
                        print(pub)  
                else:
                    print("Nenhuma publicação encontrada com a afiliação especificada.")
            elif resposta3=="2":
                afiliação=input("Digite a afiliação da publicação para consulta:")
                res=filterafiliation_ordenadodate(bd, afiliação)
                if res:
                    print("\nPublicações encontradas:")
                    for pub in res:
                        print(pub)  
                else:
                    print("Nenhuma publicação encontrada com a afiliação especificada.")
            else:
                print("Opção Inválida.")
        elif escolha_metodo == "4":
            print("\nSelecione como deseja ordenar:")
            print("1. Ordenar por Título.")
            print("2. Ordenar por Data.")
            resposta4=input("Digite o número correspondente ao método de ordenação que deseja.")
            if resposta4=="1":
                data=input("Digite a data da publicação para consulta (no formato YYYY-MM-DD):")
                res=filterdata_ordenadotitle(bd, data)
                if res:
                    print("\nPublicações encontradas:")
                    for pub in res:
                        print(pub)  
                else:
                    print("Nenhuma publicação encontrada com a data especificada.")
            elif resposta4=="2":
                print("Data de publicação será a mesma!")
                data=input("Digite a data da publicação para consulta (no formato YYYY-MM-DD):")
                res=filterdata_ordenadodate(bd, data)
                if res:
                    print("\nPublicações encontradas:")
                    for pub in res:
                        print(pub)  
                else:
                    print("Nenhuma publicação encontrada com a data especificada.")
            else:
                print("Opção Inválida.")
        elif escolha_metodo == "5":
            print("\nSelecione como deseja ordenar:")
            print("1. Ordenar por Título.")
            print("2. Ordenar por Data.")
            resposta5=input("Digite o número correspondente ao método de ordenação que deseja.")
            if resposta5=="1":
                palavras_chave=input("Digite as palavras-chave da publicação para consulta: ")
                res=filterpalavrachave_ordenadotitle(bd, palavras_chave)
                if res:
                    print("\nPublicações encontradas:")
                    for pub in res:
                        print(pub)  
                else:
                    print("Nenhuma publicação encontrada com as palvras-chave especificadas.")
            elif resposta5=="2":
                palavras_chave=input("Digite as palavras-chave da publicação para consulta: ")
                res=filterpalavrachave_ordenadodate(bd, palavras_chave)
                if res:
                    print("\nPublicações encontradas:")
                    for pub in res:
                        print(pub)  
                else:
                    print("Nenhuma publicação encontrada com as palavras-chave especificadas.")
            else:
                print("Opção Inválida.")
        else:
            print("Opção Inválida.")





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
    
    ##-----Analisar Publicações-----########
    def AnalisarPub(bd):
        print("\n===== Analisar Publicação =====")
        print("Escolha o método de Análise:")
        print("1. Analisar por autor.")
        print("2. Analisar por palavras-chave.")

        escolha_metodo_analise = input("Digite o número correspondente ao método de análise desejado:")
        if escolha_metodo_analise=="1":
            print("\nSelecione como deseja ordenar:")
            print("1. Ordenar por frequência de artigos.")
            print("2. Ordenar por ordem alfabética.")
            resanalise=input("Digite o número correspondente ao método de ordenação que deseja.")
            if resanalise=="1":
                res=distribPub(bd)
                if res:
                    print("\nLista de Autores:")
                    print(res)
                    autor=input("Digite o autor da publicação para consulta:")
                    if autor:
                        p = articleporathor(bd, autor)
                        print(p)  
                    else:
                        print("Nenhuma publicação encontrada com o autor especificado.")
            elif resanalise=="2":
                res=listAuthors(bd)
                if res:
                    print("\nLista de Autores:")
                    print(res)
                    autor=input("Digite o autor da publicação para consulta:")
                    if autor:
                        p = articleporathor(bd, autor)
                        print(p) 
                    else:
                        print("Nenhuma publicação encontrada com o autor especificado.")
            else:
                print("Opção inválida.")
        elif escolha_metodo_analise=="2":
            print("\nSelecione como deseja ordenar:")
            print("1. Ordenar por frequência de artigos.")
            print("2. Ordenar por ordem alfabética.")
            resanalise2=input("Digite o número correspondente ao método de ordenação que deseja.")
            if resanalise2=="1":
                res=distribpalavra(bd)
                if res:
                    print("\nLista de palavras-chave:")
                    print(res)
                    palavraschave=input("Digite as palvras-chave para consulta:")
                    if palavraschave:
                        p = articleporpal(bd, palavraschave)
                        print(p) 
                    else:
                        print("Nenhuma publicação encontrada com o autor especificado.")

            elif resanalise2=="2":
                res=listKeywords(bd)
                if res:
                    print("\nLista de palavras-chave:")
                    print(res)
                    palavraschave=input("Digite as palvras-chave para consulta:")
                    if palavraschave:
                        p = articleporpal(bd, palavraschave)
                        print(p)  
                    else:
                        print("Nenhuma publicação encontrada com o autor especificado.")
            else:
                print("Opção Inválida.")
        else:
            print("Opção Inválida.")

    ##Importação de dados
    def importar_dados(ficheiro, dados_existentes):
        try:
            with open(ficheiro, encoding="utf-8") as f:
                novo_dataset = json.load(f)
            
            if isinstance(novo_dataset, list) and all(isinstance(registo, dict) for registo in novo_dataset):
                for registo in novo_dataset:
                    if registo not in dados_existentes:
                        dados_existentes.append(registo)  # Adiciona novos registos ao dataset
                print(f"{len(novo_dataset)} novos registos foram importados com sucesso.")
            else:
                print("Erro: O ficheiro não possui a estrutura esperada.")
        
        except Exception as e:
            print(f"Erro ao importar dados: {e}")
            
        return dados_existentes
    
    #------ Exportação Parcial de Dados------#

    def exportar_dados(nome_arquivo, dados):
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        return f"Dados exportados com sucesso para {nome_arquivo}."

    def exportar_publicacao(dataset):
        consultar_pub(dataset)  
        
        resposta = input("Deseja exportar esta publicação? (s/n): ").strip().lower()
        
        if resposta == 's':
            nome_arquivo = input("Digite o nome do arquivo (incluindo a extensão, ex: 'publicacao.json'): ").strip()
            
            if nome_arquivo:
                resultado = exportar_dados(nome_arquivo, dataset) 
                print(f"Publicação exportada com sucesso para {nome_arquivo}")
            else:
                print("Nome de arquivo inválido. A exportação não foi realizada.")
        else:
            print("A exportação da publicação foi cancelada.")

    #-----Atualizar Publicações------##
    def alterar_informacoes(dataset):
        """
        Permite alterar informações de uma publicação com base em um critério.
        """
        criterio = input("Indique o parâmetro pelo qual pretende buscar o documento (title, abstract, keywords, doi, authors, url, pdf, publish_date): ").strip().lower()

        if criterio not in ['title', 'abstract', 'keywords', 'doi', 'authors', 'url', 'pdf', 'publish_date']:
            print("O parâmetro inserido não é válido.")
            return

        valor = input(f"Informe o valor do parâmetro '{criterio}': ").strip().lower()
        if not valor:
            print("Valor inválido. Operação cancelada.")
            return

        publicacoes_encontradas = []
        for publicacao in dataset:
            if criterio == 'title' and valor in publicacao.get('title', '').strip().lower():
                publicacoes_encontradas.append(publicacao)
            elif criterio == 'abstract' and valor in publicacao.get('abstract', '').strip().lower():
                publicacoes_encontradas.append(publicacao)
            elif criterio == 'keywords' and valor in [kw.lower().strip() for kw in publicacao.get('keywords', '').split(",")]:
                publicacoes_encontradas.append(publicacao)
            elif criterio == 'doi' and publicacao.get('doi', '').strip().lower() == valor:
                publicacoes_encontradas.append(publicacao)
            elif criterio == 'authors' and any(valor == autor['name'].strip().lower() for autor in publicacao.get('authors', [])):
                publicacoes_encontradas.append(publicacao)
            elif criterio == 'url' and valor in publicacao.get('url', '').strip().lower():  # Ajustando para buscar a URL corretamente
                publicacoes_encontradas.append(publicacao)
            elif criterio == 'pdf' and valor in publicacao.get('pdf', '').strip().lower():  # Ajustando para buscar o PDF corretamente
                publicacoes_encontradas.append(publicacao)
            elif criterio == 'publish_date' and publicacao.get('publish_date', '').strip() == valor:
                publicacoes_encontradas.append(publicacao)

        if not publicacoes_encontradas:
            print("Nenhuma publicação encontrada com o critério informado.")
            return

        alterada = False
        for pub in publicacoes_encontradas:
            if not alterada:
                print(f"\nPublicação encontrada: {pub}")
                confirmacao = input("Confirma ser esta a publicação que pretende alterar? (s/n): ").strip().lower()
                if confirmacao == 's':
                    print("\nEscolha o que deseja alterar:")
                    print("1. Título")
                    print("2. Resumo")
                    print("3. Palavras-chave")
                    print("4. Autores")
                    print("5. Data de Publicação")
                    print("6. URL")
                    print("0. Finalizar Alterações")

                    alteracoes_feitas = False  # Flag para verificar se houve alterações
                    while not alteracoes_feitas:
                        escolha_opcao = input("\nDigite o número correspondente à opção desejada: ")
                        if escolha_opcao == "1":
                            novo_titulo = input("Digite o novo título: ")
                            pub["title"] = novo_titulo
                            print("Título alterado com sucesso.")
                            alteracoes_feitas = True
                        elif escolha_opcao == "2":
                            novo_resumo = input("Digite o novo resumo: ")
                            pub["abstract"] = novo_resumo
                            print("Resumo alterado com sucesso.")
                            alteracoes_feitas = True
                        elif escolha_opcao == "3":
                            novas_palavras_chave = input("Digite as novas palavras-chave separadas por vírgula: ")
                            pub["keywords"] = novas_palavras_chave.split(",")
                            print("Palavras-chave alteradas com sucesso.")
                            alteracoes_feitas = True
                        elif escolha_opcao == "4":
                            novos_autores = []
                            while True:
                                autor_nome = input("Digite o nome do autor (ou pressione Enter para terminar): ")
                                if not autor_nome:
                                    break
                                autor_afiliacao = input(f"Digite a afiliação de {autor_nome}: ")
                                autores_dict = {
                                    "name": autor_nome,
                                    "affiliation": autor_afiliacao
                                }
                                novos_autores.append(autores_dict)
                            pub["authors"] = novos_autores
                            print("Autores alterados com sucesso.")
                            alteracoes_feitas = True
                        elif escolha_opcao == "5":
                            nova_data_publicacao = input("Digite a nova data de publicação (no formato YYYY-MM-DD): ")
                            pub["publish_date"] = nova_data_publicacao
                            print("Data de publicação alterada com sucesso.")
                            alteracoes_feitas = True
                        elif escolha_opcao == "6":
                            nova_url = input("Digite a nova URL: ")
                            pub["url"] = nova_url
                            print("URL alterada com sucesso.")
                            alteracoes_feitas = True
                        elif escolha_opcao == "0":
                            print("\nAlterações finalizadas.")
                            alterada = True
                            alteracoes_feitas = True  # Finaliza o loop de alterações
                        else:
                            print("Opção inválida. Tente novamente.")
                        
                    if alterada:  
                        return

                else:
                    print("Publicação não alterada.")









    ##------Criar Publicação-------##
    def inserir_publicacao(dataset):
        print("\n===== Inserir Nova Publicação =====")
        
        titulo = input("Digite o título da publicação: ")
        descricao = input("Digite a descrição da publicação: ")
        url = input("Digite a URL da publicação: ")

        if not url.startswith("http"):
            print("URL inválida. Deve começar com 'http'.")
            return

        palavras_chave = input("Digite as palavras-chave da publicação separadas por vírgula: ")
        palavras_chave_lista = palavras_chave.split(",")

    
        autores = []
        while True:
            autor_nome = input("Digite o nome do autor (ou pressione Enter para terminar): ")
            if not autor_nome:
                break  
            autor_afiliacao = input(f"Digite a afiliação de {autor_nome}: ")
            autor_orcid = input(f"Digite o ORCID de {autor_nome} (ou pressione Enter se não souber): ")
            
            autor = {
                "name": autor_nome,
                "affiliation": autor_afiliacao
            }
            
            if autor_orcid:
                autor["orcid"] = autor_orcid
            
            autores.append(autor)
        
        
        while True:
            data_publicacao = input("Digite a data de publicação (no formato YYYY-MM-DD): ")
            try:
                datetime.strptime(data_publicacao, '%Y-%m-%d')
                break
            except ValueError:
                print("Formato de data inválido. Tente novamente.")

        
        doi = input("Digite o DOI da publicação (se tiver): ")

        
        nova_publicacao_id = len(dataset) + 1

        
        nova_publicacao = {
            "id": nova_publicacao_id,  
            "title": titulo,
            "abstract": descricao,
            "keywords": palavras_chave_lista,
            "authors": autores,
            "publish_date": data_publicacao,
            "doi": doi if doi else None,  
            "url": url
        }

        
        dataset.append(nova_publicacao)
        
        print("Publicação inserida com sucesso!")



    def validar_formato_data(data_str):
        try:
            datetime.strptime(data_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False
        
    def exibir_info_publicacao(publicacao):
        print(f"ID: {publicacao['id']}, Título: {publicacao['title']}, Resumo: {publicacao['abstract']}")
        print(f"Palavras-chave: {', '.join(publicacao['keywords'])}")
        print("Autores:")
        for autor in publicacao["authors"]:
            print(f"  - {autor['name']} ({autor['affiliation']})")
        print(f"Data de Publicação: {publicacao['publish_date']}")
        print(f"URL: {publicacao['url']}")

    def exibir_resultados_publicacao(resultados, criterio):
        if resultados:
            print(f"\nResultados encontrados ({criterio}):")
            for publicacao in resultados:
                if criterio == "Título":
                    print(f"ID: {publicacao['id']}, Título: {publicacao['title']}")
                elif criterio == "Palavras-chave":
                    print(f"ID: {publicacao['id']}, Título: {publicacao['title']}, Palavras-chave: {', '.join(publicacao['keywords'])}")
                elif criterio == "Data de Publicação":
                    print(f"ID: {publicacao['id']}, Título: {publicacao['title']}, Data de Publicação: {publicacao['publish_date']}")
                else:
                    exibir_info_publicacao(publicacao)
        else:
            print(f"Não existem publicações com esse(a) '{criterio}'.")

    #----Funçoes de estatistica---

    ##---Distribuição de publicações por ano--
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

    
    def pubano(fnome):
        valores = list(distribpubporano(fnome).values())
        labels = list(distribpubporano(fnome).keys())

        plt.figure(figsize=(5, 5))
        plt.bar(labels, valores)

        
        plt.title('Distribuição de publicações por ano')

        
        plt.xticks(rotation=45, ha='right')

        for i, v in enumerate(valores):
            plt.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

        
        plt.tight_layout()
        plt.show()




    ##---Distribuição por mês de um determinado ano---
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

    
    def mesano(fnome, ano):
        valores = list(distribmesnoano(fnome, ano).values())
        labels = list(distribmesnoano(fnome, ano).keys())

        plt.figure(figsize=(5, 5))
        plt.bar(labels, valores, color = "darkseagreen")

        
        plt.title(f'Distribuição de publicações por mês de {ano}')

        

        for i, v in enumerate(valores):
            plt.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

        
        plt.tight_layout()
        plt.show()


    ##---Número de publicações por autor (top 20 autores)---
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

    
    def npubautor(fnome):
        valores = list(distribautores(fnome).values())
        labels = list(distribautores(fnome).keys())

        plt.figure(figsize=(5, 5))
        plt.bar(labels, valores, color = "orange")

        
        plt.title('Distribuição de publicações por autor Top20')

        
        plt.xticks(rotation=90, ha='right', fontsize=8)

        for i, v in enumerate(valores):
            plt.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

        
        plt.tight_layout()
        plt.show()

    ##---Distribuição de publicações de um autor por anos---
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

    
    def pubautorano(fnome,autor):
        valores = list(distribpubdeautorporano(fnome,autor).values())
        labels = list(distribpubdeautorporano(fnome,autor).keys())

        plt.figure(figsize=(5, 5))
        plt.bar(labels, valores, color = "gold")

        
        plt.title(f'Distribuição de publicação por ano de {autor}')

        
        plt.xticks(rotation=35, ha='right',fontsize=8)

        for i, v in enumerate(valores):
            plt.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

        
        plt.tight_layout()
        plt.show()


    ##---GRÁFICO5 : Distribuição de palavras-chave pela frequência (top20 palavras-chaves)---
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


    def palavrafreq(fnome):
        valores = list(distribpalavra20(fnome).values())
        labels = list(distribpalavra20(fnome).keys())

        plt.figure(figsize=(5, 5))
        plt.bar(labels, valores, color = "gold")

        
        plt.title('Distribuição de palavra-chaves pela frequência Top20')

        
        plt.xticks(rotation=90, ha='right',fontsize=8)

        for i, v in enumerate(valores):
            plt.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

        
        plt.tight_layout()
        plt.show()

    #---Gráfico Distribuição de palavras-chaves mais frequentes por ano---

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

    

    def palavrafreqano(fnome, ano):
        cores_nomeadas = list(mcolors.CSS4_COLORS.keys())
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


        
        
    #----------Estatística--------------------------------
    def estatística(dataset):
        print("\n===Selecione a oção que deseja ===")
        print("1. Distribuição de publicações por ano.")
        print("2. Distribuição de publicações por mês de um determinado ano. ")
        print("3. Número de publicações por autor.(Top 20 autores)")
        print("4. Distribuição de publicações de um autor por anos.")
        print("5. Distribuição de palavras-chave pela sua frequência. (top 20 palavras-chave)")
        print("6. Distribuição de palavras-chave mais frequentes")
        print("7. Sair")

        escolhaestatistica = input("\nEscolha uma opção: ")
        
        while escolhaestatistica!="7":
            if escolhaestatistica=="1":
                pubano(dataset)
            elif escolhaestatistica=="2":
                anoestatistica=input("Introduza o ano que deseja consultar a distribuição de publicações por mês.")
                mesano(dataset, anoestatistica)
            elif escolhaestatistica=="3":
                npubautor(dataset)
            elif escolhaestatistica=="4":
                autorestatistica=input("Introduza o nome do autor que deseja consultar.")
                pubautorano(dataset,autorestatistica)
            elif escolhaestatistica=="5":
                palavrafreq(dataset)
            elif escolhaestatistica=="6":
                anopalavrasfreq=input("Introduza o ano que deseja consultar as palvras-chaves mais frequentes.")
                palavrafreqano(dataset, anopalavrasfreq)
            else:
                print("Opção inválida.")
            estatística(dataset)
        menu_principal()







    #--------Eliminar Publicação------
    def remover_pub(bd):
        """
        Remove publicações de uma lista de dicionários com base em um critério fornecido pelo usuário.
        
        Parâmetros:
        - bd: lista de dicionários, onde cada dicionário é uma publicação.
        """
        
        criterio = input("Indique o parâmetro pelo qual pretende buscar o documento (title, abstract, keywords, doi, authors, url, pdf, publish_date): ").strip().lower()
        
        if criterio not in ['title', 'abstract', 'keywords', 'doi', 'authors', 'url', 'pdf', 'publish_date']:
            print("O parâmetro inserido não é válido.")
            return

        valor = input(f"Informe o valor do parâmetro '{criterio}': ").strip().lower()
        if not valor:
            print("Valor inválido. Operação cancelada.")
            return

        publicacoes_encontradas = []
        for publicacao in bd:
            if criterio == 'title' and valor in publicacao.get('title', '').strip().lower():  # Busca parcial no título
                publicacoes_encontradas.append(publicacao)
            elif criterio == 'abstract' and valor in publicacao.get('abstract', '').strip().lower():  # Busca parcial no resumo
                publicacoes_encontradas.append(publicacao)
            elif criterio == 'keywords':
                keywords = publicacao.get('keywords', '').strip().lower()
                if valor in [kw.strip() for kw in keywords.split(",")]:  # Busca parcial nas keywords
                    publicacoes_encontradas.append(publicacao)
            elif criterio == 'doi' and publicacao.get('doi', '').strip().lower() == valor:
                publicacoes_encontradas.append(publicacao)
            elif criterio == 'authors' and any(valor == autor['name'].strip().lower() for autor in publicacao.get('authors', [])):
                publicacoes_encontradas.append(publicacao)
            elif criterio == 'url' and valor in publicacao.get('url', '').strip().lower():  # Busca no URL
                publicacoes_encontradas.append(publicacao)
            elif criterio == 'pdf' and valor in publicacao.get('pdf', '').strip().lower():  # Busca no PDF
                publicacoes_encontradas.append(publicacao)
            elif criterio == 'publish_date' and publicacao.get('publish_date', '').strip() == valor:
                publicacoes_encontradas.append(publicacao)

        if not publicacoes_encontradas:
            print("Nenhuma publicação encontrada com o critério informado.")
            return

        removida = False
        for pub in publicacoes_encontradas:
            if not removida:
                print(f"\nPublicação encontrada: {pub}")
                confirmacao = input("Confirma ser esta a publicação que pretende apagar? (s/n): ").strip().lower()
                if confirmacao == 's':
                    bd.remove(pub)
                    print(f"Publicação removida com sucesso.")
                    removida = True
                else:
                    print("Publicação não removida.")
        
        print("Operação concluída.")



    

    

        




    def menu_principal():
        print("\n===== Menu Principal =====")
        print("1. Carregar Base de Dados")
        print("2. Guardar Base de Dados")
        print("3. Consultar Publicação")
        print("4. Analisar Publicação")
        print("5. Importar Dados")
        print("6. Exportação Parcial")
        print("7. Atualizar Publicações")
        print("8. Criar Publicação")
        print("9. Estatística")
        print("10. Eliminar Publicação")
        print("11. Help")
        print("12. Sair")

        escolha = input("\nEscolha uma opção: ")
        return escolha
    
    dataset = None 
    nome = None
    carregada_e_guardada = False 
    
    op=menu_principal()
    while op!="12":
        if op == "1":
            nome = input("Digite o nome do ficheiro a carregar (incluindo a extensão): ")
            dataset = carregar_dataset(nome)
            if dataset:
                print("Base de dados carregada com sucesso.")
            else :
                carregada_e_guardada = False
        elif op == "2":
            if dataset:
                guardar_dataset(nome, dataset)
                carregada_e_guardada = True
            else:
                print("Carregue uma base de dados primeiro.")
        elif op == "3":
            if carregada_e_guardada:
                consultar_pub(dataset)
            else:
                print("Carregue e salve uma base de dados primeiro.")
        elif op == "4":
            if carregada_e_guardada:
                AnalisarPub(dataset)
            else:
                print("Carregue e salve uma base de dados primeiro.")
        elif op == "5":
            if carregada_e_guardada:
                ficheiro = input("Digite o nome do ficheiro a importar (incluindo a extensão): ")
                dataset = importar_dados(ficheiro, dataset)
            else:
                print("Carregue e salve uma base de dados primeiro.") 
        elif op == "6":
            if carregada_e_guardada:
                exportar_publicacao(dataset)
            else:
                print("Carregue e salve uma base de dados primeiro.")    
        elif op == "7":
            if carregada_e_guardada:
                alterar_informacoes(dataset)
            else:
                print("Carregue e salve uma base de dados primeiro.")  
        elif op == "8":
            if carregada_e_guardada:
                inserir_publicacao(dataset)
            else:
                print("Carregue e salve uma base de dados primeiro.")
        elif op == "9":
            if carregada_e_guardada:
                estatística(dataset)
            else:
                print("Carregue e salve uma base de dados primeiro.")
        elif op == "10":
            if carregada_e_guardada:
                remover_pub(dataset)
            else:
                print("Carregue e salve uma base de dados primeiro.")
        elif op == "11":
            help()
        else:
            print("Opção inválida. Tente novamente.")

        op=menu_principal()
    print("Obrigada e até á próxima.")

                
    

if __name__ == "__main__":
    interface_comando()


