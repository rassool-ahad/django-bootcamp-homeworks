operatorLst = ['+', '-', '/', '*']
inp = input('enter your numbers with operator between them')
inp.replace(' ', '')
userOperator = ''
for i in operatorLst:
    if inp.find(i) != -1:
        userOperator = i
        break
else:
    print('i could not find operator. check the syntax and run again')
    exit()
firstNum = int(inp[0:inp.index(userOperator)])
secondNum = int(inp[inp.index(userOperator)+1:])
if userOperator == '-':
    print(firstNum-secondNum)
elif userOperator == '+':
    print(firstNum+secondNum)
elif userOperator == '*':
    print(firstNum*secondNum)
elif userOperator == '/':
    print(firstNum/secondNum)
# a = {
# '+': lambda x, y: x + y,
# '-': lambda x, y: x - y,
# '/': lambda x, y: x / y,
# '*': lambda x, y: x * y,
# '//': lambda x, y: x // y,
# }
# a['-'](1,2)