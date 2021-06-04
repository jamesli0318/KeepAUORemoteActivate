import mouse    # pip install mouse
import pygetwindow as gw    # pip install pygetwindow
import time

AUORemoteWindow = gw.getWindowsWithTitle('iconnectts2.auo.com')[0]

while(1):
    if AUORemoteWindow.isMaximized:
        print("Working from home now")
    else:
        AUORemoteWindow.maximize()
        mouse.right_click()
        time.sleep(0.5)
        AUORemoteWindow.minimize()
    time.sleep(600)
