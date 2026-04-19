from base import Shape

class Rectangle(Shape):

    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("width and height cannot be negative")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height