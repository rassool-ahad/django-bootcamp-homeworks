inputNum = int(input("enter your number"))
for rows in range(1,inputNum+1):
    for columns in range(1,inputNum+1):
        print(rows*columns,end="\t")
    print('\n')
