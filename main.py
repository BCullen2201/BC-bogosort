from os import system
from random import randint, shuffle

def randomList():
    list = []
    
    for i in range(1, 11):
        list.append(randint(1,10))

    return list

listOfNumbers = randomList()
attempts = 1

sortedNumbers = listOfNumbers.copy()
sortedNumbers.sort()

def checkIfSorted():
        global attempts # how the fuck do globals work

        if listOfNumbers != sortedNumbers:
            print(listOfNumbers)
            print(sortedNumbers)
            print("Not sorted")
            attempts = attempts + 1
            print(f"Attempts: {attempts}")
            shuffle(listOfNumbers)
        else:
            print(listOfNumbers)
            print(sortedNumbers)
            print("Numbers are sorted")
            print(f"Attempts: {attempts}")
            input("Press ENTER to go again") # stops infinite loop when listOfNumbers is sorted
            shuffle(listOfNumbers)

def main():
    while True:
        system("clear")
        checkIfSorted()

if __name__ == "__main__":
    main()