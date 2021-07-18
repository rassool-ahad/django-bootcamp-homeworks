def operator(operation:str):
    try:
        return eval(operation)

    except ZeroDivisionError:
        raise ZeroDivisionError
    except SyntaxError:
        raise SyntaxError

print(operator("2++2"))


