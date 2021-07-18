scores = input('enter student scores with space separator')
scoresLst = scores.split(' ')
sumOfScores = 0
minimum = int(scoresLst[0])
maximum = int(scoresLst[0])
for eachScore in scoresLst:
    if int(eachScore) > maximum:
        maximum = int(eachScore)
    elif int(eachScore) < minimum:
        minimum = int(eachScore)
    sumOfScores = sumOfScores + int(eachScore)
avg = sumOfScores/len(scoresLst)
print(f"""maximum = {maximum}
minimum = {minimum}
average = {avg}
""")