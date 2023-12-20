import pyautogui
import time

while 1==1:
    time.sleep(3)
    print(pyautogui.position())
    # print(pyautogui.position().x) # 
    # pyautogui.leftClick(x=1121, y=667) 
    
    # click type bar: x=934, y=519
    pyautogui.leftClick(x=934, y=519)

    # type word x=1023 y=554
    time.sleep(0.5)
    pyautogui.leftClick(x=1023, y=554)
    message = "1234"
    pyautogui.typewrite(message, interval=0.25)

    # click ok: x=1274, y=615
    time.sleep(0.5)
    pyautogui.leftClick(x=1274, y=615)

    # click comfirm x=1121 y=667
    time.sleep(0.5)
    pyautogui.leftClick(x=1121, y=667)

    # click x: x=1303, y=479
    time.sleep(0.5)
    pyautogui.leftClick(x=1303, y=479)



    # click type bar: x=934, y=519
    # pyautogui.leftClick(x=934, y=519)