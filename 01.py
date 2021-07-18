import num2words as ntow


class notprimeexception(Exception):
    pass


def reminder(n: int()) -> callable:
    def inner_func1(func):
        def inner_func(*args, **kwargs):
            res = func(*args, **kwargs)
            return res % n

        return inner_func

    return inner_func1


def string_p(func: callable) -> callable:
    def inner_func(*args, **kwargs):
        res = func(*args, **kwargs)
        return f"the result is {ntow.num2words(res)}"

    return inner_func


class Multiplication_primals():
    """this class input should be tow primal number
    its output is that numbers multiplication"""

    def __init__(self, number1: int, number2: int):
        self.number1 = number1
        self.number2 = number2

    @staticmethod
    def is_primal(x: int) -> bool:
        for numbers in range(2, x):
            if x % numbers == 0:
                return False
        return True

    def __check_inputs(self) -> bool:
        if self.is_primal(self.number1) and self.is_primal(self.number2):
            return True
        else:
            return False

    # @reminder(3)
    @string_p
    def multiplication(self):
        if self.__check_inputs:
            return self.number1 * self.number2
        raise notprimeexception("there is a non-primal number in your inputs.check your numbers with is-primal method")


a = Multiplication_primals(11, 23)
print(a.multiplication())
