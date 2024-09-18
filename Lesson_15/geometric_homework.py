import math

class Rhombus:
    def __init__(self, side_a, angle_a):
        self.setattr('side_a', side_a)
        self.setattr('angle_a', angle_a)

    def setattr(self, name, value):
        if name == 'side_a':
            if value <= 0:
                raise ValueError("The side of the rhombus must be greater than 0")
            self.__dict__[name] = value

        elif name == 'angle_a':
            if not (0 < value < 180):
                raise ValueError("The angle of the rhombus must be between 0 and 180 degrees")
            self.__dict__[name] = value
            self.__dict__['angle_b'] = 180 - value

    def __repr__(self):
        return f"Rhombus(side_a={self.side_a}, angle_a={self.angle_a}, angle_b={self.angle_b})"

rhombus = Rhombus(5, 60)
print(rhombus)