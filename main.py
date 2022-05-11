from os import system
from random import shuffle

listOfNumbers = [9,4,7,2,1,5,3,6,8,10]
attempts = 1 # Lets user know how many times it took to sort listOfNumbers

sortedNumbers = listOfNumbers.copy()
sortedNumbers.sort()

def checkIfSorted():
    global attempts

    if listOfNumbers != sortedNumbers:
        print(listOfNumbers)
        print(sortedNumbers)
        print("Not sorted")
        attempts = attempts + 1
        print(f"Attempts: {attempts}")
        shuffle(listOfNumbers)
    else:
        print("Numbers are sorted")
        print(f"Attempts: {attempts}")
        input("Press ENTER to go again") # stops infinite loop when listOfNumbers is sorted

while True: # keeps checkIfSorted() running
    system("clear") # keeps window clean, results are more apparent
    checkIfSorted()