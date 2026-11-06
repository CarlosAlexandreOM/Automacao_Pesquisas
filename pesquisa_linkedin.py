# Importa as bibliotecas necessárias
import pyautogui
import pyperclip
import time


# URLs das pesquisas de vagas no LinkedIn
pesquisas_linkedin = [
    "https://www.linkedin.com/jobs/search-results/?currentJobId=4483132339&keywords=%22analista%20de%20BI%20j%C3%BAnior%22%20OR%20%22analista%20de%20BI%20junior%22%20OR%20%22junior%20BI%20analyst%22&origin=JOBS_HOME_KEYWORD_HISTORY&geoId=106057199&f_TPR=r86400&f_SAL=f_SA_id_225001%3A272001",
    "https://www.linkedin.com/jobs/search-results/?currentJobId=4483149602&keywords=%22analista%20de%20dados%20j%C3%BAnior%22%20OR%20%22analista%20de%20dados%20junior%22%20OR%20%22junior%20data%20analyst%22&origin=JOB_SEARCH_PAGE_JOB_FILTER&referralSearchId=71GroePAZ8I5Sq44nsoRsA%3D%3D&geoId=106057199&distance=25&f_TPR=r86400&f_SAL=f_SA_id_225001%3A272001",
    "https://www.linkedin.com/jobs/search-results/?currentJobId=4455797054&keywords=%22est%C3%A1gio%20em%20BI%22%20OR%20%22est%C3%A1gio%20em%20Business%20Intelligence%22%20OR%20%22est%C3%A1gio%20em%20Analytics%22&origin=JOB_SEARCH_PAGE_JOB_FILTER&referralSearchId=o134LWrHHBS7U8MWy33v7g%3D%3D&geoId=106057199&distance=25&f_TPR=r86400&f_SAL=f_SA_id_225001%3A272001",
    "https://www.linkedin.com/jobs/search-results/?currentJobId=4482798772&keywords=%22est%C3%A1gio%20em%20an%C3%A1lise%20de%20dados%22%20OR%20%22est%C3%A1gio%20em%20dados%22&origin=JOB_SEARCH_PAGE_JOB_FILTER&referralSearchId=mPhurvF%2Bxv8VMF7VWtF4nQ%3D%3D&geoId=106057199&distance=25&f_TPR=r86400&f_SAL=f_SA_id_225001%3A272001"
]


# Tempos de espera ajustados ao ambiente local
tempo_inicial = 5
tempo_abertura_navegador = 3
tempo_carregamento_pagina = 3

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
for i, pesquisa in enumerate(pesquisas_linkedin):

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
    if i < len(pesquisas_linkedin) - 1:
        pyautogui.hotkey("ctrl", "t")
