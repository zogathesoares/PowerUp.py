import pyautogui
import time

# GABARITO PYAUTOGUI

#pyautogui.click -> clicar em algum lugar
#pyautogui.press -> apertar uma tecla
#pyautogui.write -> escrever um texto
#pyautogui.hotley -> apertar uma combinação de teclas
#pyautogui.PAUSE = 1 (ele vai pausar um segundo) or 0.3/0.5
#pyautogui.position -> ele vai mostra posição do mouse

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa
# abrir o chrome
pyautogui.press('Win')
time.PAUSE = 0.3
pyautogui.write('chrome')
time.PAUSE = 0.3
pyautogui.press('enter')


# digitar o site
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
time.PAUSE = 0.2
pyautogui.press('enter')

# espera 3 segundos
time.sleep(3)

# Passo 2: Fazer login no sistema; 
# preencher o login
pyautogui.click(x=788, y=509)
pyautogui.write('milenaborabora@gmail.com.br')

# preencher senha
pyautogui.press('tab')
pyautogui.write('teamomilena')

# botao para logar
pyautogui.press('tab')
pyautogui.press('enter')

# espera de 1 segundo caso demore para abrir o formulario
time.sleep(1)

# Passo 3: Importar a base de dados
import pandas

tabela = pandas.read_csv('produtos.csv')

print(tabela)

# Passo 4: cadastrar 1 produto e consequentemente repetir todos os processos até o final da planilha/tabela

# for linha in tabela.index: (para cada linha dentro das linhas da minha tabela executa isso daqui!)

for linha in tabela.index: # para cada linha da minha tabela repetir essas ações abaixo
    pyautogui.click(x=816, y=363)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)

    pyautogui.press('tab') #passar para o próximo campo
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)

    pyautogui.press('tab') # passar para o próximo campo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)

    pyautogui.press('tab') # passar para o próximo campo
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)

    pyautogui.press('tab') # passar para o próximo campo
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)

    pyautogui.press('tab') # passar para o próximo campo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)

    pyautogui.press('tab') # passar para o próximo campo
    obs = str(tabela.loc[linha, 'obs'])


    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press('tab') # passar para o botão enviar
    pyautogui.press('enter') 

    pyautogui.scroll(10000) # resetar scroll

# FINISH

