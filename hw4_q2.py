from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @staticmethod
    def concat_area(*rectangles):
            area = 0
            for _ in rectangles:
                area += _.perimeter
            return area


class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def __call__(self,length):
       self.length = length

    @property
    def perimeter(self):
        return (2*self.width)+(2*self.length)

    @property
    def area(self):
        return self.width*self.length


class Quadrilateral(Shape):
    def __init__(self,side) -> None:
        self.side = side

    @property
    def perimeter(self):
        return 4*self.side

    @property
    def area(self):
        return self.side**2

    @staticmethod
    def draw_contact(quadrilateral_list: list):
        for lines in range( max(quadrilateral_list)):
            for _ in quadrilateral_list:
                if lines < _:
                    print('* '*_, sep='', end='')
                else:
                    print('  '*_, sep='', end='')
            print()


# rec = Rectangle(5, 2)
rec2 = Rectangle(6, 3)
rec2(3)
# print(rec.perimeter)
# print(Shape.concat_area(rec, rec2))
# Quadrilateral.draw_contact([0, 2, 3,4, 5, 6, 7, 8])

