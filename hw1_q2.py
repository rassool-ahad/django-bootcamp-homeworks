inputStr = input("enter your text:")
vowls =['a','i','o','e','u']
countVowls = 0
countDigits = 0
sumDigits = 0
countChars = {}
for char in inputStr:
    if char in vowls:
        countVowls = countVowls +1
    elif char.isdigit():
        countDigits = countDigits+1
        sumDigits = sumDigits+int(char)
    if countChars.get(char) != None:
        countChars.update({char: (countChars.get(char)+1)})
    else :
        countChars[char] = 1
print(f'vowls:{countVowls}\ndigits:{countDigits}\nsum of digits:{sumDigits}')
for char, count in countChars.items():
    if count != 1:
        print(f"'{char}':{count}", end=',')