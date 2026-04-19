from rectangle import Rectangle
from circle import Circle

list_of_shape = [(Rectangle, (3, 4)), (Circle, (5,)), (Rectangle, (-2, 5))]

for ctor, arge in list_of_shape:
    shape = ctor(*arge)
    print(f"The area of The {shape.__class__.__name__} is : {shape.area():.2f}")