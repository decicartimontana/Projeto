import json

def format_json(json_data):
    formatado = ""
    i = 0
    for char in json_data:
        if char == '{':
            formatado += '{\n' + ' ' * (i + 4)
            i += 4
        elif char == '}':
            i -= 4
            formatado += '\n' + ' ' * i + '}'
        elif char == ',':
            formatado += ',\n' + ' ' * i
        else:
            formatado += char

    return formatado


with open('./ata_medica_papers.json', 'r', encoding='utf-8') as arquivo:
    publicacoes=json.load(arquivo)
#print(f"Total de publicações carregadas: {len(publicacoes)}")

nome_arquivo="publicacoes_ata_medica.json"

ata_medica_formatado=format_json(json.dumps(publicacoes))

with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
    arquivo_json.write(ata_medica_formatado)
    #arquivo_json.write(json.dumps(publicacoes,indent=4, verificarformatado=False))
print("Dados salvos com sucesso no arquivo 'ata_medica.json'.")




#ata_medica_formatado = format_json(ata_medica)
#with open("ata_medica_formatado.json", "w", encoding="utf-8") as arquivo_json:
    #arquivo_json.write(ata_medica_formatado)
#print("Dados salvos com formatação manual no arquivo 'ata_medica_formatado.json'!")




