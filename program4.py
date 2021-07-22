#Name: Joseph White
#Teacher: Thomas Bloomfield
#Class: CS 115
#Program: Python program 4 that creates random numbers, prints them to a file,
#reads data from file, passes data through a made function, and outputs an accumulation
#based on a certain rule set

#importing random module for random number generator
import random

def main():
    #creating variables and assigning with input
    numGen = input("Please enter how many random numbers you would like to generate:")
    while numGen.isdigit()== False:
        numGen = input("This is not a valid number, please try again:")
    numGen = int(numGen)
    #creating and writing intergers.txt
    numberFile = open("integers.txt", "w")
    lineNumber = 0
    #creating loop for random number generation
    for n in range(numGen):
        num = random.randrange(501)
        numberFile.write(str(num) + "\n")
    #closing file object
    numberFile.close()

    numberFile = open("integers.txt", "r")
    line = numberFile.readline()
    #creating accumulator and assigning to 0
    accumulator = 0
    #reading lines until line returns blank string
    while line != '':
        lineNumber += 1
        x = int(line)
        accumulator += process_data(x, lineNumber)
        line = numberFile.readline()
    print(accumulator)
    numberFile.close()
    
def process_data(line, lineNumber):
    #function that returns an output for the accumulator
    accumulator = 0
    #created flag so that once the highest number is used no other number will be used
    flag = 0
    if line % 11 == 0:
        accumulator += 11
        flag = 1
    if line % 7 == 0 and flag == 0:
        accumulator += 7
        flag = 1
    if line % 5 == 0 and flag == 0:
        accumulator += 5
        flag = 1
    if line % 3 == 0 and flag == 0:
        accumulator += 3
        flag = 1
    if line % 2 == 0 and flag == 0:
        accumulator += 2
        flag = 1
    if line % 2 != 0 and line % 3 != 0 and line % 5 != 0 and line % 11 != 0:
        accumulator += lineNumber
    return accumulator

    
#calls main function
main()



