import pyautogui
from time import sleep
from random import randrange

sleep(5)

for i in range(10):
    pyautogui.moveTo(1022,244,3)
    sleep(randrange(20,60))
    pyautogui.leftClick()
    pyautogui.scroll(-500)
