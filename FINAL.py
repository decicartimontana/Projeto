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

# Cores personalizadas
escuro = '#293B14'
claro = '#CBDDB5'
tijolo = '#6A041A'


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
            [[sg.Button("Carregar BD", size=(17, 2), font=("Cambria", 20), button_color=(claro, escuro), key="-CARREGAR-"),
              sg.Button("Gravar BD", size=(17, 2), font=("Cambria", 20), button_color=(claro, escuro), key="-GRAVAR-")],
             [sg.Button("Importar Dados", size=(17, 2), font=("Cambria", 20), button_color=(claro, escuro), key="-IMPORTAR-"),
              sg.Button("Criar Publicação", size=(17, 2), font=("Cambria", 20), button_color=(claro, escuro), key="-CRIAR-")],
             [sg.Button("Consultar", size=(17, 2), font=("Cambria", 20), button_color=(claro, escuro), key="-CONSULTAR-"),
              sg.Button("Listagem", size=(17, 2), font=("Cambria", 20), button_color=(claro, escuro), key="-LISTAGEM-")],
             [sg.Button("Atualizar", size=(17, 2), font=("Cambria", 20), button_color=(claro, escuro), key="-ATUALIZAR-"),
              sg.Button("Eliminar", size=(17, 2), font=("Cambria", 20), button_color=(claro, escuro), key="-ELIMINAR-")],
             [sg.Button("Estatísticas", size=(17, 2), font=("Cambria", 20), button_color=(claro, escuro), key="-ESTATISTICAS-"),
              sg.Button("Exportar", size=(17, 2), font=("Cambria", 20), button_color=(claro, escuro), key="-EXPORTAR-")]],
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
        
# Executar a interface gráfica
interface_grafica()