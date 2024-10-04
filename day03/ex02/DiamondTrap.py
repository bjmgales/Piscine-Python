from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Concrete class: King.

    Initializes a King with a name and alive status.

    Parameters:
        `first_name: str` The first name of the character. \
This is a mandatory argument.
        `is_alive: bool [optional), default = False]` \
Indicates whether the character is alive.
    """
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        super().__init__(first_name, is_alive)

    def get_hairs(self):
        """Get the King eyes color."""
        return self.hairs

    def get_eyes(self):
        """Get the King hairs color."""
        return self.eyes

    def set_eyes(self, color):
        """Set the King eyes color."""
        self.eyes = color

    def set_hairs(self, color):
        """Set the King hairs color."""
        self.hairs = color


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)

if __name__ == "__main__":
    main()
