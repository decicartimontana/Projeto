# Relatório da Interface Gráfica
## Algoritmos e Técnicas de programação
## Licenciatura em Engenharia Biomédica
### Autores: Mariana Alves A107205, Catarina Lamego A107280, Bianca Pereira A107193
### Docentes: José Carlos Ramalho, Luís Filipe Cunha

#### Índice
1. [Introdução](#introdução)
2. [Análise e requisitos](#análise-e-requisitos)
    2.1. [Requisitos Funcionais](#requisitos-funcionais)
    2.2. [Requisitos Técnicos](#requisitos-técnicos)
3. [Conceção do Algoritmo](#conceção-do-algoritmo)  
    3.1. [Estrutura de dados](#estrutura-de-dados)
    3.2. [Algoritmos](#algoritmos) 
        3.2.1. [Linha de Comandos](#linha-de-comandos)
        3.2.2. [Janela Principal](#janela-principal)
        3.2.2. [Carregar Ficheiro](#carregar-ficheiro)
        3.2.3. [Eliminar Publicação](#eliminar-publicação)
        3.2.4. [Atualizar Publicação](#atualizar-publicação)
        3.2.5. [Procurar Publicação](#procurar-publicação)
        3.2.6. [Listar Autores](#listar-autores)
        3.2.7. [Listar Keywords](#listar-keywords)
        3.2.8. [Estatísticas de Publicação](#estatísticas-de-publicação)
        3.2.9. [Importar Dados](#importar-dados)
        3.2.10. [Exportar dados](#exportar-dados)
        3.2.11. [Help](#help)
4. [Problemas de Concretização](#problemas-de-concretização)
5. [Conclusão](#conclusão)

#### Introdução
O projeto consiste na criação de um sistema em Python de consulta, armazenamento, criação e análise de publicações científicas. 
O sistema deve ser capaz de pesquisa de artigos usando filtros relevantes, tais como a data de publicação, as palavras-chave, autores e outros, bem como gerar relatórios (mostrando gráficos ilustrativos com estatísticas) detalhados para a análise de métricas dos artigos e dos seus autores.
Este relatório faz parte do projeto da Unidade Curricular de Algoritmos e Técnicas de Programação e está estruturado da seguinte maneira:
- Apresentação dos requisitos que nos foram apresentados, assim como análise dos mesmos;
- Conceção da resolução, apresentando a estratégia e a linha de raciocínio, tal como a descrição dos algoritmos elaborados;
- Problemas encontrados ao longo da realização do trabalho e as suas soluções;
- Conclusão incluindo reflexões do trabalho;

#### Análise e requisitos
O sistema foi concebido para atender aos seguintes requisitos principais:

##### Requisitos Funcionais
- **Carregamento do Dataset:** O sistema deve ser capaz de carregar uma base de dados de publicações armazenada em formato JSON, permitindo a manipulação eficiente dos registros em memória.
- **Criação de Publicações:** O sistema deve possibilitar a criação de novas publicações. Para isso, o usuário deve fornecer informações como título, resumo, palavras-chave, lista de autores, data de publicação e URLs associados.
- **Atualização de Publicações:** Publicações existentes podem ser atualizadas, com foco em campos como resumo, palavras-chave e afiliações de autores.
- **Consulta de Publicações:** Os usuários devem ser capazes de pesquisar publicações com base em critérios como título, autores, palavras-chave e intervalos de datas. Também é possível ordenar os resultados por diferentes parâmetros.
- **Relatórios e Gráficos:** Estatísticas como distribuição de publicações por ano, número de publicações por autor e frequências de palavras-chave devem ser apresentadas em relatórios ilustrados com gráficos claros e informativos.
- **Persistência de Dados:** Alterações realizadas no sistema devem ser salvas de forma persistente no arquivo JSON.
- **Exportação e Importação de Dados:** Permitir a importação de novos dados de outras bases e a exportação de subconjuntos de dados filtrados

##### Requisitos Técnicos
- **Implementação em Python:** Todas as funcionalidades foram desenvolvidas utilizando a linguagem Python, fazendo uso de sua biblioteca padrão e pacotes externos.
- **Interface Gráfica e CLI:** Duas interfaces foram criadas para interação com o usuário: Interface de Linha de Comando (CLI) para maior flexibilidade e Interface Gráfica (GUI), implementada com PySimpleGUI, para facilitar a utilização.


#### Conceção do Algoritmo
##### Estrutura de dados
As publicações científicas a analisar são representadas por uma estrutura de dados definida como uma lista de dicionários, na qual cada dicionário representa uma publicação. Cada dicionário pode ter as chaves: abstract, keywords, authors, doi, pdf, publish_date, title e url. Todas as chaves recebem uma string como valor, exceto a chave autores que recebe uma lista de dicionários, na qual cada dicionário representa um autor. Cada autor pode ter as chaves: name, affiliation e orcid.
As publicações podem ou não ter as chaves nomeadas em cima, no entanto, a chave 'title' é constante em todas.

##### Algoritmos
O primeiro passo consiste em importar os  módulos necessários para o desenvolvimento do código. Foram importados módulos em json(*import json*) e em os (*import os*), bem como os módulos necessários para a resolução de gráficos(*import matplotlib.pyplot as plt*) e janelas (*import PySimpleGUI as sg*). Por fim, foram importadas as funções definidas num ficheiro .py, para o ficheiro .py  onde se localiza a interface (*import f_projeto as fpj*).

###### Linha de Comandos
Inicialmente o utilizador deve escolher com que interface pretende trabalhar, podendo optar pela interface gráfica ou pela linha de comando.
Para tal definimos uma função *interfaceGrafica()* para a interface gráfica e uma função *interfacelinhadecomandos()* para a linha de comandos, que serão chamadas conforme o botão escolhido pelo utilizador.
![Fig.1. Escolha da linha de comando](./Imagens/1.png)

###### Janela Principal
A janela principal da interface gráfica é definida pela função *criar_main_window()* e corresponde ao menu da linha de comandos. É nesta janela principal que se encontram as principais operações do sistema. Cada botão corresponde a uma operação específica, que será explicada em detalhe a seguir.
À esquerda encontram-se os botões das possíveis operações, enquanto à direita é visivel uma área onde são exibidas mensagens conforme o dataset em memória vai sofrendo alterações. Se o utilizador quiser executar operações sem antes carregar um ficheiro no sistema é exibida uma mensagem de alerta, que informa o mesmo dessa necessidade.
![Fig.2. Janela Principal](./Imagens/2.png)
![Fig.3. Mensagem de Alerta](./Imagens/3.png)

###### Carregar Ficheiro
Ao pressionar o botão 'Carregar Ficheiro' é aberta uma janela que permite ao utilizador selecionar um ficheiro .json dos seus ficheiros e posteriormente é chamada a função *carregar_dataset()*. Esta função é responsável por abrir o ficheiro .json, com o comando *open()* e carregar os seus dados para a estrutura *dataset* em memória, com o comando *json.load()*.
![Fig.4. Carregar Ficheiro](./Imagens/4.png)
![Fig.5. Mensagem de Sucesso](./Imagens/17.png)
![Fig.6. Resultado ](./Imagens/18.png)

###### Criar Publicação
Ao pressionar o botão 'Criar Publicação' é aberta uma janela que permite ao utilizador criar uma nova publicação e adiciona-la ao dataset em memória através da função *criar_publi()*. 
![Fig.7. Criar Publicação](./Imagens/5.png)
A função é responsável por abrir uma nova janela que exibe os campos que o utilizador pode criar no lado esquerdo. Permite adicionar um alargado numero de autores à publicação, uma vez que após preencher os campos respetivos ao autor e pressionar o botão 'Adicionar Autor', os mesmos serão adicionados a uma lista previamente definida e vazia, que no final será o valor da chave 'authors'. O utilizador pode observar os autores que vai adicionando na área a baixo do botão 'Adicionar Autor'. Caso tente adicionar um autor sem preencher os campos name ou affiliation um mensagem de aviso é exibida.
![Fig.8. Mensagem de Aviso - Name, Affiliation](./Imagens/7.png)
Após os campos desejados estarem preenchidos o utilizador pressiona 'OK', os dados são adicinados a um dicionário vazio previamente definido, a publicação é exibida na área mais à direita da janela na forma definida pela função *mostrar_publi()* e adicionada ao dataset em memória. Os campos do lado esquerdo são limpos e permitem que o utilizador crie outra publicação.
Uma ves que o título é uma chave presente em todas as publicações o prenchimento deste campo é obrigatório, sendo uma mensagem de aviso exibida caso contrário.
![Fig.9. Mensagem de Aviso - Título](./Imagens/6.png)
![Fig.10. A Criar Nova Publicação](./Imagens/19.png)
![Fig.11. Exibir Publicação Criada](./Imagens/20.png)
![Fig.12. Resultado](./Imagens/21.png)

###### Eliminar Publicação
Ao pressionar o botão 'Eliminar Publicação' é chamada a função *eliminar_publi()* que abre uma janela que para a introdução do título de uma publicação.
![Fig.13. Procurar a Publicação a Eliminar](./Imagens/8.png)
A função vai percorrer o dataset através de um for loop e se o título for encontrado então a publicação será adicionada a uma lista previamente definida e vazia. Isto vai permitir abrir uma janela que exibe a publicação encontrada do lado esquerdo na forma definida pela função *mostrar_publi()* e do lado direito um pedido de confirmação da operação. Caso a operação seja confirmada, então a publicação será eliminada do dataset, utilizando o comando *.remove()*.
Se nenhuma publicação com o título inserido for encontrada então é exibida uma mensagem de aviso.
![Fig.14. Eliminar Publicação](./Imagens/9.png)
![Fig.15. Resultado](./Imagens/22.png)

###### Atualizar Publicação
Ao pressionar o botão 'Atualizar Publicação' é chamada a função *atualizaPubli()* que, tal como a função anterior, abre uma janela que para a introdução do título de uma publicação. A função vai percorrer o dataset através de um for loop e se o título for encontrado então a publicação será adicionada a uma lista previamente definida e vazia. Isto vai permitir abrir uma janela que exibe a publicação encontrada do lado esquerdo na forma definida pela função *mostrar_publi()* e do lado direito os campos que podem ser atualizados. O campo autores permite eliminar, criar ou editar um autor específico da publicação, basta pressionar o botão da respetiva operação.
A edição de uma publicação é feita de forma relativamente simples, igualando as chaves do dicionário da publicação com os valores dos campos inseridos. Se não for inserida informação no campo então ele permanece inalterado.
Após os campos pretendidos estarem preenchidos e o utilizador pressionar 'OK' a publicação é editada no dataset e exibida numa janela na forma definida pela função *mostrar_publi()*.
Se nenhuma publicação com o título inserido for encontrada então é exibida uma mensagem de aviso.
![Fig.16. Atualizar Publicação](./Imagens/10.png)

###### Procurar Publicação
Ao pressionar o botão 'Procurar Publicação' é chamada a função *criar_procurar_window()* que exibe uma nova janela na qual o utilizador pode selecionar os critérios de busca pressionando o botão respetivo. 
![Fig.17. Procurar Publicação](./Imagens/11.png)
Cada botão tem associado uma determinada função que pesquisa a publicação pelo critério correspondente e exibe as publicações encontradas na área à direita da janela na forma definida pela função *mostrar_publi()*. 

- **Botão 'Autor':** chama a função *procurar_autores()* que abre uma janela que permite ao utilizador introduzir o nome do autor que procura. A função percorre o dataset e conforme encontra publicações com o nome inserido pelo utilizador no valor da chave 'name' adiciona a publicação a uma lista inicialmente vazia através do comando *.append()*. Se nenhuma publicação for encontrada então é exibida uma mensagem de aviso. Posteriormente é possivel escolher se a lista de publicações encontradas deve estar ordenada por data (*ordenaData()*) de publicação ou título(*ordenaTitulo()*), bem como se o utilizador pretende salvar a lista (*popup_salvar()* que utiliza a função *salvar_em_arquivo()* que, por sua vez, utiliza o comando *json.dump()* para salvar a lista em um ficheiro .json).
As funções abaixo funcionam de forma em tudo semelhente à função explicada, apenas avaliam valores de chaves distintas:
- **Botão 'Keyword':** chama a função *procurar_keywords()*
- **Botão 'Título':** chama a função *procurar_titulo()*
- **Botão 'Afiliação':** chama a função *procurar_afiliacao()*
- **Botão 'Data':** chama a função *procurar_data()*
![Fig.18. Procurar Publicação - Autor](./Imagens/23.png)
![Fig.19. Procurar Publicação - Ordenar(título)](./Imagens/24.png)
![Fig.20. Procurar Publicação - Salvar(não)](./Imagens/25.png)
![Fig.21. Procurar Publicação - Resultado](./Imagens/26.png)

###### Listar Autores
Ao pressionar o botão 'Listar Autores' é chamada a função *listaAutores()* responsável por percorrer o dataset em memória e adicionar o nome dos autores que vai encontrando no valor da chave 'name' a uma lista definida inicialmente como vazia, caso o nome do autor ainda não conste na lista. No final a lista é ordenada alfabeticamente e pode ser salva num ficheiro .json através da função *salvar_em_arquivo()*.
O resultado é exibido na área mais à direita da janela principal e cada elemento da lista(autor) ocupa uma linha.

###### Listar Keywords
Ao pressionar o botão 'Listar Keywords' é chamada a função *listaKeywords()* que funciona de forma semelhante à função anterior, apenas avalia os valores na chave 'keywords' dos dicionários do dataset. Uma vez que os valores são uma string que contém todos os keywords separados por vírgulas e espaços, a função *split(', ')* é utilizada para transformar a string em uma lista de strings.

###### Estatísticas de publicação
Ao pressionar o botão 'Estatísticas de publicação' é chamada a função *criar_stats_window()* responsável por criar uma janela com as opções de distrições que é possível executar à esquerda, na forma de botões, uma área superior direita para exibir o resultado da distribuição e uma área inferior disponível para visualização do gráfico da respetiva distribuição se assim for desejado pelo utilizador. 
![Fig.22. Estatísticas de Publicação](./Imagens/27.png)

- **Botão 'por ano':** chama a função *distribAno()* que calcula a distribuição de publicações por ano e exibe o resultado na área superior direita, podendo o utilizador ordenar esse resultado por ano ou número de publicações através dos comandos *sorted(list(.items))* e *sorted(list(.items), key=topordena)*, sendo o *topordena()* uma função que acede ao elemento de índice 1 de um tuplo. Uma distribuição é apenas um dicionário no qual as keys são o ano (acedido com utilização do comando *.split('-')* e dos indicices da lista de strings criada por este) e conforme é lida uma publicação que pertence a determinado ano vão sendo acumuladas contagens.
Posteriormente é chamada a função *graf_distribAno()* se o utilizador selecionar 'Sim' na janela que lhe é apresentada a questionar se deseja visualizar o gráfico da distribuição.
A função *graf_distribAno()* utiliza a biblioteca do *matplotlib* para criar o gráfico. Inicialmente utiliza-se o comando *plt.clf()* para limpar gráficos que possam ter sido criados anteriormente, evitando que eles se adicionem. posteriormente define-se o tamanho da figura com o comando *plt.figure(figzise=)* e para melhor leitura dos dados inclinamos os valores no eixo x com o comando *plt.xticks(rotation=45, rotation_mode='anchor', ha='right')*. O comando *plt.gca()* permite aceder aos eixos do grafico possibilitando mudanças das sua propriedades e o comando *plt.tight_layout()* é essencial para que a imagem apareça corretamente na interface. Por fim, denote-se que o return desta função é o *path* para a imagem  do gráfico guardada na biblioteca do utilizador através do comando *plt.savefig()*, uma vez que só assim é possível mostra-lo na interface.
Os seguintes botões funcionam de forma semelhante pelo que apenas iremos explicar particularidades dos mesmos.
- **Botão 'Por mês do Ano':** chama a função *distribMêsAno()* que calcula a distribuição de publicações por mês do ano inserido pelo utilizador numa janela que lhe é apresentada. Afunção verifica o ano de publicação da publicação e se ele for igual ao ano inserido pelo utilizador então verifica o mês de publicação e vai acumulando contagens no dicionário que representa a distribuição. Posteriormente é chamada a função *graf_distribMêsAno()* em tudo semelhante ao grafico anterior.
- **Botão 'Pelos TOP20 Autores':** chama a função *distribTOP20Autor()* que calcula a distribuição de publicações pelos 20 autores mais prolíficos. A função vai percorrer o dataset e verificar o nome do autor de cada publicação, adicionando o nome do autor ao dicionário caso ele ainda não esteja nele, e vão sendo acumuladas contagens no valor correspondente caso o autor esteja no dicionário. Posteriormente é o dicionário é transformado em lista utilizando o comando *list(.items())* e ordenado conforme o comando *sorted(list(.items), key=topordena)* (pelo numero de publicações). Finalmente 'corta-se' a lista de maneira a que apenas os primeiros 20 elementos estejam integrados na mesma e com o comando *dict()* voltamos a transformar a lista em dicionário.
Só agora é chamada a função *graf_distribTOP20Autor()* que cria o gráfico correspondente à distribuição se assim for desejado.
- **Botão 'Por Ano de x Autor:** chama a função *distribAutorAno()* semelhante a *distribMêsAno()* e posteriormente, se o utilizador desejar observar a mesma como gráfico é utilizada a função *graf_distriAutorAno()*.
- **Botão 'Pelos TOP20 Keywords':** chama a função *distribTOP20Keywords()* semelhante a *distribTOP20Autor()* e posteriormente, se o utilizador desejar observar a mesma como gráfico é utilizada a função *graf_distriTOP20Keywords()*.
- **Botão 'Por Ano da Keyword x:** chama a função *distribKeyWordAno()* e posteriormente, se assim desejado , é utilizada a função *graf_distriKeyWordAno()*.
![Fig.23. Estatísticas de publicação - Resultado](./Imagens/12.png)

###### Importar Dados
Ao pressionar o botão 'Importar Dados' abre-se uma janela que permite selecionar o ficheiro .json a importar. A função *carregar_dataset* é responsável por abrir o ficheiro selecionado e guardar a sua informação numa variável denominada *'dataset_importado'*. Se este ficheiro não existir, então é exibida uma mensagem de aviso, caso contrario cria-se uma nova variável *'titulos_existentes'* que será a lista de todos os títulos do dataset em memória. Posteriormente a função verifica se os titulos das publicações do ficheiro importado existem no dataset em memória. Se não existirem, então as publicações passam a integrar a variável *'novas_publis'*. Por fim, se a variável *'novas_publis'* não estiver vazia, então é concatenada ao dataset em memória e é exibida uma mensagem de sucesso correspondente na área mais à direita da janela principal, caso contrario é exibida na mesma área a mensagem de que nada foi alterado no dataset.
![Fig.24. Mensagem de Inalteração - Importar Dados](./Imagens/13.png)

###### Exportar Dados
Ao pressionar o botão 'Exportar Dados' abre-se uma janela que permite ao utilizador introduzir o nome do ficheiro em que pretende guardar os dados. Posteriormente é chamada a função *salvar_em_arquivo()* que é responsável por salvar o dataset em memória no ficheiro .json nomeado pelo utilizador. 
A qualquer momento após um ficheiro ser carregado para o sistema, se o utilizador sair do mesmo o dataset em memória é automaticamente salvo, utilizando a mesma função, num ficheiro nomeado 'medical_papers_updated.json'. 
![Fig.25. Exportar Dados - Nomear Ficheiro](./Imagens/14.png)
![Fig.26. Exportar Dados - Automatico](./Imagens/15.png)

###### Help
O botão 'Help' abre uma janela com as instruções de utilização do sistema. Aparece nas 4 janelas mais importantes do sistema: janela principal, janela de criar publicação, janela de procurar publicação e janela de estatísticas de publicação.
É um popup de texto que exibe informações, orientações relacionados com a funcionalidade e navegação na janela em que se encontra. Este recurso tem como objetivo facilitar a experiência do utilizador, promovendo a autonomia e a eficiência na utilização da interface.
![Fig.27. Help - Exemplo da Mensagem da Janela Principal](./Imagens/16.png)


#### Problemas de Concretização
Durante o processo de desenvolvimento da aplicação deparamo-nos bastante vezes com erros que exigiam a consideração de novas alternativas.
Um dos problemas que encontramos foi o próprio layout da interface. Sendo o PySimpleGUI um módulo relativamente desconhecido para nós foi necessária alguma pesquisa de maneira a organizar a informação de forma mais adequada para a sua visualização, nomeadamente tornando elementos *scrollable* ou organizando a informação por colunas. A comunicação entre as bibliotecas do PySimpleGUI e do matplotlib foi outra das principais dificuldades, devido ao tamanho do gráfico e ao tamanha do local em que seria inserido, bem como a necessidade de guardar o gráfico como .png para ser adicionado à interface.
Talvez o problema mais persistente e difícil de contornar foi o cancelar ou fechar de uma janela menor, que não era possível fazer sem que a aplicação se fechasse. Para contornar este problema foi necessário perceber que era a falta de informação em determinados parâmetros que causava este problema e utilizar isso a nosso favor. Nomeadamente com a utilização do comando *isinstance()* para mostrar o resultado de uma pesquisa na janela de procura apenas se existirem publicações com o filtro aplicado, caso contrário apenas aparece uma mensagem de aviso e o sistema continua a funcionar normalmente.
Estes apenas alguns exemplos das adversidades maiores com que nos deparamos, uma vez que os restantes foram simples erros de código que, resolvidos por várias tentativas-erro e pesquisas mais aprofundadas.


#### Conclusão
Concluindo, consideramos que conseguimos elaborar a aplicação requisitada com sucesso e capaz de executar todos os pontos propostos. Admitimos estar satisfeitas com o nosso projeto que apenas foi possível com inúmeras horas de trabalho e pesquisa relacionadas com os diversos problemas que não esperávamos encontrar, que conduziram a múltiplas tentativas-erro e pesquisas aprofundadas.
Apesar das dificuldades, consideramos esta aplicação funcional com uma interface de fácil uso e interpretação, bem como esteticamente agradável. 
Para o desenvolvimento dos algoritmos presentes no sistema foi essencial o acompanhamento constante da UC, o que nos garantiu o conhecimento necessário para a manipulação de estruturas de dados, o trabalho com bibliotecas e a construção da interface.
Assim, concluimos que este projeto foi essencial para sedimentar os conhecimentos obtido na UC, aplicando-os numa situação prática e mais próxima de uma situação real, permitindo-nos compreender a inter-relação e a importância das ferramentas adquiridas na UC.