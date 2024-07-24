import imageio.v2 as lio


def ft_load_gs(path: str) -> tuple:
    """Load image as a numpy array"""
    try:
        if not isinstance(path, str):
            raise TypeError("TypeError: path parameter must be of str type")
        img = lio.imread(path)
        print("The shape of the image is:", img.shape, '\n', img)
    except Exception as err:
        print(type(err).__name__ + ":", err)
        return None

    return lio.imread(path, pilmode='L')
