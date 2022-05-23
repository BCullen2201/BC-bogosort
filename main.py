from os import system
from random import shuffle

listOfNumbers = [9,4,7,2,1,5,3,6,8,10]
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