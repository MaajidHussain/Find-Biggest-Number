def find_big_number(simpleArray):
    biggestNumber=simpleArray[0]
    for i in range(1,len(simpleArray)):
        if simpleArray[i] > biggestNumber:
            biggestNumber=simpleArray[i]
    print(biggestNumber)
simpleArray=[63,32,59,68,100,121,54,78]
find_big_number(simpleArray)
