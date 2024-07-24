from load_image import ft_load
from matplotlib import pyplot as plt


def ft_invert(array: list) -> list:
    """Invert the colors of the image received."""
    array_cpy = array.copy()
    array_cpy = 255 - array_cpy
    plt.imshow(array_cpy)
    plt.gcf().canvas.manager.set_window_title('Inverted')
    plt.show()
    plt.imsave('./ex05/inverted.jpg', array_cpy)
    return array_cpy


def ft_red(array) -> list:
    """Convert the colors of the image to red."""
    array_cpy = array.copy()
    array_cpy[:, :, [1, 2]] = 0
    plt.imshow(array_cpy)
    plt.gcf().canvas.manager.set_window_title('Red')
    plt.show()
    plt.imsave('./ex05/red.jpg', array_cpy)
    return array_cpy


def ft_green(array) -> list:
    """Convert the colors of the image to green."""
    array_cpy = array.copy()
    array_cpy[:, :, [0, 2]] = 0
    plt.imshow(array_cpy)
    plt.gcf().canvas.manager.set_window_title('Green')
    plt.show()
    plt.imsave('./ex05/green.jpg', array_cpy)
    return array_cpy


def ft_blue(array) -> list:
    """Convert the colors of the image to blue."""
    array_cpy = array.copy()
    array_cpy[:, :, [0, 1]] = 0

    plt.imshow(array_cpy)
    plt.gcf().canvas.manager.set_window_title('Blue')
    plt.show()
    plt.imsave('./ex05/blue.jpg', array_cpy)
    return array_cpy


def ft_gray(array) -> list:
    """Convert the image from rgb to grayscale."""
    array_cpy = array.copy()
    array_cpy = array_cpy / 255
    array_cpy = array_cpy[:, :, 0] * 0.2126 + array_cpy[:, :, 1] * 0.7152\
        + array_cpy[:, :, 2] * 0.0722
    print(array_cpy)
    plt.imshow(array_cpy,  cmap="gray")
    plt.gcf().canvas.manager.set_window_title('Grayscale')
    plt.show()
    plt.imsave('./ex05/grayscale.jpg', array_cpy, cmap="gray")
    return array_cpy


def main():
    img = ft_load("./ex05/grayscale.jpg")
    print(img)
    ft_blue(img)
    ft_green(img)
    ft_red(img)
    ft_gray(img)
    ft_invert(img)


if __name__ == "__main__":
    main()
