#python3

#-*- coding: utf-8 -*-
import pyautogui
import os
import time
import pygetwindow as gw

#import re

ra_location = "C:\\Program Files\\RadiAntViewer64bit\\RadiAntViewer.exe"


#第一步： 创建文件夹

inds = []
month = ''
date = ''

with open("D:/testpyaugogui/ID2.txt") as info:
    for line in info:
        line = line.strip()
        array = line.split()
        # print(array[0])
        # print(array[1])
        
        # folder1 = "D:/Dicom/%s" % (array[1])
        # if not os.path.exists(folder1):
            # os.mkdir(folder1)
        
        # folder2 = "D:/Dicom/%s/%s" % (array[1],array[2])
        # if not os.path.exists(folder2):
            # os.mkdir(folder2)
        
        folder3 = "D:/Dicom/%s/%s/%s" % (array[1],array[2],array[0])
        if not os.path.exists(folder3):
            os.mkdir(folder3)
        
        month = array[1]
        date = array[2]
        inds.append(array[0])


#ind = '124526'
# 第二步：打开软件RA
## RA位置在（36，770)

##返回桌面
pyautogui.hotkey('win', 'd') 

x=36
y=770
num_seconds=1
os.popen(ra_location)
#pyautogui.moveTo(x, y, duration=num_seconds)
#pyautogui.doubleClick() # 打开软件
# pyautogui.click()
# pyautogui.hotkey('win', 'up')
windowTitle = 'RadiAnt DICOM Viewer 4.6.9 (64-bit) - evaluation version - go to https://radiantviewer.com/store/ for paid licenses'

time.sleep(1)
notepadWindow = gw.getWindowsWithTitle(windowTitle)[0]
notepadWindow.maximize()

for ind in inds:
    # 第三步：导入图片

    ## 打开导入快捷键ctrl+shift+o
    pyautogui.hotkey('ctrl', 'shift','o')

    ## 获得焦点
    x=880
    y=500
    pyautogui.moveTo(x, y, duration=num_seconds)
    pyautogui.click()

    ## 按一下tab,并删除
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('backspace')


    ## 输入图片所在文件夹的绝对路径
    inputdir = "D:\\GuigangCT\\Data\\%s\\%s" % (month, ind)

    pyautogui.write(inputdir, interval=0.05)
    pyautogui.press('enter')

    time.sleep(30)

    ## 获得第二幅图
    x=77
    y=351
    pyautogui.moveTo(x, y, duration=num_seconds)
    pyautogui.click()

    # 第四步：导出图片为DICOM格式

    ## 选择格式
    pyautogui.hotkey('ctrl','e')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('right')
    pyautogui.press('tab')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('right')
    pyautogui.press('enter')

    ## 输出保存路径
    time.sleep(1)
    
    ### 获得焦点
    x=880
    y=500
    pyautogui.moveTo(x, y, duration=num_seconds)
    pyautogui.doubleClick(interval=1)
    
    ### 按一下tab,并删除
    time.sleep(5)
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('backspace')

    ### 输出图片所在文件夹的绝对路径
    time.sleep(5)
    outputdir = "D:\\Dicom\\%s\\%s\\%s" % (month, date, ind)

    pyautogui.write(outputdir, interval=0.05)
    pyautogui.press('enter')
    #pyautogui.hotkey('alt','f4')
    time.sleep(5)