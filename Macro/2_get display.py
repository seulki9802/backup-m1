from PIL import ImageGrab, Image
import pyautogui

x, y = pyautogui.position() 

img = ImageGrab.grab((x-50, y-50, x+50, y+50))
w, h = img.size[0] / 10, img.size[1] / 10
print(x, y)
print(img.size)
# img = img.crop((x, y, x+100, y+100))
img.show()
# while 1:
#     print(img.size)

#     print(pyautogui.position())