import requests
from itertools import product
import re

successfullLinks = []

#author Gene Wicaksono                                                     hi shaun







##Params:
# amountOfNums The amount of digits you would like to check. leave none if you input current
# current digits you are sure about. if left none, you must input amountOfNums
# highestdigit Max value of each digit. this affects performance dramatically.
# onlyFindFirst if true, it will stop the program and only return the first successfull link. 
def urlBash(amountOfNums:int=None, highestdigit:int=9, current:list = None, onlyFindFirst:bool=True):
    successfullLinks = []
    if not current:
        if not amountOfNums:
            return print("if you have an empty current, please input the amountOfNums param")
        current = []
        for x in range(amountOfNums):
            current.append("-")
    else:
        current = list(map(str, current))
        print(current)
        amountOfNums = len(re.findall("-", "".join(current)))
    

    genNum = []
    for num in range(highestdigit):
        genNum.append(str(num+1))
    allPossibilities = list(product(genNum, repeat=amountOfNums))
    print(allPossibilities)

    for x in allPossibilities:
        currentCopy = [x for x in current]
        for number in x:
            currentCopy[currentCopy.index("-")] = number
        print(currentCopy)
        joined = int("".join(currentCopy))
        stringreq = f"http://mathbits.com/caching/GC{joined}.html"
        print(stringreq)
        import requests
        response = requests.get(stringreq)
        if response.status_code !=404:
            print("Successfull Link: %s"%(stringreq))
            successfullLinks.append(stringreq)
            if onlyFindFirst:
                break
    if not successfullLinks:
        print("Complete. No working links found.")
    else:
        print("Compltete. Working links:")
    print(successfullLinks)



"example"
urlBash(amountOfNums=5, highestdigit=4, current=[4, 4, "-",4,1], onlyFindFirst=True)


