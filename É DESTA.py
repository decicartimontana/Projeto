import FreeSimpleGUI as sg

# Cores personalizadas
cinza_escuro = '#8B7E66'
castanho_claro = '#CDB79E'

# Interface gráfica
def interface_grafica():
    # Layout do lado esquerdo: título e botões Sair/Help
    esquerda_layout = [
        # Título centralizado no lado esquerdo
        [sg.Text("Sistema de Consulta e Análise de Publicações Científicas",
                 font=("Cambria", 30, "bold"), text_color=cinza_escuro, expand_x= True,
                 background_color=castanho_claro, justification="center", size=(25, 2))],
        # Espaço para separação
        [sg.Push(background_color=castanho_claro)],
        [sg.Text("", size=(20, 22), background_color=castanho_claro)],  # Espaço adicional
        # Botões Sair e Help alinhados horizontalmente
        [sg.Push(background_color=castanho_claro),
         sg.Button("Sair", size=(10, 1), font=("Cambria", 14),
                   button_color=(cinza_escuro, castanho_claro), key="-SAIR-"),
         sg.Button("Help", size=(10, 1), font=("Cambria", 14),
                   button_color=(cinza_escuro, castanho_claro), key="-HELP-"),
         sg.Push(background_color=castanho_claro)]
    ]

    # Layout do menu: 10 opções em 2 colunas
    menu_layout = [
        [sg.Text("Menu", font=("Cambria", 25), text_color=cinza_escuro,
                 background_color=castanho_claro, justification="center", size=(25, 1))],
        [sg.Column(
            [[sg.Button("Carregar BD", size=(17, 2), font=("Cambria", 20), button_color=(castanho_claro, cinza_escuro), key="-CARREGAR-"),
              sg.Button("Gravar BD", size=(17, 2), font=("Cambria", 20), button_color=(castanho_claro, cinza_escuro), key="-GRAVAR-")],
             [sg.Button("Importar Dados", size=(17, 2), font=("Cambria", 20), button_color=(castanho_claro, cinza_escuro), key="-IMPORTAR-"),
              sg.Button("Criar Publicação", size=(17, 2), font=("Cambria", 20), button_color=(castanho_claro, cinza_escuro), key="-CRIAR-")],
             [sg.Button("Consultar", size=(17, 2), font=("Cambria", 20), button_color=(castanho_claro, cinza_escuro), key="-CONSULTAR-"),
              sg.Button("Listagem", size=(17, 2), font=("Cambria", 20), button_color=(castanho_claro, cinza_escuro), key="-LISTAGEM-")],
             [sg.Button("Atualizar", size=(17, 2), font=("Cambria", 20), button_color=(castanho_claro, cinza_escuro), key="-ATUALIZAR-"),
              sg.Button("Eliminar", size=(17, 2), font=("Cambria", 20), button_color=(castanho_claro, cinza_escuro), key="-ELIMINAR-")],
             [sg.Button("Estatísticas", size=(17, 2), font=("Cambria", 20), button_color=(castanho_claro, cinza_escuro), key="-ESTATISTICAS-"),
              sg.Button("Exportar", size=(17, 2), font=("Cambria", 20), button_color=(castanho_claro, cinza_escuro), key="-EXPORTAR-")]],
            background_color=castanho_claro, element_justification="center"
        )]
    ]

    # Layout principal
    layout = [
        [sg.Column(esquerda_layout, background_color=castanho_claro,vertical_alignment="top", element_justification="left"),
         sg.VSep(),
         sg.Column(menu_layout, background_color=castanho_claro, vertical_alignment="bottom", element_justification="center",expand_y=True)]
    ]



    # Criar a janela
    window = sg.Window("Sistema de Consulta e Análise de Publicações Científicas", layout,
                       background_color=castanho_claro)

    # Loop de eventos
    while True:
        eventos, valores = window.read()

        if eventos in (sg.WINDOW_CLOSED, "-SAIR-"):
            break
        elif eventos == "-HELP-":
            sg.popup("Ajuda", "Use as opções do menu para navegar pelo sistema.\n"
                              "Clique em 'Sair' para fechar a aplicação.")
        else:
            sg.popup(f"Função ainda não implementada: {eventos}")

    window.close()

# Executar a interface gráfica
interface_grafica()