isPrimical = lambda n : not [i for i in range(2, n) if not (n % i)]
lowerPrimicalList= lambda n: [i for i in range(2, n) if isPrimical(i)]
dividedbylist = lambda n:[i for i in range(2,n) if not (n%i)]
primicalDividedby = lambda n:[i for i in dividedbylist(n) if isPrimical(i)]
def PriceWithdiscount(price)->int:
    if isPrimical(price):
        return price - len(lowerPrimicalList(price))
    else :
        return price - len(dividedbylist(price))


numberofStones = int(input("enter number of stones and then press enter:"))
count = 1
price = 0
while count != numberofStones+1:
    eachStoneWeight= int(input(f'enter {count}th stone weight:'))
    if isPrimical(int(eachStoneWeight)):
        price = price + len(lowerPrimicalList(int(eachStoneWeight)))
    else:
        price = price + len(primicalDividedby(int(eachStoneWeight)))
    print(f'your stones price without discount till now is {price}$')
    count += 1
print(f'your stones price with discount is {PriceWithdiscount(price)}$')