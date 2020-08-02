#! python3
import pyautogui, os
#pyautogui.PAUSE = 1.5

inpath = "input"
outpath = "output"
os.makedirs(outpath, exist_ok=True)
pigs = []
for file in os.listdir(inpath):
    if os.path.isdir(inpath+'/'+file): # 判断是否为文件夹
      pigs.append(file)
      os.makedirs(outpath+'/'+file, exist_ok=True)

# The first step: open finder and change to the target folder containing photos
pyautogui.hotkey('option', 'space')  # open alfred
pyautogui.write('finder', interval=0.15)
pyautogui.press('enter') # now the finder has opened

pyautogui.hotkey('shift', 'command','G')  # go to folder
pyautogui.write('/Users/zhezhang/Desktop/pyautogui/input/123456', interval=0.05)
pyautogui.press('enter') # now we are at the target folder

# # The second step: select all files and open and save as it with previewer
pyautogui.moveTo(415, 189, duration=0.3)
pyautogui.click()
pyautogui.hotkey('command', 'a') # select all
pyautogui.doubleClick() # double-click to open
pyautogui.moveTo(200, 200, duration=0.3) # move to the left margin
pyautogui.hotkey('command', 'a') # select all
pyautogui.moveTo(111, 12, duration=0.3) # move to the '文件' button
pyautogui.click(x=111, y=12) # click to open
pyautogui.moveTo(164, 372, duration=0.3) # move to the '导出为...' button
pyautogui.click(x=164, y=372) # click to open

x, y = (90, 208)
pyautogui.moveTo(x, y, duration=0.3)
pyautogui.click()
# # pyautogui.hotkey('shift', 'command','G')  # go to folder
# # pyautogui.write('/Users/zhezhang/Desktop/pyautogui/output/123456', interval=0.05)
# # pyautogui.press('enter') # now we are at the output folder
pyautogui.moveTo(181, 837, duration=0.3) # move to the '选项' button
pyautogui.click() # click to open
# pyautogui.moveTo(518, 745, duration=0.3) # move to the '格式' button
# pyautogui.click() # click to open '格式'
# pyautogui.moveTo(532, 676, duration=0.3) # move to the 'JPEG' button
# pyautogui.click() # click to open 'JPEG'
# pyautogui.moveTo(791, 841, duration=0.3) # move to the '选取' button
# pyautogui.click() # click to open '选取'









