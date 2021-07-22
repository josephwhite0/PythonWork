#Name: Joseph White
#Teacher: Tom Bloomfield
#Class: CS 115
#Program: Python Program Project 3

#printing the menu of operations
print("(1) addition \n(2) subtraction \n(3) multiplication \n(4) division \n(5) quit")
operation = int(input("Please enter a number (1-5): "))

#validating the input for operation
while operation > 5:
    print("(1) addition \n(2) subtraction \n(3) multiplication \n(4) division \n(5) quit")
    operation = int(input("Please enter a number (1-5): "))
    
#creating a while loop so that if 5 is the input the program will quit and creating
#variables from input from user
while operation < 5:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    #validating input so the user can't divide by 0, a message will print and the menu will
    #display again
    if (num1== 0 or num2 == 0) and operation == 4:
        print("Division by zero is undefined")
        print("(1) addition \n(2) subtraction \n(3) multiplication \n(4) division \n(5) quit")
        operation = int(input("Please enter a number (1-5): "))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
    #defining the different operations based on what is chosen
    if operation == 1:
        print(num1 + num2)
    if operation == 2:
        print(num1 - num2)
    if operation == 3:
        print(num1 * num2)
    if operation == 4:
        div = (num1 / num2)
        print (format(div, '.2f'))
        
    #after operation completes menu will display again for user to choose another
    print("(1) addition \n(2) subtraction \n(3) multiplication \n(4) division \n(5) quit")
    operation = int(input("Please enter a number (1-5): "))
    
#when user chooses to close program, "goodbye" will print
else:
    print("Goodbye")

