class Indenter:
    count_enter = 0

    def __enter__(self):
        print("   " * self.count_enter, end="")
        self.count_enter += 1
        return self

    def print(self, text: str):
        print(text)

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('talk is cheap')
        with indent:
            indent.print('show me the code ')
    indent.print('Torvalds')

# output is :

"""
hi!
	talk is cheap
		show me the code 
Torvalds



"""
