import pyautogui
from time import sleep
from random import randrange

sleep(5)

for i in range(10):
    pyautogui.moveTo(450, 500,3) 
    sleep(randrange(20, 60))
    pyautogui.doubleClick()
    pyautogui.scroll(-500)
    
    
