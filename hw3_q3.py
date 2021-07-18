class Book:
    numberofbooks = 0

    def __init__(self, name: str, price: int, number: int) -> None:
        self.name = name
        self.price = price
        self.number = number
        Book.numberofbooks += number

    def __repr__(self) -> str:
        return f'book name: {self.name} \nprice: {self.price} \nnumber: {self.number}'

    @classmethod
    def nummberofallbooks(cls) -> int:
        return f'number of all books is {cls.numberofbooks}'


a = Book('ra',200,2)
print(a)
b = Book('ra',200,2)
print(Book.nummberofallbooks())