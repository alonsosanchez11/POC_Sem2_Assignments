class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        if(base < 0):
            self.__base = 0
        else:       
            self.__base = base
            
        if(height < 0):
            self.__height = 0
        else:
            self.__height = height
        
    def get_height(self) -> float:
        return self.__height
    
    def get_base(self)-> float:
        return 1 * self.__base + 1 * self.__height
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self) -> float:
        return 3 * self.__base + 3 * self.__height

    def __str__(self) -> str:
        return "Rectangle with base:" + str (self.__base) + ", height:" + str (self.__height)

class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)
        self.__side = side

    def get_side(self) -> float:
        return self.__side
    
    def __str__(self) -> str:
        return "Sqaure with side length:" + str(self.__side)


square1 = Square(3)
print(square1)
print("The area of square1 is", square1.get_area())
print("The perimeter of square1 is", square1.get_perimeter())
print("The side length of sqaure1 is", square1.get_side())