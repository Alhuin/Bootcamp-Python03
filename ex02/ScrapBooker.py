import numpy as np
import parent_import
from ex01.ImageProcessor import ImageProcessor as imp
from ex00.NumPyCreator import NumPyCreator as npc


class CropError(Exception):
    def __init__(self, message):
        self.message = f"CropError: {message}"


class ScrapBooker:
    @staticmethod
    def crop(array, dimensions, position=(0, 0)):
        """ crops the image as a rectangle with the given dimensions,
        whose top left corner is given by the position parameter """
        if dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1]:
            raise CropError("Dimensions are too big to match the array.")
        elif 0 <= position[0] <= array.shape[0] \
                and 0 <= position[0] <= array.shape[1]:
            return np.array(
                array[
                    position[0]:position[0] + dimensions[0],
                    position[1]:position[1] + dimensions[1]
                ]
            )
        raise CropError("Position out of array.")

    @staticmethod
    def thin(array, n, axis):
        """ deletes every n-th pixel row along the specified axis
        (0 vertical, 1 horizontal) """
        axis = 1 if axis == 0 else 0
        to_delete = [
            i
            for i in range(array.shape[axis])
            if (i + 1) % n == 0
        ]
        return np.delete(array, to_delete, axis)

    @staticmethod
    def juxtapose(array, n, axis):
        """ juxtaposes n copies of the image along the specified axis
        (0 vertical, 1 horizontal)."""
        ret = array.copy()
        for i in range(n - 1):
            ret = np.concatenate((ret, array), axis)
        return ret

    @staticmethod
    def mosaic(array, dimensions):
        """ makes a grid of dimensions (h x w) with multiple copies of the
        array """
        return np.tile(array, dimensions)


def main():
    arr = imp.load("../resources/42AI.png")
    sc = ScrapBooker()
    # croped = sc.crop(arr, (150, 150), (50, 50))
    # imp.display(croped)
    # b = sc.thin(a, 2, 0)
    # b = sc.juxtapose(a, 1, 0)
    # b = sc.mosaic(a, (4, 20))
    # print(b)
    t1 = np.array([
        ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A"],
        ["B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B", "B"],
        ["C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C", "C"],
        ["D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D", "D"],
        ["E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"],
        ["F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F"],
        ["G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G", "G"],
        ["H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H", "H"],
        ["I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I", "I"],
        ["J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J", "J"],
    ])
    print(t1)
    print(t1.shape)
    t2 = sc.thin(t1, 4, 0)
    print(t2)
    print(t2.shape)
    t3 = sc.thin(t1, 4, 1)
    print(t3)
    print(t3.shape)
    pass


if __name__ == "__main__":
    main()
