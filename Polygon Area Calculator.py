# This class stores the width and height of a rectangle instance, and
# can calculate its diagonal length, its area and perimeter. It can
# also return a visual representation of the rectangle, and it returns
# how many times a particular shape can fit into it.
class Rectangle:

    # A width and height is passed into a rectangle object when it is
    # created.
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # A setter method to change the width of the rectangle.
    def set_width(self, new_width):
        self.width = new_width

    # A setter method to change the height of the rectangle.
    def set_height(self, new_height):
        self.height = new_height

    # Returns the area of the rectangle.
    def get_area(self):
        return self.width * self.height

    # Returns the perimeter of the rectangle.
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # Returns the length of the diagonal of the rectangle.
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # Displays a visual representation of the rectangle using '*'s.
    # The number of '*'s on each line is the width, and the number of
    # lines is the height.
    def get_picture(self):
        # Does not display the picture if the width and/or height is
        # greater than 50.
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        # This stores the string representation of the shape, with each
        # line separated by a '\n'.
        picture = ""
        # Keeps track of the height number
        height_num = 1
        while height_num <= self.height:
            picture += "*" * self.width + "\n"
            height_num += 1

        return picture

    # This takes in a shape, and it returns how many times that shape
    # can be fitted into this shape (without rotations) by using the
    # area of each shape.
    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    # This displays the rectangle's width and height when the object is
    # called by itself.
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"


# This inherits the methods of the Rectangle class.
class Square(Rectangle):

    # A length is passed into a square object when it is created. The
    # width and height are the same.
    def __init__(self, length):
        self.width = length
        self.set_width_to_height()

    # This method changes the side length of the square with the new
    # length.
    def set_side(self, new_length):
        self.width = new_length
        self.set_width_to_height()

    # Overrides the parent method. Sets both the width and height to the
    # new length.
    def set_width(self, new_length):
        self.width = new_length
        self.set_width_to_height()

    # Overrides the parent method. Sets both the width and height to the
    # new length.
    def set_height(self, new_length):
        self.width = new_length
        self.set_width_to_height()

    # A method that sets the height of the square to its width. Used to
    # avoid repetition of code.
    def set_width_to_height(self):
        self.height = self.width

    # This displays the square's side length when the object is called 
    # by itself.
    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    

# TESTS

rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)
rect.get_picture()

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
