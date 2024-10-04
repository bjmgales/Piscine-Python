from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract class: Character.

    Blueprint for character creation objects with a name and a living status.
    It cannot be instantiated directly.

    Parameters:
        first_name (str): The first name of the character. \
            Defaults to an empty string.
        is_alive (bool): The living status of the character. \
            Defaults to True.
    """
    def __init__(self, first_name: str = "", is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Method to set is_alive to False.
        This method must be implemented by all subclasses."""
        pass


class Stark(Character):
    """
    Concrete class: Stark.

    Initializes a Stark character with a name and alive status.

    Parameters:
        `first_name: str` The first name of the character. \
This is a mandatory argument.
        `is_alive: bool [optional), default = False]` \
Indicates whether the character is alive.
    """

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Construct Concrete Class using Parent Class __Init__()

        The usage of super() protect the class from wrong instanciations \
such as `Ned = Stark()"
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """set self.is_alive to false"""
        self.is_alive = False
