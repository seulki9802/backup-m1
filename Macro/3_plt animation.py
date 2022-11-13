import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cv2


imgs = ['교독문', '예배순서', '인트로', '찬송가', '찬양팀']
fig, ax = plt.subplots()


def update(i):
    img = cv2.imread('./Macro/{}.png'.format(imgs[i%len(imgs)]))
    img = np.array(img)
    ax.imshow(img)


ani = FuncAnimation(fig, update)
plt.show()