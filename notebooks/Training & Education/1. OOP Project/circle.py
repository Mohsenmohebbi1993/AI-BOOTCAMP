from base import Shape

class Circle(Shape):

    def __init__(self, redius):
        if redius < 0:
            raise ValueError("Redius cannot be negative")
        self.redius = redius

    
    def area(self):
        return self.redius * self.redius * 3.14159