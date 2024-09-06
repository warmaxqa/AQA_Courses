from Lesson_16.task_02.figure import Figure
from Lesson_16.task_02.rectangle import Rectangle
from Lesson_16.task_02.square import Square
from Lesson_16.task_02.triangle import Triangle

square_f: Square = Square(10)

rectangle: Rectangle = Rectangle(10, 5)

triangle: Triangle = Triangle(5, 10, 3, 4)

figure_list: list[Figure] = [square_f, rectangle, triangle]

list_tuple_perimetr_and_square: list[tuple[int, object]] = [(figure.calculate_perimetr(), figure.calculate_square()) for
                                                            figure in
                                                            figure_list]

for item in list_tuple_perimetr_and_square:
    print(item[0], item[1])