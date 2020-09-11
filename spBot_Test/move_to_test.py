import subprocess
import pyautogui
import time


def cmd_stats(command):
    p = subprocess.Popen(["start", "cmd", "/k", "{}".format(command)], shell=True)
    p.wait(1)


counter = 10000
x = 0
while x <= counter:
    x += 1
    if x > counter:
        print('--->Complete')
    print('{} of {}'.format(x, counter))
    pyautogui.moveTo(900, 900, duration=1)
    pyautogui.doubleClick()
    pyautogui.moveTo(890, 900, duration=1)
    pyautogui.doubleClick()
    pyautogui.moveTo(870, 900, duration=1)
    pyautogui.doubleClick()
    print('Sleeping..........')
    time.sleep(10)
