#Program Name: Bookstore Database
#Author's Name: Joseph White
#Date: 7.15.2021
#Description of Program: This program builds a database using .txt data files for a bookstore. It also has a system where a user
#can look up specific information from the database, and also prints out orders/resupply numbers.

import pymysql

index = 0
userInput = ""
userISBN = ""
userPubID = ""
userCustID = ""

#open connection
conn = pymysql.connect(host = 'localhost', user = 'root')

#obtaining curser
cursor = conn.cursor()

#creating database
with conn:
    with conn.cursor() as cursor:

        cursor.execute('CREATE DATABASE IF NOT EXISTS bookstore;')

        #creating tables in database
        cursor.execute('CREATE TABLE IF NOT EXISTS bookstore.Customers(custID int NOT NULL,Name varchar(255), Address varchar(255), Age varchar(25), Income int, loginID varchar(255), Password varchar(255), Additional_attributes varchar(255), PRIMARY KEY(custID));')
        cursor.execute('CREATE TABLE IF NOT EXISTS bookstore.Publishers(publisherID int NOT NULL, Name varchar(255), Address varchar(255), Discount int, PRIMARY KEY(publisherID));')
        cursor.execute('CREATE TABLE IF NOT EXISTS bookstore.Books(ISBN bigint NOT NULL, Title varchar(255), Author varchar(255), Qty_in_Stock int, Price int, Cost int, Year int, publisherID int, PRIMARY KEY(ISBN), FOREIGN KEY(publisherID) REFERENCES bookstore.Publishers(publisherID));')
        cursor.execute('CREATE TABLE IF NOT EXISTS bookstore.Orders(orderNum int NOT NULL AUTO_INCREMENT, custID int, CCnum bigint, CCmonth int, CCyear int, Orderdate varchar(255), Shipdate varchar(255), PRIMARY KEY(orderNum), FOREIGN KEY(custID) REFERENCES bookstore.Customers(custID));')
        cursor.execute('CREATE TABLE IF NOT EXISTS bookstore.OrderList(orderNum int NOT NULL , ISBN bigint, orderQuantity int, PRIMARY KEY(orderNum), FOREIGN KEY(ISBN) REFERENCES bookstore.Books(ISBN))')
        cursor.execute('CREATE TABLE IF NOT EXISTS bookstore.StockResupply(ISBN bigint, quant int, FOREIGN KEY(ISBN) REFERENCES bookstore.Books(ISBN))')
        
        #entering in data from the customer table into the database
        f = open("data\Cust_table.txt")
        for x in f:
            custList = x.split(",")
            custList[len(custList) -1] = custList[len(custList) -1].strip()
            custList.insert(2, (custList[2] + custList.pop(3) + custList.pop(3)))
            custList.pop(3)
            custList[0] = int(custList[0])
            custList[4] = float(custList[4])
            q = "INSERT INTO bookstore.Customers(custID, Name, Address, Age, Income, loginID, Password) VALUES (%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(q, (custList))
            conn.commit()
        f.close()

        #entering in data from the Publisher table into the database
        f = open("data\Publisher_table.txt")
        for x in f:
            pubList = x.split(",")
            pubList[len(pubList) - 1] = pubList[len(pubList) -1].strip()
            if len(pubList) == 7:
                pubList.insert(2, (pubList[2] + pubList.pop(3) + pubList.pop(3) + pubList.pop(3)))
                pubList.pop(3)
            elif len(pubList) == 6:
                pubList.insert(2, (pubList[2] + pubList.pop(3) + pubList.pop(3)))
                pubList.pop(3)
            q = "INSERT INTO bookstore.Publishers(publisherID, Name, Address, Discount) VALUES (%s, %s, %s, %s);"
            cursor.execute(q, (pubList))
            conn.commit()
        f.close()

        #entering in the data from the Book table into the database
        f = open("data\Book_table.txt")
        for x in f:
            bookList = x.split(",")
            bookList[len(bookList) - 1] = bookList[len(bookList) - 1].strip()
            q = "INSERT INTO bookstore.Books(ISBN, Title, Author, Qty_in_Stock, Price, Cost, Year, publisherID) VALUES(%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(q, (bookList))
            conn.commit()
        f.close()

        #entering in the data from the OrderList table into the database
        f = open("data\Orderlist_table.txt")
        for x in f:
            orderLst = x.split(",")
            orderLst[len(orderLst) - 1] = orderLst[len(orderLst) - 1].strip()
            q = "INSERT INTO bookstore.OrderList(orderNum, ISBN, orderQuantity) VALUES(%s,%s,%s);"
            cursor.execute(q, (orderLst))
            conn.commit()
        f.close()
        
        #entering in the data from the Orders table into the database
        f = open("data\Orders_table.txt")
        for x in f:
            orders = x.split(",")
            orders[len(orders) - 1] = orders[len(orders) - 1].strip()
            q = "INSERT INTO bookstore.Orders(custID, CCnum, CCmonth, CCyear, Orderdate, Shipdate) VALUES(%s,%s,%s,%s,%s,%s);"
            cursor.execute(q, (orders))
            conn.commit()
        f.close()
        
        #takes the data from the Orderlist table in database and enters it into the stockresupply table
        q = "SELECT ISBN, orderQuantity FROM bookstore.OrderList;"
        cursor.execute(q)
        data = cursor.fetchall()
        for row in data:
            orderList = row
            q = "INSERT INTO bookstore.StockResupply(ISBN, quant) VALUES(%s,%s);"
            cursor.execute(q, (orderList))
            conn.commit()
            
        #creates a loop and a simple interface for a user to look up a book, publisher, or customer
        while userInput != "exit":
            userInput = input("Press 1 to enter ISBN, 2 for CustomerID, or 3 for PublisherID?: ")
            
            while userInput == "1" and userInput != "exit":
                userInput = int(input("Please enter Book ISBN number: "))
                if userInput <= 99999999999 and userInput > 0:
                    ISBNokay = userInput
                    q = "SELECT * FROM bookstore.Books WHERE ISBN = %s"
                    cursor.execute(q, (ISBNokay))
                    data = cursor.fetchall()
                    for row in data:
                        bookISBN, bookTitle, bookAuthor, QinStock, bookPrice, bookCost, bookYear, bookPubID = row
                    
                        q = "SELECT Name From bookstore.Publishers WHERE publisherID = %s"
                        cursor.execute(q, (bookPubID))
                        
                        data = cursor.fetchone()
                        for row in data:
                            pubActual = row

                        print("{0:<15} {1:<35} {2:<30} {3:<15} {4:<15} {5:<15} {6:<25} {7}\n"
                                "{8:<15} {9:<35} {10:<30} {11:<15} {12:<15} {13:<15} {14:<25} {15}\n".format("ISBN", "TITLE", "AUTHOR", "IN STOCK", "BOOKPRICE", "BOOK COST",
                              "BOOK YEAR", "PUBLISHER", str(bookISBN), bookTitle, bookAuthor, str(QinStock), str(bookPrice), str(bookCost), str(bookYear), pubActual))
                else:
                    userInput = input("Please try again: ")
                    
            while userInput == "2" and userInput != "exit":
                userInput = int(input("Please enter Customer ID: "))
                if  userInput <= 999999999 and userInput > 0:
                    CustIDokay = userInput
                    q = "SELECT * FROM bookstore.Customers WHERE custID = %s"
                    cursor.execute(q, (CustIDokay))
                    data = cursor.fetchall()
                    for row in data:
                        custID, name, address, age, income, loginID, password, add_at = row
                        
                        print("{0:<13} {1:<25} {2:<40} {3:<10} {4:<15} {5:<15} {6}\n"
                              "{7:<13} {8:<25} {9:<40} {10:<10} {11:<15} {12:<15} {13}\n".format("CUSTOMER ID", "NAME", "ADDRESS", "AGE", "INCOME", "LOGIN ID", "PASSWORD", str(custID), name, address, str(age), str(income), loginID, password))  
                else:
                    userInput = input("Please try again")
                    
            while userInput == "3" and userInput != "exit":
                userInput = int(input("Please enter Publisher ID: "))
                if userInput <= 999999999 and userInput > 0:
                    PubIDokay = userInput
                    q = "SELECT * FROM bookstore.Publishers WHERE publisherID = %s"
                    cursor.execute(q, (PubIDokay))
                    data = cursor.fetchall()
                    for row in data:
                        publisherID, name, address, discount = row
                        
                        print("{0:<13} {1:<25} {2:<50} {3}\n"
                        "{4:<13} {5:<25} {6:<50} {7}\n".format("PUBLISHER ID", "NAME", "ADDRESS", "DISCOUNT", publisherID, name, address, str(discount)))
                else:
                    userInput = input("Please try again: ")

        # Prints out everything from the Orders table
        print()
        q = "SELECT * FROM bookstore.Orders"
        cursor.execute(q)
        data = cursor.fetchall()
        print("{0:<15} {1:<20} {2:<20} {3:<12} {4:<15} {5:<15} {6}".format("ORDER NUMBER", "CUSTOMER ID", "CARD NUMBER", "CARD MONTH", "CARD YEAR", "ORDER DATE", "SHIP DATE"))
        for row in data:
            orderNum, custID, cardNum, cardMonth, cardYear, orderDate, shipDate = row 
            
            print("{0:<15} {1:<20} {2:<20} {3:<12} {4:<15} {5:<15} {6}".format(str(orderNum), str(custID), str(cardNum), str(cardMonth), str(cardYear), orderDate, shipDate))

        # Prints out everything from the Order List table
        print()
        q = "SELECT * FROM bookstore.OrderList"
        cursor.execute(q)
        data = cursor.fetchall()
        print("{0:<15} {1:<20} {2}".format("ORDER NUMBER", "ISBN", "ORDER QUANTITY"))
        for row in data:
            orderNum, ISBN, orderQuant = row
            
            print("{0:<15} {1:<20} {2}".format(orderNum, ISBN, orderQuant))
        
        # Prints out everything from the Stock Resupply table
        print()
        q = "SELECT * FROM bookstore.StockResupply"
        cursor.execute(q)
        data = cursor.fetchall()
        print("{0:<20} {1}".format("ISBN", "ORDER QUANTITY"))
        for row in data:
            ISBN, quantity = row
            
            print("{0:<20} {1}".format(ISBN, quantity))

    
    