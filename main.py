from os import system
from random import shuffle

def makeList():
    listOfNum = []
    
    for i in range(1,11):
        listOfNum.append(i)

    shuffle(listOfNum)

    return listOfNum

def makeSortedList(unsorted):
    sortedNum = []

    sortedNum = unsorted.copy()
    sortedNum.sort()

    return sortedNum

def checkIfSorted(sorted, unsorted):
    attempts = 0

    while unsorted != sorted:
        system("clear")
        print(f"List:   {unsorted}")
        print(f"Sorted: {sorted}")
        print("Not sorted")
        attempts = attempts + 1
        print(f"Attempts: {attempts}")
        shuffle(unsorted)

    system("clear")
    print(f"List:   {unsorted}")
    print(f"Sorted: {sorted}")
    print("List is sorted!")
    print(f"Attempts: {attempts}")
        
def main():
    numList = makeList()
    sortedNumList = makeSortedList(numList)
    checkIfSorted(sortedNumList, numList)

if __name__ == "__main__":
    main()
