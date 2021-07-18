number_dic = {'one': '1',
              'tow': '2',
              'three': '3',
              'four': '4',
              'five': '5',
              'six': '6',
              'seven': '7',
              'eight': '8',
              'nine': '9',
              'ten': '10',
              'eleven': '11',
              'twelve': '12',
              'thirteen': '13',
              'fourteen': '14',
              'fifteen': '15',
              'sixteen': '16',
              'seventeen': '17',
              'eighteen': '18',
              'nineteen': '19',
              'twenty': '20'
              }
with open("input-q-1.txt", "r") as f:
    txt: str = f.read()
txt = txt.lower()
words = txt.split(' ')
for word in words:
    if number_dic.get(word, 0) != 0:
        txt = txt.replace(word, number_dic[word])
with open('output-q-1.txt', 'w') as f:
    f.write(txt)




