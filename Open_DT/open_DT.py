import pyautogui
from time import sleep, time
import keyboard

pyautogui.PAUSE = 0.1

pyautogui.press('winleft')

# 把comeu放到開始才能用
pyautogui.moveTo(520, 790)
pyautogui.hscroll(-300)

sleep(1)

btn_location = pyautogui.locateOnScreen('C:/Scraper/ComEu.png', confidence=0.95)
btn_point = pyautogui.center(btn_location)
pyautogui.click(btn_point)

sleep(1)
pyautogui.typewrite("cd C:/DT/CNT.2022.v4.1/")
pyautogui.press('Enter')

sleep(1)
pyautogui.typewrite("/c/dt/CNT.2022.v4.1/dt.bat start")
pyautogui.press('Enter')
pyautogui.hotkey('winleft', 'd')
tab_location = pyautogui.locateOnScreen('C:/Scraper/Tab_ComEu.png', confidence=0.95)
pyautogui.click(tab_location)
pyautogui.typewrite("ssh bigred@192.168.88.3")
pyautogui.press('Enter')
pyautogui.typewrite("bigred")
pyautogui.press('Enter')