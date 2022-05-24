from os import system
from random import randint, shuffle

attempts = 0

def makeList():
    global listOfNum
    listOfNum = []
    
    for i in range(0,10):
        listOfNum.append(randint(1,10))

    return listOfNum

def makeSortedList():
    global sortedNum

    sortedNum = makeList().copy()
    sortedNum.sort()

    return sortedNum

def checkIfSorted():
    global attempts
    global listOfNum # I still don't know how globals work
    global sortedNum
    
    if listOfNum != sortedNum:
        print(f"List:   {listOfNum}")
        print(f"Sorted: {sortedNum}")
        print("Not sorted")
        attempts = attempts + 1
        print(f"Attempts: {attempts}")
        shuffle(listOfNum)
    else:
        print(f"List:   {listOfNum}")
        print(f"Sorted: {sortedNum}")
        print("List is sorted!")
        print(f"Attempts: {attempts}")
        input("Press ENTER to try and sort another list...")
        attempts = 0
        listOfNum = makeList()
        sortedNum = makeSortedList()
        
def main():
    makeList()
    makeSortedList()
    while True:
        system("clear")
        checkIfSorted()

if __name__ == "__main__":
    main()