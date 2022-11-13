import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import ImageGrab
import pyautogui
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

fig, ax = plt.subplots()


def update(i):
    x, y = pyautogui.position()
    img = ImageGrab.grab((x-50, y-10, x+50, y+10))
    txt = pytesseract.image_to_string(img, lang='eng')
    ax.imshow(img)
    plt.title(txt)

ani = FuncAnimation(fig, update)
plt.show()