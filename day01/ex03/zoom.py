from matplotlib import pyplot as plt
from load_image import ft_load_gs


def ft_zoom(path: str):
    """Zoom (more like crop, but hey subject) image of size\
        400x400 and on path ending with \"animal.jpeg\""""
    try:
        img = ft_load_gs(path)
        if img is None:
            return None
        assert img.shape[0] == 768 and img.shape[1] == 1024 \
            and path.endswith("animal.jpeg"), \
            "as stated by this great subject," \
            " image should be \"animal.jpeg\" with a size of 768x1024"
        center_y, center_x = img.shape[0] // 2, img.shape[1] // 2
        crop_size = 200
        img = img[center_y - crop_size:center_y + crop_size,
                  center_x - crop_size:center_x + crop_size]
        print("New shape after slicing:", img.shape)
        print(img)
        plt.imshow(img, cmap="gray")
        plt.show()
        plt.imsave('./ex03/zoomed.jpeg', img, cmap="gray")
    except Exception as err:
        print(type(err).__name__ + ':', err)
    return img


def main():
    ft_zoom("./ex03/animal.jpeg")


if __name__ == "__main__":
    main()
