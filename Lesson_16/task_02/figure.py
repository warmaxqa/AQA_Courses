from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def calculate_perimetr(self):
        ...
    @abstractmethod
    def calculate_square(self):
        ...
