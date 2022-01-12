Intensivão de Python [Aula 1]

import pyautogui 
import pyperclip
import time

pyautogui.POUSE = 1  #entre um comndo e outro ele vai espera 1 segundopara rodar (0.5 se estiver lento de mais)

pyautogui.(hotkeycomando> teclado)("ctrl", "t") #para abri uma tela
pyerclip.copy(https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga)# pyperclip é para caracters especiasi 
pyautogui.hotket("ctrl", "v")
pyautogui.press("enter")

time.sleep(6) #esta pausa é para esperar o sistema carregar 
pyautogui.click(x=234, y=655, cliks=2)# para dar 2 clicks (cliks=2)
#para botão eeeesquerdo button=right
pyautogui.click(x=234, y=655, cliks=2, button=right)

#local entrar local 
pyautogui.press("win")
pyautogui.write("crhome") coloque o nome do sistema qie ele vai pesqisar no win 
pyautogui.press("enter")

#Para achar a localidade do mouser 
time.sleep(5)
pyautogui.position()

#trabalhando com pandas .. import pandas se utilizar jupyter

import pandas as pd #podemos dar o apelido de "pd"

tabelaRs = pandas.read_ecel(r"C:\Users\mathe\OneDrive\Área de Trabalho\itensivão de python") 
display(tabelaRs)# dispaly igual a print() porem deixa as coisa mais bonita 
# dizendo o que o panda precia fazer dentro, tabela  vai armazenar  que o pd vai ler em excel

faturamento = tabela["valor final"].sum() # para selecionar coluna usamos []
qtd_produtos = tabela["Quantidade"].sum()

#autmarizar envio de email 
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/?pli=1#inbox")
pyautogui.press("enter")


time.sleep(5)
 #pegar o botão de enviar email
 pyautogui.click(x=342, y=456)
 
#para preencher destino
pyautogui.write("nome do email")
pyautogui.press("tab")# seleciona o email
pyautogui.press("tab")# passa de campo 

#escrever email
texto = """ 
 prezado boa tarde!
 segue relatoro de faturamentos
  
Regards 
"""
#clicar em enviar
pyautogui.press("ctrl", "enter")




















