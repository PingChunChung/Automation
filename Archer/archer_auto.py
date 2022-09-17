import pyautogui, cv2
from time import sleep

while True:
    pyautogui.PAUSE = 0.2
    btn_summon = pyautogui.locateCenterOnScreen('D:\Auto\Archer\summon.jpg', confidence = 0.9)
    pyautogui.click(btn_summon)

    sleep(2)

    btn_continue = pyautogui.locateCenterOnScreen('D:\Auto\Archer\continue.jpg', confidence = 0.9)
    pyautogui.click(btn_continue)
    sleep(1)

    btn_confirm = pyautogui.locateCenterOnScreen('D:\Auto\Archer\confirm.jpg', confidence = 0.95)
    pyautogui.click(btn_confirm)

    sleep(1)
    
    
    btn_test = pyautogui.locateCenterOnScreen('D:\Auto\Archer\test.jpg', confidence = 0.95)
    if btn_test != Null:
        break

# 畫面移動到最下面
# pyautogui.moveTo(btn_confirm)
# pyautogui.dragTo(x = btn_confirm.x, y = btn_summon.y, duration = 0.2)
# sleep(4)
# pyautogui.moveTo(btn_confirm)
# pyautogui.dragTo(x = btn_confirm.x, y = btn_summon.y, duration = 0.2)

# 點擊boss戰券
# btn_boss = pyautogui.locateCenterOnScreen('D:\Auto\Archer\boss.jpg', confidence = 0.9)
# pyautogui.click()

# sleep(2)

# 畫面移動到最上面
# pyautogui.moveTo(btn_summon)
# pyautogui.dragTo(x = btn_summon.x, y = btn_boss.y, duration = 0.2)
# sleep(4)
# pyautogui.moveTo(btn_summon)
# pyautogui.dragTo(x = btn_summon.x, y = btn_boss.y, duration = 0.2)

# sleep(1)