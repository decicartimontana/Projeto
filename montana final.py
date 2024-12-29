import json

ficheiro_data_set="./ata_medica_papers.json"

def carregardataset(ficheiro):
    if ficheiro=="":
        print("Nenhum ficheiro foi especificado.")
        return ficheiro
    else:
        with open(ficheiro, 'r', encoding='utf-8') as arquivo:
            dataset=json.load(arquivo)
            print("Data set carregado com sucesso.")
            return dataset
        

def guardar_dataset(ficheiro,dados):
    if dados is None:
        print("Não existem dados para guardar")
    else:
        with open(ficheiro, 'w', encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=2, ensure_ascii=False)
            print("Dados aramzenados com sucesso.")

def importar_dados(ficheiro, dados_existentes):
    novo_dataset=carregardataset(ficheiro)
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

def exportar_dados(ficheiro,dados_filtrados):
    if not dados_filtrados:
        return "Não há dados para exportar."
    else:
        with open(ficheiro,'w',encoding='utf-8') as arquivo:
            json.dump(dados_filtrados,arquivo,ident=2,ensure_ascii=False)
            print(f"Dados exportados com sucesso para {ficheiro}.")



atamedica=carregardataset(ficheiro_data_set)





#carregar o data set
with open('./ata_medica_papers.json', 'r', encoding='utf-8') as arquivo:
    publicacoes=json.load(arquivo)

#criar um novo arquivo em json com aquela informaçao
nome_arquivo="publicacoes_ata_medica.json"

publicacoes_formatadas= json.dumps(publicacoes, indent=2, ensure_ascii=False)


with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
    arquivo_json.write(publicacoes_formatadas)
print(f"Dados salvos com sucesso no arquivo {nome_arquivo}.")





#def format_json(json_data):
    #formatado = ""
    #i = 0
    #for char in json_data:
        #if char == '{':
            #formatado += '{\n' + ' ' * (i + 4)
            #i += 4
        #elif char == '}':
            #i -= 4
            #formatado += '\n' + ' ' * i + '}'
        #elif char == ',':
            #formatado += ',\n' + ' ' * i
        #else:
            #formatado += char

    #return formatado
