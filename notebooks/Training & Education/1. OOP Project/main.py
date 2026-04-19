from rectangle import Rectangle
from circle import Circle

list_of_shape = [(Rectangle, (3, 4)), (Circle, (5,)), (Rectangle, (-2, 5)), (Circle, (-10,))]

for ctor, arge in list_of_shape:
    try:
        shape = ctor(*arge)
        print(f"The area of The {shape.__class__.__name__} is : {shape.area():.2f}")

    except ValueError as e:
        print(f"Error create {ctor.__name__} with arge {arge}: {e}")
        continue

    