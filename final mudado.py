import FreeSimpleGUI as sg

#Carregar BD
import json
def carregar_dataset(fnome):
    f = open(fnome, encoding="utf-8")
    bd = json.load(f)
    if bd == "":
        print("Nenhum ficheiro foi especificado.")
    else:
        print(f"Dados carregados com sucesso. Foram lidas um total de {len(bd)} publicações.")
    return bd 

#----- Armazenamento de Dados -----#

def guardar_dataset(nome,dataset):
    ficheiro = open(nome,'w',encoding='utf-8')
    json.dump(dataset,ficheiro,ensure_ascii=False,indent=2)
    ficheiro.close()


# Cores personalizadas
escuro = '#293B14'
claro = '#CBDDB5'
tijolo = '#6A041A'

#Janela de erro
def janelaErro(tipoerro):
    layout=[
        [sg.Text(tipoerro,background_color=claro,font = ("Cooper Hewitt",12), text_color=escuro)], 
        [sg.Button("Ok", button_color=(claro,escuro),font = ('Cooper Hewitt',12))]
        ]
    window= sg.Window(title="Janela Erro",background_color=claro, default_element_size=(15,1)).Layout(layout)

    stop=False  
    while not stop:
        evento, valor = window.read()
        if evento == "Ok" or evento == sg.WIN_CLOSED:
            stop = True
    window.close()

# Interface gráfica
def interface_grafica():
    # Layout do lado esquerdo: título centralizado verticalmente
    esquerda_layout = [
        # Espaço expansível para centralização vertical
        [sg.Push(background_color=claro)],
        # Título centralizado
        [sg.Text("Sistema de Consulta e Análise de Publicações Científicas",
                 font=("Cambria", 30, "bold"), text_color=escuro, background_color=claro,
                 justification="center", size=(25, 2), expand_x=True)],
        # Espaço expansível para centralização vertical
        [sg.Push(background_color=claro)],
        # Botões Sair e Help alinhados horizontalmente
        [sg.Push(background_color=claro),
         sg.Button("Sair", size=(10, 1), font=("Cambria", 14),
                   button_color=(claro,escuro), key="-SAIR-"),
         sg.Button("Help", size=(10, 1), font=("Cambria", 14),
                   button_color=(claro, tijolo), key="-HELP-"),
         sg.Push(background_color=claro)]
    ]
    
    # Layout do menu: 10 opções em 2 colunas
    menu_layout = [
        [sg.Text("Menu", font=("Cambria", 25), text_color=escuro,
                 background_color=claro, justification="center", size=(25, 1))],
        [sg.Column(
            [[sg.Button("Carregar BD", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-CARREGAR-"),
              sg.Button("Gravar BD", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-GRAVAR-")],
             [sg.Button("Consultar Publicação", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-CONSULTAR-"),
              sg.Button("Analisar Publicações", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-LISTAGEM-")],
             [sg.Button("Importar Dados", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-IMPORTAR-"),
              sg.Button("Exportação Parcial", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-EXPORTAR-")],
             [sg.Button("Atualizar Publicação", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-ATUALIZAR-"),
              sg.Button("Criar Publicação", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-CRIAR-")],
             [sg.Button("Estatísticas", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-ESTATISTICAS-"),
              sg.Button("Eliminar Publicação", size=(17, 2), font=("Cambria", 17), button_color=(claro, escuro), key="-ELIMINAR-")]],
              
              
            background_color=claro, element_justification="center"
        )],
        # Janela de dados centralizada abaixo do menu
        [sg.Text("", size=(60, 1), font=("Cambria", 16), justification="center", key="-DADOS-",
                 background_color=claro, text_color=escuro)]
    ]
    

    # Layout principal
    layout = [
        [sg.Column(esquerda_layout, background_color=claro, vertical_alignment="center", element_justification="left"),
         sg.VSep(),
         sg.Column(menu_layout, background_color=claro, vertical_alignment="center", element_justification="center", expand_y=True)]
    ]

    # Criar a janela
    window = sg.Window("Sistema de Consulta e Análise de Publicações Científicas", layout,
                       background_color=claro)

    stop = False

    while stop == False:

        eventos, valores = window.read()
        
        if eventos in [sg.WIN_CLOSED, 'Exit']:
            stop = True

        elif eventos == '-SAIR-':
            stop = True
            window.close()


        elif eventos == "-CARREGAR-":  
            window["-DADOS-"].update("A carregar a base de dados...")
            formLayout = [
                [
                sg.Text("Base de dados:", font=("Cooper Hewitt", 12), pad=(0, 30), text_color=claro, background_color=escuro),
                sg.InputText(key="-FICHEIRO-", readonly=True, enable_events=True, text_color=escuro),
                sg.FileBrowse(file_types=[("JSON (*.json)", "*.json")], size=(8, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro)),
                sg.Button(key="-CARREGAR-", button_text="Carregar", size=(12, 1), disabled=True, font=("Cooper Hewitt", 12), button_color=(claro, escuro)) 
                ]
            ]

            wform = sg.Window('Carregamento da base de dados',formLayout, size=(650,100), background_color=claro)

            stopform = False
            while not stopform:
                inputEvent, inputValues = wform.read()
                if inputEvent == sg.WIN_CLOSED:
                    window["-DADOS-"].update("")
                    stopform = True
                elif inputEvent == '-FICHEIRO-':
                    wform["-CARREGAR-"].update(disabled=False)
                elif inputEvent == "-CARREGAR-":
                    if inputValues['Browse']:
                        BD = carregar_dataset(inputValues['Browse'])
                        nome = inputValues['Browse']
                        stopform = True
                        window["-DADOS-"].update("Base de dados carregada com sucesso!")
                        wform.close()
        elif eventos == "-GRAVAR-":
            window["-DADOS-"].update("A gravar base de dados...")
            ####################################################################################################
            if BD == None:
                janelaErro("Introduza primeiro uma base de dados!")
            
            else:
                Guardada = 1
                guardar_dataset(nome, BD)
                window["-DADOS-"].update("Base de dados gravada!")

  ####################################################################################################
        elif eventos == "-CONSULTAR-":
            window["-DADOS-"].update("A consultar publicação...")

            if BD == None :
                janelaErro ("Introduza primeiro uma base de dados!")

            elif Guardada == 0:
                janelaErro ("Guarde primeiro a base de dados!")
            
            else:
                
                layout8 = [
                    [sg.Text ('Deseja consultar a publicação por:', size= (45,1), expand_x= True, font=("Cambria", 15, "bold"),background_color=claro,text_color=escuro)],
                    [sg.Button ('Título', size=(12,1),button_color=(claro,escuro),font = ("Cooper Hewitt",12)),sg.Button ('Autor', size=(12,1),button_color=(claro,escuro),font = ("Cooper Hewitt",12)),sg.Button ('Afiliação', size=(10,1),button_color=(claro,escuro),font = ("Cooper Hewitt",12)),sg.Button ('Data de Publicação', size=(10,1),button_color=(claro,escuro),font = ("Cooper Hewitt",12)),sg.Button ('Palavras-chave', size=(17,1),button_color=(claro,escuro),font = ("Cooper Hewitt",12)),sg.Button ('Retornar ao Menu',font=("Cooper Hewitt", 14), button_color= (claro,escuro))],      
                ]
                #######
                window8 = sg.Window(title="Consultar Publicação", resizable=True, background_color=claro).Layout(layout8)
                stop8 = False
                
                while stop8 == False:
                    eventos8, valores8 = window8.read()
                    
                    if eventos8 in [sg.WIN_CLOSED, 'Exit'] or eventos8=='Retornar ao Menu':
                        stop8 = True
                        window8.close()
                    
                    elif eventos8 == 'Título':
                        window8.close()
                        resultados = []
                        
                        layout8 = [
                            [sg.Text('Título:', size=(14, 1), expand_x=True, font=("Cambria", 15, "bold"), background_color=claro, text_color=escuro)],
                            [sg.Combo(values=listatitulo(BD), key='titulo', font=("Cooper Hewitt", 12),background_color=escuro, text_color=claro)],
                            [sg.Button('OK', button_color=(claro, escuro), font=("Cooper Hewitt", 12)),
                            sg.Button('Sair', button_color=(claro, escuro), font=("Cooper Hewitt", 12))],
                        ]
                        
                        window9 = sg.Window(title="Consultar tarefa pelo Título", resizable=True, background_color=claro).Layout(layout8)
                        stop9 = False
                        
                        while not stop9:
                            eventos9, valores9 = window9.read()

                            if eventos9 in [sg.WIN_CLOSED, 'Exit']:
                                stop9 = True

                            elif eventos9 == 'OK':
                                resultados = []
                                tarefas_encontradas = consultartitulo(valores9['titulo'], BD)

                                if tarefas_encontradas:
                                    tarefas_info = [f"{tarefa['id']} : {tarefa['titulo']} : {tarefa['descricao']} : {tarefa['data_vencimento']} : {tarefa['prioridade']} : {tarefa['categoria']} : {tarefa['concluida']}" for tarefa in tarefas_encontradas]

                                    layout_titulo11 = [
                                        [sg.Text('Selecione a tarefa:', size=(20, 1), font=("Cambria", 12), background_color=claro, text_color=escuro)],
                                        [sg.Listbox(values=tarefas_info, size=(80, 10), key='-TAREFAS-', pad=((0, 0), (15, 10)), enable_events=True)],
                                        [sg.Button('Sair', button_color=(claro, escuro), font=("Cooper Hewitt", 12))]
                                    ]

                                    window_titulo11 = sg.Window('Selecionar Tarefa', layout_titulo11, grab_anywhere=False, finalize=True,
                                        background_color=claro)

                                    stoptitulo11 = False

                                    while not stoptitulo11:
                                        eventtitulo11, valuestitulo11 = window_titulo11.read()

                                        if eventtitulo11 in (sg.WIN_CLOSED, 'Sair'):
                                            stoptitulo11 = True
                                            window_titulo11.close()

                                        elif eventtitulo11 == '-TAREFAS-':
                                            selected_index = valuestitulo11['-TAREFAS-'][0]

                                            if selected_index is not None:
                                                selected_index1 = selected_index.split(':')

                        # Agora você pode usar selected_tarefa para exibir os detalhes na nova janela
                                                detalhes_tarefa_layout = [
                                                    [sg.Text(f"Tarefa Selecionada:\n\nTítulo: {selected_index1[1]}\n"
                                                    f"Descrição: {selected_index1[2]}\n"
                                                    f"Data de Vencimento: {selected_index1[3]}\n"
                                                    f"Prioridade: {selected_index1[4]}\n"
                                                    f"Categoria: {selected_index1[5]}\n"
                                                    f"Concluída: {selected_index1[6]}", text_color=escuro,background_color=claro)],
                                                    [sg.Button('Fechar', size=(10, 1), font=("Cooper Hewitt", 12), button_color=(claro, escuro))]
                                                ]

                                                window_detalhes_tarefa = sg.Window('Detalhes Tarefa', detalhes_tarefa_layout, grab_anywhere=False,
                                                        finalize=True, background_color=claro)

                                                stop_detalhes_tarefa = False

                                                while not stop_detalhes_tarefa:
                                                    event_detalhes_tarefa, values_detalhes_tarefa = window_detalhes_tarefa.read()

                                                    if event_detalhes_tarefa in (sg.WIN_CLOSED, 'Fechar'):
                                                        stop_detalhes_tarefa = True
                                                        window_detalhes_tarefa.close()

                            elif eventos9 == 'Sair':
                                stop9 = True

                        window9.close()      
# Executar a interface gráfica
interface_grafica()