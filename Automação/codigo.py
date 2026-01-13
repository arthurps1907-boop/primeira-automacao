import pyautogui
import time

#ABRIR O GOOGLE CHROME
pyautogui.PAUSE = 3
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

#PESQUISA O YOUTUBE
time.sleep(2)
pyautogui.write('youtube.com')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=777, y=155)
pyautogui.typewrite('Mulher segura', interval=0.1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=670, y=500)
pyautogui.press('enter')
time.sleep(3)
input("Pressione Enter para fechar...")
