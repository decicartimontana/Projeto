# Interface de linha de comando

#----- Função Menu -----#

def menu():
    print("""Menu:
          1) Carregar Base de Dados
          2) Criar Publicação
          3) Atualizar Publicação
          4) Remover Publicação
          5) Consultar Publicação
          6) Análise de publicações
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
    return bd

print(carregar_dataset("ata_medica_papers.json"))


