#Program Name: Country Capital Dictionary Game 
#Author's Name: Joseph White
#Date: 6.3.2021
#Description of Program: This program creates a country/capital trivia game using a dictionary using the two data points of country and capital.

import random

#assigning variables
countryDict = {}
data = ""
country = ""
cList = []
capCity = ""
correct = 0
incorrect = 0
answer = ""
cont = "YES"

#opening file, cleaning up data, and assigning data to dictionary
f = open("C:/Users/josef/Desktop/python work/data/countries_and_capitals.txt", "r")

for x in f:
    data= x.split("\t")
    while("" in data):
        data.remove("")
    country = data[0]
    cList.append(country)
    capCity = data[1]
    capCity = capCity[:-1] 
    countryDict[country] = capCity

f.close()

#Creating a loop that picks a random element from a list of countries. Then asks the user to enter
#the capital of said country. If they are correct, their correct score goes up one and if they are
#wrong their incorrect score goes up. This loop continues until user says that they no longer want 
#to continue. The loop will then break and tell the user their score.
cListLen = len(cList) - 1
while cont == "YES":
    randomNum = random.randint(0,cListLen) 
    randCountry = cList[randomNum] 
    answer = input("Enter the capital of " + randCountry + ": ")
    if answer == countryDict[randCountry]:
        correct += 1
        cont = input("Correct! Continue? YES or NO: ")
        #Validation loop so that if anyting else is entered other than YES or NO then it will
        #say the input is invalid
        while cont != "YES" and cont != "NO":
            cont = input("Invalid input. Would you like to continue? YES or NO: ")
        if cont == "NO":
            print("Thank you for playing!\nCorrect:",correct,"\n"+"Incorrect:",incorrect)
            break
        
    else:
        incorrect += 1
        cont = input("Wrong! Try again? YES or NO: ")
        #Validation loop so that if anyting else is entered other than YES or NO then it will
        #say the input is invalid
        while cont != "YES" and cont != "NO":
            cont = input("Invalid input. Would you like to continue? YES or NO: ")
        if cont == "NO":
            print("Thank you for playing!\nCorrect:",correct,"\n"+"Incorrect:",incorrect)
            break
            
        