from matplotlib import pyplot as plt
from load_image import ft_load_gs
import numpy as np


def ft_transpose(array: list):
    """Rotate the received image by 90° to the right."""
    transposed = [[0 for _ in range(len(array))] for _ in range(len(array[0]))]

    for y in range(len(array)):
        for x in range(len(array[y])):
            transposed[y][x] = array[x][y]
    return transposed


def ft_zoom(path: str):
    """Zoom (more like crop, but hey subject) image of size\
        400x400 and on path ending with \"animal.jpeg\""""
    try:
        img = ft_load_gs(path)
        if img is None:
            return None
        assert img.shape[0] == 400 and img.shape[1] == 400 \
            and path.endswith("animal.jpeg"), \
            "as stated by this great subject," \
            " image should be \"animal.jpeg\" with a size of 400x400"
        print("The shape of the image is:", img.shape, '\n', img)
        center_y, center_x = img.shape[0] // 2, img.shape[1] // 2
        crop_size = 200
        img = img[center_y - crop_size:center_y + crop_size,
                  center_x - crop_size:center_x + crop_size]
        img = np.array(ft_transpose(img))
        print("New shape after transpose:", img.shape)
        print(img)
        plt.imshow(img, cmap="gray")
        plt.show()
        plt.imsave('./ex04/transposed.jpeg', img, cmap="gray")
    except Exception as err:
        print(type(err).__name__ + ':', err)
    return img


def main():
    ft_zoom("./ex04/animal.jpeg")


if __name__ == "__main__":
    main()
