list1 = ['morning', 'afternoon', 'night']
list2 = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
finalList = []
for day in list2:
    for time in list1:
        finalList.append(f'{day}-{time}')
print(finalList)
