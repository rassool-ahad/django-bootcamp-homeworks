import logging

logging.basicConfig(level=logging.DEBUG,filename="person.log", filemode="a")

logger_person = logging.getLogger("person_logger")
file_handler2 = logging.FileHandler('person.log', 'a')
log_format_2 = logging.Formatter("%(asctime)s-%(name).10s-%(levelname).16s-%(message)s")

stream_handler2 = logging.StreamHandler()
file_handler2.setFormatter(log_format_2)
stream_handler2.setFormatter(log_format_2)
stream_handler2.setLevel(logging.INFO)
logger_person.addHandler(stream_handler2)
logger_person.addHandler(file_handler2)
class Person():
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        logger_person.log(logging.WARNING, f"Person created! {name} {family}")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            logging.critical("Invalid age!")
        self._age = 0
