import pyautogui as pag
import random
import time
#Stay available all the time with this 😼
while True:
    x, y = random.randint(600, 700), random.randint(200, 600)
    pag.moveTo(x,y,0.5)
    time.sleep(2)