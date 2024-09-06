from Lesson_16.task_02.figure import Figure


class Rectangle(Figure):
    __rectangle_a: int
    __rectangle_b: int

    def __init__(self, rectangle_a: int, rectangle_b: int):
        self.__rectangle_a = rectangle_a
        self.__rectangle_b = rectangle_b

    def calculate_perimetr(self):
        return (self.__rectangle_a * 2) * (self.__rectangle_b * 2)

    def calculate_square(self) -> int:
        return self.__rectangle_a * self.__rectangle_b
