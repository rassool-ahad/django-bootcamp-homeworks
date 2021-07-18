dividedbylist = lambda n:[i for i in range(1,n+1) if not (n%i)]
userInput = int(input('enter your number:'))
sum = 0
count = 1
while len(dividedbylist(sum)) != userInput:
    sum += count
    count += 1
    if len(dividedbylist(sum))>userInput :
        print(f"there is no good number with {userInput}  divided by")
        break
else :
    print(sum)