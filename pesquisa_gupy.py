# Importa as bibliotecas necessárias
import pyautogui
import pyperclip
import time


# URLs das pesquisas de vagas na Gupy
pesquisas_gupy = [
    "https://portal.gupy.io/job-search/term=Dados&workplaceTypes[]=remote",
    "https://portal.gupy.io/job-search/term=Est%C3%A1gio&workplaceTypes[]=remote",
    "https://portal.gupy.io/job-search/term=Est%C3%A1giario&workplaceTypes[]=remote"
]



# Tempos de espera ajustados ao ambiente local
tempo_inicial = 5
tempo_abertura_navegador = 3
tempo_carregamento_pagina = 1.5

# Configura uma pausa após cada ação do PyAutoGUI
pyautogui.PAUSE = 1


# Aguarda antes de iniciar a automação
time.sleep(tempo_inicial)


# Abre o Google Chrome pelo menu Iniciar do Windows
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


# Aguarda a abertura do navegador
time.sleep(tempo_abertura_navegador)


# Abre cada pesquisa em uma aba do navegador
for i, pesquisa in enumerate(pesquisas_gupy):

    # Seleciona a barra de endereços
    pyautogui.hotkey("ctrl", "l")

    # Copia a URL para a área de transferência e cola na barra
    pyperclip.copy(pesquisa)
    pyautogui.hotkey("ctrl", "v")

    # Acessa a URL
    pyautogui.press("enter")

    # Aguarda o carregamento inicial da página
    time.sleep(tempo_carregamento_pagina)

    # Abre uma nova aba se ainda houver pesquisas pendentes
    if i < len(pesquisas_gupy) - 1:
        pyautogui.hotkey("ctrl", "t")
