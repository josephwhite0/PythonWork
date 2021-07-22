#Name: Joseph White
#Teacher: Tom Bloomfield
#Class: CS 115
#Program: This is a program that shows a menu and allows
#user to choose a number of operations that manipulate
#a string that is assigned by the user



#setting up variables


y = ""
list1 = []
list2 = []
count = {}
i = 0

def main ():
#setting up selection menu for string program
    menu = 0
    userInput = ""
    letter = ""
    num1 = 0
    num2 = 0
    menu = input("Menu:\n1.Enter a string\n"
             "2.Display the string\n"
             "3.Reverse the String\n"
             "4.Append the string\n"
             "5.Slice the string\n"
             "6.Display the count of each alphanumeric character\n"
             "7.Quit\n"
             "Please enter selection:")
    print()

#setting up process assigned to each number on the menu
    while menu != "7":
        if menu == "1":
        #assigns string to variable x
            userInput = input("Please enter a String:")
            print()
            menu = input("Menu:\n1.Enter a string\n"
                     "2.Display the string\n"
                     "3.Reverse the String\n"
                     "4.Append the string\n"
                     "5.Slice the string\n"
                     "6.Display the count of each alphanumeric character\n"
                     "7.Quit\n"
                     "Please enter selection:")
            print()
        elif menu == "2":
        #if there is no string assigned to x then this loop will activate.
        #this happens with every number in the menu except for the number 1
            if userInput == "":
                print("No String Entered")
                print()
                menu = input("Menu:\n1.Enter a string\n"
             "2.Display the string\n"
             "3.Reverse the String\n"
             "4.Append the string\n"
             "5.Slice the string\n"
             "6.Display the count of each alphanumeric character\n"
             "7.Quit\n"
             "Please enter selection:")
                print()
            else:
            #Displays the string assigned to x, then prints out menu again for
            #user to pick another number
                print("You entered:", userInput)
                print()
                menu = input("Menu:\n1.Enter a string\n"
             "2.Display the string\n"
             "3.Reverse the String\n"
             "4.Append the string\n"
             "5.Slice the string\n"
             "6.Display the count of each alphanumeric character\n"
             "7.Quit\n"
             "Please enter selection:")
                print()
        elif menu == "3":
            if userInput == "":
                print("No String Entered")
                print()
                menu = input("Menu:\n1.Enter a string\n"
             "2.Display the string\n"
             "3.Reverse the String\n"
             "4.Append the string\n"
             "5.Slice the string\n"
             "6.Display the count of each alphanumeric character\n"
             "7.Quit\n"
             "Please enter selection:")
                print()
            else:
            #Prints out inputed string backwords
                reverse = ""
                index = len(userInput)
                while index > 0:
                    reverse += userInput[index - 1]
                    index = index - 1
                userInput = reverse
                print(userInput)
                print()
                menu = input("Menu:\n1.Enter a string\n"
             "2.Display the string\n"
             "3.Reverse the String\n"
             "4.Append the string\n"
             "5.Slice the string\n"
             "6.Display the count of each alphanumeric character\n"
             "7.Quit\n"
             "Please enter selection:")
                print()
        elif menu == "4":
            if userInput == "":
                print("No String Entered")
                print()
                menu = input("Menu:\n1.Enter a string\n"
             "2.Display the string\n"
             "3.Reverse the String\n"
             "4.Append the string\n"
             "5.Slice the string\n"
             "6.Display the count of each alphanumeric character\n"
             "7.Quit\n"
             "Please enter selection:")
                print()
            else:
            #Appends a string to the original string
            #This will augment the original string
                userInput += input("Please enter a String to append to your first String:")
                print(userInput)
                print()
                menu = input("Menu:\n1.Enter a string\n"
             "2.Display the string\n"
             "3.Reverse the String\n"
             "4.Append the string\n"
             "5.Slice the string\n"
             "6.Display the count of each alphanumeric character\n"
             "7.Quit\n"
             "Please enter selection:")
                print()
        elif menu == "5":
            if userInput == "":
                print("No String Entered")
                print()
                menu = input("Menu:\n1.Enter a string\n"
             "2.Display the string\n"
             "3.Reverse the String\n"
             "4.Append the string\n"
             "5.Slice the string\n"
             "6.Display the count of each alphanumeric character\n"
             "7.Quit\n"
             "Please enter selection:")
                print()
            else:
            #Displays a slice of the string assigned to x
                num = input("Please enter first number for a slice operation on your String:")
                print()
            #isdigit() makes sure that the number entered is a number, and will loop if it is not
                while num.isdigit() != True:
                    num = input("Invalid Input : Please enter first number for a slice operation on your String:")
                    print()
                num1 = num
                num = input("Please enter the second number:")
                print()
                while num.isdigit() != True:
                    num = input("Invalid Input: Please enter the second number:")
                    print()
                num2 = num
            #slicing the string
                userInput = userInput[int(num1):int(num2)]
                print(userInput)
                print()
                menu = input("Menu:\n1.Enter a string\n"
             "2.Display the string\n"
             "3.Reverse the String\n"
             "4.Append the string\n"
             "5.Slice the string\n"
             "6.Display the count of each alphanumeric character\n"
             "7.Quit\n"
             "Please enter selection:")
                print()
        elif menu == "6":
            if userInput == "":
                print("No String Entered")
                print()
                menu = input("Menu:\n1.Enter a string\n"
             "2.Display the string\n"
             "3.Reverse the String\n"
             "4.Append the string\n"
             "5.Slice the string\n"
             "6.Display the count of each alphanumeric character\n"
             "7.Quit\n"
             "Please enter selection:")
                print()
            else:
            #This calls the process_string method which takes out all spaces, special characters, and makes all letter uppercase then
            #counts the times each digit or letter occurs in the string
                process_string(userInput)
                for x in list1:
                    global i
                    print(x, ",", list2[i])
                    i += 1
                print()
                menu = input("Menu:\n1.Enter a string\n"
             "2.Display the string\n"
             "3.Reverse the String\n"
             "4.Append the string\n"
             "5.Slice the string\n"
             "6.Display the count of each alphanumeric character\n"
             "7.Quit\n"
             "Please enter selection:")
                print()
        else:
        #if anything other than 1-7 is entered for the menu this loop initiates
            print("Invalid input, try again")
            print()
            menu = input("Menu:\n1.Enter a string\n"
             "2.Display the string\n"
             "3.Reverse the String\n"
             "4.Append the string\n"
             "5.Slice the string\n"
             "6.Display the count of each alphanumeric character\n"
             "7.Quit\n"
             "Please enter selection:")
            print()

def process_string(string):
    global count
    global y
    x = string
    x = x.replace(" ","")
    x = x.strip()
    x = x.upper()
    for ch in x:
        if ch.isalnum():
            y += ch
    for ch in y:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    for key in count:
        if count[key] >= 1:
            list1.append(key)
            list2.append(count[key])
     
        
    
main()










