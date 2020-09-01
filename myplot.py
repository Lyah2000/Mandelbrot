import numpy as np
import matplotlib.pyplot as plt

def plot(arr_x50, arr_y50, c50, arr_x30, arr_y30, c30, arr_x20, arr_y20, c20, arr_x10, arr_y10, c10, arr_x5, arr_y5, c5):
    fig, ax = plt.subplots()
    plt.scatter(arr_x50, arr_y50, s = 5, marker = ".", c = c50)
    plt.scatter(arr_x30, arr_y30, s = 5, marker = ".", c = c30)
    plt.scatter(arr_x20, arr_y20, s = 5, marker = ".", c = c20)
    plt.scatter(arr_x10, arr_y10, s = 5, marker = ".", c = c10)
    plt.scatter(arr_x5, arr_y5, s = 5, marker = ".", c = c5)
    ax.grid() #добавляет сетку
    plt.show()