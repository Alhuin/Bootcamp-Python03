import numpy as np


class CreationException(Exception):
    def __init__(self, message):
        self.message = f"Creation Error: {message}"


class NumPyCreator:
    @staticmethod
    def from_list(lst, dtype=None):
        if isinstance(lst, list):
            return np.array(lst, dtype=dtype)
        raise CreationException("from_list() must take a list as parameter, "
                                f"got {type(lst)}.")

    @staticmethod
    def from_tuple(tpl, dtype=None):
        if isinstance(tpl, tuple):
            return np.array(tpl, dtype=dtype)
        raise CreationException("from_tuple() must take a tuple as parameter, "
                                f"got {type(tpl)}.")

    @staticmethod
    def from_iterable(itr, dtype=None):
        if isinstance(itr, range):
            return np.array(itr, dtype)
        raise CreationException("from_iterable() must take a range as "
                                f"parameter, got {type(iter)}.")

    @staticmethod
    def from_shape(shape, value=0, dtype=None):
        if isinstance(shape, tuple):
            return np.full(shape, value, dtype=dtype)
        raise CreationException("from_shape() must take a tuple as first "
                                f"parameter, got {type(shape)}.")

    @staticmethod
    def random(shape):
        if isinstance(shape, tuple):
            return np.random.rand(*[arg for arg in shape])
        raise CreationException("random() must take a tuple as parameter, "
                                f"got {type(shape)}.")

    @staticmethod
    def identity(n):
        if isinstance(n, int):
            return np.identity(n)
        raise CreationException("identity() must take an integer as "
                                f"parameter, got {type(n)}")


def main():
    NC = NumPyCreator()
    # np_array = NC.from_list(([1, 2], [3, 4]), float)
    # np_array = NC.from_tuple(["a", "b"], str)
    np_array = NC.from_iterable(range(5), dtype=int)
    # np_array = NC.from_shape((4, 2, 8), 5, dtype=float)
    # np_array = NC.random((4, 2, 2))
    # np_array = NC.identity(4)
    print(np_array)
    print(f"Dimensions: {np_array.ndim}")
    print(f"Shape: {np_array.shape}")
    print(f"Size: {np_array.size}")
    print(f"DataType: {np_array.dtype}")
    print(f"ItemsSize: {np_array.itemsize} bites by element")
    print(f"Data: {np_array.data}")


if __name__ == "__main__":
    main()
