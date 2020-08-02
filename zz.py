import pyautogui
import pygetwindow as gw
import time

x=520
y=661
num_seconds=0.5

for i in range(1,2):
    pyautogui.hotkey('win', 'd')
    pyautogui.moveTo(x, y, duration=num_seconds)
    pyautogui.doubleClick()
    
    windowTitle = gw.getActiveWindow().title
    #print(windowTitle)
    # windowTitle = '1533.txt'
    # notepadWindow = gw.getWindowsWithTitle(windowTitle)[0]
    # print (notepadWindow)
    windowTitle.maximize()
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')
    
