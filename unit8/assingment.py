class Rectangle:
    
    __counter = 0

    def get_count():
        return Rectangle.__counter
    
    def __init__(self, base: float, height: float) -> None:
        if(base < 0):
            self.__base = 0
        else:       
            self.__base = base
            
        if(height < 0):
            self.__height = 0
        else:
            self.__height = height

        Rectangle.__counter += 1
    
    def get_height(self) -> float:
        return self.__height
    
    def get_base(self)-> float:
        return 1 * self.__base + 1 * self.__height
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self) -> float:
        return 3 * self.__base + 3 * self.__height

 
rectangle_1 = Rectangle(5,10)
print("The base of the rectangle is", rectangle_1.get_base())
print("The height of the rectangle is", rectangle_1.get_height())
print("The perimeter of the rectangle is", rectangle_1.get_perimeter())
print("The area of the rectangle is", rectangle_1.get_area())

rectangle_2 = Rectangle(1, 6)
print("The base of the rectangle is", rectangle_2.get_base())
print("The height of the rectangle is", rectangle_2.get_height())
print("The perimeter of the rectangle is", rectangle_2.get_perimeter())
print("The area of the rectangle is", rectangle_2.get_area())

print("The counting, I guess? Of Rectangles is", Rectangle.get_count())