class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @property
    def area(self):
        return self._width * self._height
    
class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
    
# rect = Rectangle(4, 5)

# print(rect.width == 4)        # True
# print(rect.height == 5)       # True
# print(rect.area == 20)        # True

square = Square(5)
print(square.area == 25)      # True