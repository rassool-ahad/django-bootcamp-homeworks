rowsNum = int(input("enter number of Pascal's triangle row "))
itemsLst = []
for row in range(rowsNum):
    print(((rowsNum-row)-1)*' ', end='')
    rowLst = []
    for items in range(row+1):
        if items == 0:
            rowLst.append(1)
        elif items == row:
            rowLst.append(1)
        else:
            rowLst.append(itemsLst[row-1][items]+itemsLst[row-1][items-1])
    itemsLst.append(rowLst)
    for i in rowLst:
        print(i, end=' ')
    print('\n', end='')
inp = input("""that was triangle shape of pascal's triangle :) 
by the way in the home work shape of output was diferent.
do you want see the home work output shape too??(y/n)""")
if inp == 'y':
    for row in itemsLst:
        for i in row:
            print(i, end=' ')
        print('\n', end='')
elif inp == 'n':
    print('bye')
    exit()