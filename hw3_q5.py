
class Person():
    def __init__(self, name:str, email:str = "", sex:str = "male" ) -> None:
        self.name = name
        self.email = email
        assert sex == "male" or sex == "female", "sex must be male or female"
        self.sex = sex

    def __repr__(self) -> str:
        return f"name:{self.name}\nemail:{self.email}\nsex:{self.sex}"


class Researcher():
    def __init__(self, person: Person, field: str, university: str="") -> None:
        self.person = person
        self.field = field
        self.university = university
    def __repr__(self) -> str:
        return f"name:{self.person.name}\nemail:{self.person.email}\nsex:{self.person.sex}\nfield:{self.field}"
class Poet():
    def __init__(self,person:Person, type = "") -> None:
        self.person = person
        self.type = type
    def __repr__(self) -> str:
        return f"name:{self.person.name}\nemail:{self.person.email}\nsex:{self.person.sex}\ntype:{self.type}"
class Writer():
    def __init__(self,person:Person, code:int, genre="") -> None:
        self.person = person
        self.code = code
        self.genre = genre
    def __repr__(self) -> str:
        return f"name:{self.person.name}\nemail:{self.person.email}\nsex:{self.person.sex}\ncode:{self.field}\n genre:{self.genre}"
class assar():
    def __init__(self, name, *owners: Person) -> None:

        self.name = name
        self.owners = owners

    def __repr__(self) -> str:
        return f"name:{self.name}\nowners:{self.owners}"




class poem(assar):
    numbers = 0

    def __init__(self, poet: Poet, number, name, poemtype="", *owners) -> None:
       super().__init__(name, *owners)
       self.poet = poet
       self.poemtype = poemtype
       self.number= number
       poem.numbers += number

    @classmethod
    def numberofpoems(cls):
        return cls.numbers

    def __repr__(self) -> str:
        return f"name:{self.name}\nowners:{self.owners},pemtype:{self.poemtype}"

class Book(assar):
    numbers = 0

    def __init__(self, writer: Writer, number, name, publication="", *owners) -> None:
        super().__init__(name, *owners)
        self.writer = writer
        self.publication = publication
        self.number = number
        self.owners = owners
        poem.numbers += number

    def __del__(self) -> None:
        poem.numbers += self.number

    @classmethod
    def count(cls):
        return cls.numbers

    def numberofowners(self):
        return len(self.owners)

class assey(assar):
    numbers = 0

    def __init__(self, reasercher: Researcher, number, name, *owners,year:str="") -> None:
        super().__init__(name, *owners)
        self.owners = owners
        self.researcher = reasercher
        self.year = year
        self.number = number
        poem.numbers += number

    def numberofowners(self):
        return len(self.owners)

    @classmethod
    def numberofpoems(cls):
        return cls.numbers

