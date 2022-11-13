import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import ImageGrab
import pyautogui


fig, ax = plt.subplots()


def update(i):
    x, y = pyautogui.position()
    img = ImageGrab.grab((x-100, y-100, x+100, y+100))

    ax.imshow(img)

ani = FuncAnimation(fig, update)
plt.show()