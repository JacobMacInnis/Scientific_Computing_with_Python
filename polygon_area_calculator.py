class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width >50 or self.height > 50:
            return 'Too big for picture.'

        picture = ''
        for index in range(self.height):
            picture += '*' * self.width    
            picture += '\n'
        return picture


    def get_amount_inside(self, other_shape):
        fit_width = self.width // other_shape.width
        fit_height = self.height // other_shape.height

        return fit_width * fit_height
        

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, new_width):
        self.width = new_width
        self.height = new_width

    def set_height(self, new_height):
        self.height = new_height
        self.width = new_height

square = Square(5)
print(square)
print(square.get_picture())
rectangle = Rectangle(15,10)

print(rectangle.get_picture())
print(rectangle.get_amount_inside(square))
