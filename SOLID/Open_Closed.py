# Wrong

class ShapeCalculator:
    def calculate_area(self, shape):
        if shape.type == "rectangle":
            return shape.width * shape.height
        elif shape.type == "circle":
            return 3.14 * (shape.radius ** 2)

    def calculate_perimeter(self, shape):
        if shape.type == "rectangle":
            return 2 * (shape.width + shape.height)
        elif shape.type == "circle":
            return 2 * 3.14 * shape.radius


# Correct

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

# Similarly create classes for other shapes
