import pyautogui
import pandas
import time

#ABRIR O GOOGLE CHROME
pyautogui.PAUSE = 3
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#PESQUISA O YOUTUBE
time.sleep(3)
pyautogui.write('youtube.com')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=777, y=155)
pyautogui.write('Mulher segura')
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=670, y=500)
pyautogui.press('enter')
time.sleep(5)
input("Pressione Enter para fechar...")
