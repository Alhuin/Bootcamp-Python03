from matplotlib import image
from matplotlib import pyplot as plt
from pathlib import Path
import numpy as np


class ImageProcessor:
    @staticmethod
    def load(path):
        """ Load an image from path and return the corresponding np array"""
        print("path", path)
        print(Path(path).is_file())
        if Path(path).is_file():
            img = image.imread(path)
            print(f"Loading image of dimensions {img.shape[0]} x "
                  f"{img.shape[1]}")
            return np.array(img)
        raise FileNotFoundError

    @staticmethod
    def display(array):
        """ Diplay an image from a numpy array """
        if isinstance(array, np.ndarray):
            plt.imshow(array)
            plt.show()
        else:
            raise TypeError("display() needs a numpy ndarray as parameter, "
                            f"got {type(array)}")


def main():
    ip = ImageProcessor()
    arr = ip.load('../resources/42AI.png')
    print(arr)
    ip.display(arr)


if __name__ == "__main__":
    main()
