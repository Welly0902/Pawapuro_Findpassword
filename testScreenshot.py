import pyautogui
import time
# from PIL import Image

# while 1==1:
#     time.sleep(3)
#     print(pyautogui.position())
time.sleep(3)

region = (709, 460, 480, 150)

screenshot = pyautogui.screenshot(region=region)

target_image = 'screenshot.png'


# screenshot = pyautogui.screenshot()

# time.sleep(5)

# screenshot.save('screenshot.png')
# screenshot2 = pyautogui.screenshot()

location = pyautogui.locate(target_image, screenshot)

# print(location)
if location:
    print("Target image found at location:", location)
else:
    print("Target image not found on the screen.")