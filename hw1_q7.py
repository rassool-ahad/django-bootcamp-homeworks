userText = input('inter your text to counts characters')
countChars = {}
for char in userText:
    if countChars.get(char) != None:
        countChars.update({char: (countChars.get(char)+1)})
    else :
        countChars[char] = 1
for char, count in countChars.items():
    print(f'{char} : {count}')