import pyautogui
import time

start_time = time.time()

c = 'abcdefghijklmnopqrstuvwxyz0123456789'
ctr = 0 

region = (709, 460, 480, 150)



target_image = 'screenshot.png'
target_message = ''

try:
    for i in range(len(c)):
        for j in range(len(c)):
            for k in range(len(c)):
                for l in range(len(c)):
                    # print(c[i] + c[j] + c[k] + c[l])
                    ctr += 1
                    message = c[i] + c[j] + c[k] + c[l]
                    time.sleep(1.5)
                    # print(pyautogui.position())
                    # print(pyautogui.position().x) # 
                    # pyautogui.leftClick(x=1121, y=667) 
                    
                    # click type bar: x=773, y=522
                    pyautogui.leftClick(x=773, y=522)

                    # type word x=753, y=560
                    time.sleep(0.5)
                    pyautogui.leftClick(x=753, y=560)
                    # message = "1234"
                    pyautogui.typewrite(message, interval=0.25)

                    # click ok: x=1111, y=614
                    time.sleep(0.5)
                    pyautogui.leftClick(x=1111, y=614)

                    # click comfirm x=940, y=662
                    time.sleep(0.5)
                    pyautogui.leftClick(x=940, y=662)

                    time.sleep(2)
                    print(f"Try password: {message}")
                    target_message = message
                    screenshot = pyautogui.screenshot(region=region)
                    # screenshot.save("s.png")
                    location = pyautogui.locate(target_image, screenshot)

                    # click x: x=1144, y=481
                    time.sleep(0.5)
                    pyautogui.leftClick(x=1144, y=481)

except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
except pyautogui.ImageNotFoundException:
    print(f"Find password: {target_message}")
finally:
    end_time = time.time()

    runtime = end_time - start_time
    print(f"The program run {ctr} times")
    print(f"The program took {runtime} seconds to run.")
    # click type bar: x=934, y=519
    # pyautogui.leftClick(x=934, y=519)