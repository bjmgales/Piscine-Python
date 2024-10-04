import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)
    active: bool = field(default=True, init=False)

    def __post_init__(self):
        self.login = self.name[0] + self.surname
    # def __init__(self, **kwargs):
    #     for key in kwargs:
    #         if key not in {'name', 'surname'}:
    #             raise TypeError("Student.__init__() got an " +
    #                             f"unexpected keyword argument '{key}'")
    #     if {'name', 'surname'} not in kwargs:
    #         raise TypeError("Student.__init__() await " +
    #                         "name and surname")

    #     self.active = True
    #     if "name" in kwargs:
    #         self.name = kwargs.name
    #     if "surname" in kwargs:
    #         self.surname = kwargs.surname

    #     self.login = kwargs.name[0] + kwargs.surname
    #     self.id = generate_id()


def main():
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)


if __name__ == "__main__":
    main()
