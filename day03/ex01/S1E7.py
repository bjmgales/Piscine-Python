from S1E9 import Character


class Baratheon(Character):
    """
    Concrete class: Baratheon.

    Initializes a Baratheon character with a name and alive status.

    Parameters:
        `first_name: str` The first name of the character. \
This is a mandatory argument.
        `is_alive: bool [optional), default = False]` \
Indicates whether the character is alive.
    """

    def __init__(self, firstname: str, is_alive: bool = True):
        super().__init__(firstname, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """User-friendly depiction of the object."""
        return self.__repr__()

    def __repr__(self):
        """User-friendly depiction of the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def create_baratheon(firstname: str, is_alive: bool = True):
        return Baratheon(firstname, is_alive)

    def die(self):
        """set self.is_alive to false"""
        self.is_alive = False


class Lannister(Character):
    """
        Concrete class: Baratheon.

        Initializes a Baratheon character with a name and alive status.

        Parameters:
            `first_name: str` The first name of the character. \
    This is a mandatory argument.
            `is_alive: bool [optional), default = False]` \
    Indicates whether the character is alive.
        """

    def __init__(self, firstname: str, is_alive: bool = True):
        super().__init__(firstname, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """set self.is_alive to false"""
        self.is_alive = False

    def __str__(self):
        """User-friendly depiction of the object."""
        return self.__repr__()

    def __repr__(self):
        """User-friendly depiction of the object."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls,  firstname: str, is_alive: bool = True):
        return cls(firstname, is_alive)


# def main():
#     Robert = Baratheon("Robert")
#     print(Robert.__dict__)
#     print(Robert.__str__)
#     print(Robert.__repr__)
#     print(Robert.is_alive)
#     Robert.die()
#     print(Robert.is_alive)
#     print(Robert.__doc__)
#     print("---")
#     Cersei = Lannister("Cersei")
#     print(Cersei.__dict__)
#     print(Cersei.__str__)
#     print(Cersei.is_alive)
#     print("---")
#     Jaine = Lannister.create_lannister("Jaine", True)
#     print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : \
#           {Jaine.is_alive}")


# if __name__ == "__main__":
#     main()
