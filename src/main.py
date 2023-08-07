from os import system
from random import shuffle
from time import process_time_ns as timer

def makeList(userChoice):
    numList = []
    userChoice = userChoice + 1
    
    for i in range(1,userChoice):
        numList.append(i)

    shuffle(numList)

    return numList

def checkIfSorted(numList):
    system("clear")
    print('"Sorting"...')
    attempts = 0
    walls = 1
    length = len(numList) - 1

    while walls != 0:
        attempts = attempts + 1
        walls = 0

        for i in range(0, length):
            if numList[i] > numList[i + 1]:
                walls = walls + 1
                shuffle(numList)

    system("clear")
    print("List is sorted!")
    print(numList)
    print(f"Attempts: {attempts}")
        
def main():
    system("clear")
    userChoice = input("How many numbers do you want to sort?: ")
    numList = makeList(int(userChoice))
    checkIfSorted(numList)
    print(f"Process time: {timer() * 1.0E-9} s")

if __name__ == "__main__":
    main()
