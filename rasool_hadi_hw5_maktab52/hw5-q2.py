#q2-1
with open("input-q-2.txt") as f:
    input_txt = f.read()
senteces = input_txt.split('.')
output_txt = ""
for sentence in senteces:
    if sentence[-1].isnumeric() is False:
        output_txt += sentence + '.\n'
    else:
        output_txt += sentence + '.'
with open('output-q-2-1.txt', 'w') as f:
    f.write(output_txt)
#for fun : delete [number]
for letter in range(input_txt.count('[')-1):
    input_txt = input_txt.replace(input_txt[input_txt.index('['):input_txt.index(']')+1], '')
input_txt = input_txt[:-3]

#q2-2
input_txt = input_txt.replace('\n', '')
input_txt2 = input_txt.lower()
words = input_txt2.split(' ')
extraList =[',',
            '(',
            ')',
            '.'
]

unicWords =[]
numbers = []
for word in words:
    for extra in extraList:
        word = word.replace(extra, "")
    if word.isnumeric():
        numbers.append(word)
        continue
    if input_txt2.count(word) == 1:
        unicWords.append(word)
writetxt = "unic words:\n"
for words in unicWords:
    writetxt += words + "\n"
writetxt += "numbers:\n"
for number in numbers:
    writetxt += number+"\n"
writetxt += f'number of unic words is {len(unicWords)}\n number of numbers is {len(numbers)}'
with open("output-q-2-2.txt", 'w') as f:
    f.write(writetxt)
#q-2-3
print(input_txt)
wordlist = input_txt.split(' ')
allupper = []
firstupper = []
for word in wordlist:
    for extra in extraList:
        word = word.replace(extra, "")
    if word.isupper():
        allupper.append(word)
    elif word[0].isupper():
        firstupper.append(word)
        print(word)

writetxt = "words with all letters upper are:\n"
for word in allupper:
    writetxt += word + " , "
writetxt += "\nwords with first letters upper are:\n"
for word in firstupper:
    writetxt += word + " , "
with open("output-q-2-3.txt", 'w') as f:
    f.write(writetxt)






