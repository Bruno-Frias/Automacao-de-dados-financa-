import yfinance
codigo = input('Digite o código da ação desejada: ')
dados = yfinance.Ticker(codigo).history('6mo')
print(dados)
fechamento = dados.Close
print(fechamento)

maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento.iloc[-1]
print('Máxima é {:.2f}'.format(maxima))
print('Mínima é {:.2f}'.format(minima))

print('Cotação atual é {:.2f}'.format(atual))

import time
import pyautogui
import pyperclip

pyautogui.press('win')
time.sleep(5)
pyautogui.write('outlook')
time.sleep(20)
pyautogui.press('enter')
time.sleep(0)


pyautogui.hotkey('ctrl', 'n')
time.sleep(20)
pyautogui.write('brunorfrias@gmail.com')
time.sleep(2)
pyautogui.press('tab', presses=2)  
pyperclip.copy('Análise de dados')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
time.sleep(3)
pyperclip.copy('''Boa noite!
Senhores fico feliz por ter feito esses dados todos''')
pyautogui.hotkey('ctrl', 'v')
pyperclip.copy(dados) 
pyautogui.hotkey('ctrl', 'v')
pyperclip.copy(fechamento)               
pyautogui.hotkey('ctrl', 'v')
pyperclip.copy(maxima)               
pyautogui.hotkey('ctrl', 'v')
pyperclip.copy(minima)               
pyautogui.hotkey('ctrl', 'v')
pyperclip.copy(atual)               
pyautogui.hotkey('ctrl', 'v')
time.sleep(10)
pyautogui.press('esc')
time.sleep(5)
pyautogui.press('enter') 
