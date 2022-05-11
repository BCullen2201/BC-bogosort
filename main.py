from os import system
from random import shuffle

listOfNumbers = [414, 986, 90, 327, 106, 679, 676, 380, 953, 489, 842, 628, 251, 278, 926, 954, 58, 543, 276, 92, 194, 513, 175, 402, 63, 138, 154, 972, 774, 565, 928, 842, 282, 871, 622, 267, 951, 319, 686, 21, 310, 874, 173, 233, 395, 522, 11, 19, 805, 206, 314, 864, 226, 704, 704, 94, 346, 207, 921, 783, 581, 97, 916, 325, 296, 209, 884, 24, 941, 24, 258, 921, 767, 646, 800, 869, 179, 65, 791, 287, 19, 328, 99, 39, 541, 956, 548, 390, 458, 823, 558, 10, 448, 12, 946, 991, 243, 830, 837, 531]
attempts = 1 # Lets user know how many times it took to sort listOfNumbers

sortedNumbers = listOfNumbers.copy()
sortedNumbers.sort()

def checkIfSorted():
    global attempts

    if listOfNumbers != sortedNumbers:
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