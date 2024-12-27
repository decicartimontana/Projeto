def criarpublicacao(titulo, resumo, palavraschave, doi, autoresafiliacoes, urlpdf, datapublicacao):
    publicacao = {
        'Titulo': titulo,
        'Resumo': resumo,
        'Palavras-chave': palavraschave,
        'DOI': doi,
        'Autores e Afiliações': autoresafiliacoes,
        'URL do PDF': urlpdf,
        'Data de Publicação': datapublicacao
    }
    return publicacao

def coletardadospublicacao():
    print('Vamos criar uma publicação! Introduza os dados, respeitando as indicações')
    titulo = input('Título: ')
    resumo = input('Resumo: ')
    palavraschave = input('Palavras.chave (separadas por vírgula): ')
    palavraschave = [palavra.strip() for palavra in palavraschave.split(',')]
    doi = input('DOI: ')
    autoresafiliacoes = {}
    n=int(input('Quantos autores estão associados?'))
    i=0
    while i<n:
        autor = input('Nome do autor: ')
        afiliacao = input(f'Afiliação de {autor}: ')
        autoresafiliacoes[autor] = afiliacao
        i=i+1
    urlpdf = input('URL do PDF: ')
    datapublicacao = input('Data de publicação (AAAA-MM-DD):')


    publicacao = criarpublicacao(
        titulo=titulo,
        resumo=resumo,
        palavraschave=palavraschave,
        doi=doi,
        autoresafiliacoes=autoresafiliacoes,
        urlpdf=urlpdf,
        datapublicacao=datapublicacao
    )
    
    return publicacao

publicacaocriada = coletardadospublicacao()
print("\nPublicação criada com sucesso!")

def apagarpublicacao(publicacao, titulo, resumo, palavraschave, doi, autoresafiliacoes, urlpdf, datapublicacao):
    apagar=input('Indique o parâmetro pelo qual pretende aceder ao documento.')
    if apagar=='titulo':
        procurar=input('Título:')
        for palavra in publicacao:
            if procurar in 'Titulo':
                print(titulo)
    elif apagar=='resumo':
        procurar=input('Resumo:')
        for palavra in publicacao:
            if procurar in 'resumo':
                print(resumo) 
    elif apagar=='palavraschave':
        procurar=input('Palavras-chave:')
        for palavra in publicacao:
            if procurar in 'palavraschave':
                print(palavraschave) 
    elif apagar=='doi':
        procurar=input('DOI:')
        for palavra in publicacao:
            if procurar in 'doi':
                print(doi) 
    elif apagar=='autoresafiliacoes':
        procurar=input('Autor:')
        for palavra in publicacao:
            if procurar in 'autoresafiliacoes':
                print(autoresafiliacoes) 
    elif apagar=='urlpdf':
        procurar=('URL do PDF:')
        for palavra in publicacao:
            if procurar in 'urlpdf':
                print(urlpdf) 
    elif apagar=='datapublicacao':
        procurar=input('Data de publicação (AAAA-MM-DD): ')
        for palavra in publicacao:
            if procurar in 'datapublicacao':
                print(datapublicacao) 
    else:
        print('O parâmetro inserido não é válido.') 
