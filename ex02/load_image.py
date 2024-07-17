import imageio.v2 as lio


def ft_load(path: str) -> tuple:
    try:
        if not isinstance(path, str):
            raise TypeError("TypeError: path parameter must be of str type")
        img = lio.imread(path)
    except (FileNotFoundError, ValueError, PermissionError) as msg:
        print(type(msg).__name__ + ":", msg)
        return None

    print("The shape of the image is:", img.shape)
    return img


def main():
    print(ft_load("./ex02/image.png"))
    print(ft_load("./ex02/image.jpg"))
    print(ft_load("./ex02/corrupted.jpg"))
    print(ft_load("./ex02/permission.jpg"))


# if __name__ == "__main__":
#     main()
