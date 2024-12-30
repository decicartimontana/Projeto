def criarpublicacao(titulo, resumo, palavraschave, doi, autoresafiliacoes, urlpdf, datapublicacao):
    publicacao = {
        'Titulo': titulo,
        'Resumo': resumo,
        'Palavras-chave': palavraschave,
        'DOI': doi,
        'Autores e Afiliacões': autoresafiliacoes,
        'URL do PDF': urlpdf,
        'Data de Publicacão': datapublicacao
    }
    return publicacao

def coletardadospublicacao():
    print('Vamos criar uma publicação! Introduza os dados, respeitando as indicações')
    titulo = input('Título: ')
    resumo = input('Resumo: ')
    palavraschave = input('Palavras-chave (separadas por vírgula): ')
    palavraschave = [palavra.strip() for palavra in palavraschave.split(',')]
    doi = input('DOI: ')
    autoresafiliacoes = {'nomeautor': autor, 'afiliacões':afiliacao}
    i=0
    n=int(input('Quantos autores estão associados?'))
    while i<n:
        autor = input('Nome do autor: ')
        afiliacao = input(f'Afiliação de {autor}: ')
        i=i+1
        autoresafiliacoes['nomeautor']=autor
        autoresafiliacoes['afiliacões']=afiliacao
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


def consultarpublicacao(publicacao, titulo, resumo, palavraschave, doi, autoresafiliacoes, urlpdf, datapublicacao):
    consulta=input('Indique o parâmetro pelo qual pretende aceder ao documento.')
    if consulta=='titulo':
        designacao=input('Título:')
        for palavra in publicacao:
            if designacao in 'Titulo':
                print(titulo)
            else:
                print('Não encontrado!')
    elif consulta=='resumo':
        designacao=input('Resumo:')
        for palavra in publicacao:
            if designacao in 'resumo':
                print(resumo) 
            else:
                print('Não encontrado!')
    elif consulta=='palavraschave':
        designacao=input('Palavras-chave:')
        for palavra in publicacao:
            if designacao in 'palavraschave':
                print(palavraschave) 
            else:
                print('Não encontrado!')
    elif consulta=='doi':
        designacao=input('DOI:')
        for palavra in publicacao:
            if designacao in 'doi':
                print(doi) 
            else:
                print('Não encontrado!')
    elif consulta=='autoresafiliacoes':
        designacao=input('Autor:')
        for palavra in publicacao:
            if designacao in 'autoresafiliacoes':
                print(autoresafiliacoes) 
            else:
                print('Não encontrado!')
    elif consulta=='urlpdf':
        designacao=('URL do PDF:')
        for palavra in publicacao:
            if designacao in 'urlpdf':
                print(urlpdf) 
            else:
                print('Não encontrado!')
    elif consulta=='datapublicacao':
        designacao=input('Data de publicação (AAAA-MM-DD): ')
        for palavra in publicacao:
            if designacao in 'datapublicacao':
                print(datapublicacao)
            else:
                print('Não encontrado!')
    else:
        print('O parâmetro inserido não é válido.') 


