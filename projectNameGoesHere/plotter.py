#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

from projectNameGoesHere import utils

default_argv = {
    'resolution': 500,
    'frames': 300,
    'pause': 0.001,
}


class Plotter:
    def __init__(self):
        self.fig, self.ax = plt.subplots(2, 1, figsize=(6,4))
        self.lines = [None, None]
        for i in range(2):
            self.lines[i], = self.ax[i].plot([], [])
            self.ax[i].set_xlim(0,10)
            self.ax[i].set_ylim(-1,1)
        plt.pause(0.1)


    def update(self, x, y, subplot=0, pause=0.1):
        self.lines[subplot].set_data(x, y)
        plt.pause(pause)


def main(resolution=100, frames=30, pause=0.1):
    plotter = Plotter()
    x = np.linspace(0, 10, resolution)
    for f in range(frames):
        cosx = np.cos(2*np.pi*(0.01*f)*x)
        sinx = np.sin(2*np.pi*(0.01*f)*x)
        plotter.update(x, sinx, subplot=0, pause=pause)
        plotter.update(x, cosx, subplot=1, pause=pause)


if __name__ == "__main__":
    argv = utils.argparse_wrapper(default_argv, sys.argv)
    main(**default_argv)