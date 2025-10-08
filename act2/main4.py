from abc import ABC, abstractmethod

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def area(self):
        return self.width ** 2

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.height = height
        self.width = width
    
    def area(self):
        return self.width * self.height * 0.5
