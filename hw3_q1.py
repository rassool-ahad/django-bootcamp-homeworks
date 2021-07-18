class Triangel():
    def __init__(self, p1: tuple, p2: tuple, p3: tuple) -> None:

        self.__check_input(p1)
        self.__check_input(p2)
        self.__check_input(p3)

        self.__check_triangle(p1, p2, p3)

        self.x1 = p1[0]
        self.y1 = p1[1]
        self.x2 = p2[0]
        self.y2 = p2[1]
        self.x3 = p3[0]
        self.y3 = p3[1]

    @staticmethod
    def __check_input(pos:tuple):
        assert len(pos) == 2
        assert isinstance(pos[0], int)
        assert isinstance(pos[1], int)

    @staticmethod
    def __check_triangle(pos1:tuple, pos2:tuple, pos3:tuple):
        assert pos1 != pos2
        assert pos1 != pos3
        assert pos2 != pos3

    def area(self):
        return abs(0.5*((self.x1 * self.y2) - (self.x2 * self.y1) +
                       (self.x2 * self.y3) - (self.x3 * self.y2) +
                       (self.x1 * self.y1) - (self.x1 * self.y3)))

    def sideslength(self) -> tuple:
        side1 = (((self.x1 - self.x2) ** 2) + ((self.y1 - self.y2) ** 2)) ** 0.5
        side2 = (((self.x2 - self.x3) ** 2) + ((self.y2 - self.y3) ** 2)) ** 0.5
        side3 = (((self.x1 - self.x3) ** 2) + ((self.y1 - self.y3) ** 2)) ** 0.5
        return (side1, side2, side3)

    def perimeter(self):
        sides = self.sideslength()
        return sum(sides)

    def center(self)->tuple:
        return ((self.x1+self.x2+self.x3) / 3,
                (self.y1+self.y2+self.y3) / 3)

    def type(self)->str:
        sides:list = list(self.sideslength())
        maxSideLength = max(sides)
        minSideLength = min(sides)
        sides.remove(maxSideLength)
        sides.remove(minSideLength)
        middleSideLength = sides[0]
        print(maxSideLength)
        print(minSideLength)
        print(middleSideLength)
        if maxSideLength==minSideLength==middleSideLength:
            return 'Equilateral'
        elif maxSideLength==middleSideLength!=minSideLength or middleSideLength==minSideLength!=maxSideLength:
            return 'isosceles'

        elif maxSideLength**2 == (minSideLength**2) + (middleSideLength**2):
            return 'right angle'
        else:
            return 'i can definitely say its not Equilateral or isosceles or right angle'

m = Triangel((0,0),(2,0),(0,1))
print(m.area())
print(m.center())

print(m.perimeter())
print(m.type())




