def revreseText(text:str):
    charList = [char for char in text]
    ## easy way :
    # charList.reverse()
    ## still another easy way:
    # charList = charList[-1::-1]
    ##algorithm base way :
    reversedCharstr =""
    # we can use text instead of charlist in next for loop .but just in case of working with list is cooler :)
    for charReversePosition in reversed(range(len(charList))):
        reversedCharstr = reversedCharstr + charList[charReversePosition]
    return reversedCharstr


def ispalindrom(text:str):
    return True if revreseText(text).lower()==text.lower() else False


userStr = input("enter your string:")
print(ispalindrom(userStr))