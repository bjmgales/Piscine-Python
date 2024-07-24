import numpy as np
import imageio.v2 as lio


def ft_load(path: str) -> tuple:
    """Load image as a numpy array"""
    try:
        if not isinstance(path, str):
            raise TypeError("TypeError: path parameter must be of str type")
    except Exception as err:
        print(type(err).__name__ + ":", err)
        return None
    array = np.array(lio.imread(path))
    print("The shape of the image is:", array.shape)
    print(array)
    return array
