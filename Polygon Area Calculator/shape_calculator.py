class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = 0
        self.perimeter = 0
        self.diagonal = 0
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = (self.width * self.height)
        return self.area

    def get_perimeter(self):
        self.perimeter = ((self.width * 2) + (self.height * 2))
        return self.perimeter

    def get_diagonal(self):
        self.diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return self.diagonal

    def get_picture(self):
        if self.width <= 50 and self.height <= 50:
            pic_width =''
            pic_height = ''
            for i in range(self.width):
                pic_width += '*'
            
            for i in range(self.height):
                pic_height += (pic_width + chr(10))
            
            return pic_height
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        return (self.width // shape.width) * (self.height // shape.height)

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

        


class Square(Rectangle):
    def __init__(self, height):
        super().__init__(height, height)

    def set_side(self, side):
        self.height = side
        self.width = side

    def __repr__(self):
        return f"Square(side={self.height})"

    def set_height(self, height):
        return super().set_height(height), super().set_width(height)

    def set_width(self, width):
        return super().set_width(width), super().set_height(width)
    
