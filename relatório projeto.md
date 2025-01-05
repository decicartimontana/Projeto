# Relatório Sistema de Consulta e Análise De Publicações Científicas
## Algoritmos e técnicas de programação
## Licenciatura em Engenharia Biomédica
### Autores: Clara Carvalho A107195, Inês Freitas A107140, Maria Carneiro A107242
### Docentes: José Carlos Ramalho, Luís Filipe Cunha

#### Índice









### Introdução
O presente projeto tem como objetivo o desenvolvimento de um sistema em Python para consulta, armazenamento e análise de publicações científicas. Este sistema, integrado na unidade curricular de Algoritmos e Técnicas de Programação, permite a pesquisa de artigos através de filtros como título, autores, afiliações, palavras-chave e datas de publicação. Adicionalmente, o sistema possibilita a criação, atualização e eliminação de publicações, bem como geração de gráficos que analisam métricas relevantes como a frequência de palavras-chave ou o número de publicações por autor e por ano.

O projeto inclui a implementação de duas interfaces de interação: uma interface de linha de comandos (CLI) e uma interface gráfica. Ambas devem permitir o acesso às principais funcionalidades do sistema, desde a importação e exportação de dados até à manipulação do dataset em memória persistente, armazenado num ficheiro JSON.

Este relatório detalha os requisitos e a conceção do sistema, abordando a estratégia de implementação, os algoritmos utilizados.

### Requisitos do Sistema
- **Carregamento da Base de Dados:** O programa no arranque carrega para a memória da Base de Dados que está guardado no ficheiro de suporte á aplicação.
- **Gravar base de dados:** Esta opção permite ao utilizador gravar a base de dados após esta ser inserida no sistema.
- **Consultar Publicações:** O sistema permite pesquisar publicações por vários parâmetros. Ainda permite selecionar deseja ordenar as publicações devolvidas por data de publicação ou por título.
- **Análise de Publicações:** O programa permite analisar as publicações por Autor ou por palavras-chave. Quando selecionado analisar por autor, o sistema permite selecionar ordenar por frequência dos seus artigos publicados ou por ordem alfabética. Quando selecionado analisar por palavras-chave permite selecionar ordenar pelo seu número de ocorrência nos artigos (desde a que aparece mais vezes para a que aparece menos vezes) ou por ordem alfabética.
- **Importação de dados:** Permite importar novos dados em uma publicação já existente na base de dados.
- **Exportação Parcial de dados:** Esta opção permite que o utilizador selecione dados que deseja exportar através da pesquisa do título, autor ou data de publicação, onde é exportado para um local selecionado pelo utilizador em formato json, cujo utilizador pesquisou.
- **Criação de Publicações:** A aplicação permite ao utilzador que crie um artigo específicando cada parãmetro que é obrigatório.
- **Atualização de Publicações:** Nesta opção o sistema permite atualizar a informação de uma publicação, nomeadamente  a data de publicação, o resumo, palavras-chave, autores e afiliações.
- **Dados estatíticos de Publicações:** Estatísticas como distribuição de publicações por ano, número de publicações por autor e frequências de palavras-chave são apresentadas em forma de gráficos de barras  ou gráficos circulares.
- **Eliminar Publicações:** Permite eliminar publicações da base de dados.


### Requesitos técnicos 
- **Interface gráfica e CLI:** Foram criadas duas interfaces: Interface da linha de comando(CLI) e Interface Gráfica, implementada com o FreeSimpleGUI.

### Algoritmo
#### Estrutura de dados
As publicações científicas são armazenadas como uma lista de dicionários, onde cada dicionário representa uma publicação individual. Estes dicionários incluem chaves como abstract, keywords, authors, doi, pdf, publish_date, title e url, cujos valores são geralmente strings. A exceção é a chave authors, que contém uma lista de dicionários, sendo que cada um descreve um autor com atributos como name e affiliation. Embora nem todas as chaves sejam obrigatórias, a chave title está presente em todas as publicações.


#### Módulos
O primeiro passo consiste em importar os  módulos necessários para o desenvolvimento do código. Foram importados módulos em json(*import json*) bem como os módulos necessários para a resolução de gráficos(*import matplotlib.pyplot as plt*),(import threading as mp) e janelas (*import FreeSimpleGUI as sg*). Por fim, foram importadas as funções definidas num ficheiro .py, para o ficheiro .py  onde se localiza a interface (*import Funções as fc*).

#### Linha de comandos
Inicialmente, o utilizador deve escolher a interface com a qual pretende interagir, podendo optar pela interface gráfica ou pela linha de comandos. Para tal, foram definidas duas funções: interface_Grafica() para a interface gráfica e interface_linhadecomandos() para a linha de comandos. Estas funções serão chamadas consoante a opção escolhida pelo utilizador através do botão correspondente.
!#############################[Fig.1. Escolha da linha de comando](./Imagens/1.png)   

#### Janela Principal
A janela principal da interface gráfica é definida pela função interface_grafica(), que constitui o menu de opções do sistema. A estrutura desta janela está organizada em dois grandes blocos: à esquerda estão o nome da aplicação bem como um botão de ajuda e um de saída, e à direita estão os botões que permitem realizar as operações disponíveis.

##### Estrutura da janela
###### Layout do lado Esquerdo
* Na parte superior, existe um título centralizado verticalmente, que indica o nome do sistema ("Sistema de Consulta e Análise de Publicações Científicas").
* Abaixo do título, encontram-se os botões para sair ("Sair") e para aceder à ajuda ("Help")
################### IMAGEM 

###### Layout do menu do lado Direito
* O menu contém várias opções organizadas em duas colunas. Cada botão corresponde a uma operação específica do sistema, como carregar a base de dados, gravar dados, consultar ou analisar publicações, importar ou exportar dados, criar ou eliminar publicações, entre outras funcionalidades.
* Ao clicar num botão, o utilizador aciona uma ação correspondente, mas sempre com a condição de que os dados estejam carregados no sistema, caso contrário, uma mensagem de alerta será exibida, informando o utilizador da necessidade de carregar um ficheiro antes de proceder.
####################### IMAGEMMMMM

###### Janela de dados
* Abaixo do menu, existe uma área dedicada à visualização de mensagens de estado, como feedback sobre a execução das operações ou alertas para o utilizador.
#####################IMAGEM

###### Fluxo de execução
* Ao abrir a janela, o sistema aguarda a interação do utilizador. Quando um botão é pressionado, o evento correspondente é processado.
Se o utilizador escolher a opção "Sair", o programa encerra a execução e fecha a janela.
###############IMAGEM
* A interação com os botões aciona operações como carregar dados, consultar publicações ou atualizar informações. Caso o utilizador tente realizar alguma ação sem que os dados necessários estejam carregados, uma mensagem de alerta é exibida, indicando que o ficheiro deve ser carregado primeiro.

Este fluxo e layout garantem que a interface gráfica seja intuitiva e permitem que o utilizador navegue facilmente entre as operações recebendo o devido feedback sobre as ações executadas.

##### Carregar Base de Dados
* Ao pressionar o botão "Carregar Ficheiro" na interface gráfica, é aberta uma janela onde o utilizador pode selecionar um ficheiro .json no seu computador. Após a seleção, o sistema chama a função carregar_dataset(), que tem como objetivo carregar os dados desse ficheiro para a estrutura em memória (dataset).
#################Imagemmmm

* A função carregar_dataset() utiliza a função open() para abrir o ficheiro selecionado e, em seguida, usa json.load() para carregar o conteúdo do ficheiro para uma variável em memória. Caso o ficheiro esteja vazio, será exibida uma mensagem de erro. Caso contrário, a função confirma o sucesso do carregamento e informa a quantidade de publicações carregadas.
##########################Imagemmmmmm




