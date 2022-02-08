import matplotlib.pyplot as plt
import numpy as np
import cv2


def plot_unit_circle():
    angs = np.linspace(0, 2 * np.pi, 10**6)
    rs = np.zeros_like(angs) + 1
    xs = rs * np.cos(angs)
    ys = rs * np.sin(angs)
    plt.plot(xs, ys)


def mouse_move(event):
    x, y = event.xdata, event.ydata
    print(x, y)


plt.connect('motion_notify_event', mouse_move)
image = cv2.imread('/Users/georgychernousov/visualize_dot_work/cloud/cloud.tif')
plt.imshow(image)
plt.axis('equal')
plt.show()
