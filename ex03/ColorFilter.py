import numpy as np
import parent_import
from ex01.ImageProcessor import ImageProcessor as imp


def find_nearest(thresold_lst, colors, n):
    for i, color in enumerate(colors):
        for thresold in thresold_lst:
            if -1/(n * 2) <= thresold - color <= 1/(n*2):
                colors[i] = thresold
    return colors


class ColorFiler:
    @staticmethod
    def invert(array):
        """ Takes a NumPy array of an image as an argument and returns an
        array with inverted color. """
        return 1 - array

    @staticmethod
    def to_blue(array):
        """ Takes a NumPy array of an image as an argument and returns an
        array with a blue filter. """
        return np.array([
            [
                [0, 0, array[i][j][2]]
                for j in range(array.shape[1])
            ]
            for i in range(array.shape[0])
        ])

    @staticmethod
    def to_green(array):
        """ Takes a NumPy array of an image as an argument and returns an
        array with a green filter. """
        return array * [0, 1, 0]

    @staticmethod
    def to_red(array):
        """ Takes a NumPy array of an image as an argument and returns an
        array with a red filter. """
        return array - ColorFiler.to_green(array) - ColorFiler.to_blue(array)

    @staticmethod
    def to_celluloid(array, n=4):
        """ Takes a NumPy array of an image as an argument, and returns an
        array with a celluloid shade filter. """
        copy = array * 1
        thresolds = np.linspace(0, 1, num=n)
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                copy[i][j] = find_nearest(thresolds, array[i][j], n)
        return copy


def main():
    arr = imp.load("../resources/elon_muskito.png")
    cf = ColorFiler()
    # img = cf.invert(arr)
    # img = cf.to_blue(arr)
    # img = cf.to_green(arr)
    # img = cf.to_red(arr)
    # print(arr)
    # img = np.mean(arr, axis=2)
    img = cf.to_celluloid(arr)
    # print(img)
    imp.display(img)


if __name__ == "__main__":
    main()
