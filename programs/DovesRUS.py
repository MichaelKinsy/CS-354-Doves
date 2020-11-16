import mysql.connector      #Import the mysql connector module needs to be downloaded on machine that is executing script
from mysql.connector import Error

#method to connect to store database and return the connection
def connect():

    conn = None
    #Examples error handling and connecting to a database
    try:

        conn = mysql.connector.connect(host='localhost',
                                       database='DovesRUS',
                                       user='root',
                                       password='Hallpass99')
        if conn.is_connected():
            print("Successfully connected to the DovesRUS store Database!!!")

    except Error as e:
        print(e)

    return conn

#method to close the open connection and cursro from database
def disconnect(conn,cursor):
    if conn.is_connected():
        cursor.close()
        conn.close()
        print('Succesfully disconnected from the DovesRUS store Database!!!')
    else:
        print('Could not disconnect from DovesRUS stroe Database')

#method that executes a stored procedure to create a new customer
def newCustomer(name,address,cursor):
    try:
        cursor.callproc('newCustomer',(name,address,)) #method takes in a procedure name and a tuple as arguments
        print("Successfully added new customer to our database!!!")
    except mysql.connector.Error as error:      #Different example of catching an error
        print("Failed to execute stored procedure: {}".format(error)) #uses the string format method

#method that executes a stored procedure to create a new product
def newProduct(name,quantity,price,cursor):
    try:
        cursor.callproc('newProduct',(name,quantity,price,))
        print("Successfully added new product to our database!!!")
    except mysql.connector.Error as error:      #Different example of catching an error
        print("Failed to execute stored procedure: {}".format(error)) #uses the string format method

#method that executes a stored procedure to create a new order
def newOrder(customerID,productID,orderDate,cursor):
    try:
        cursor.callproc('newOrder',(customerID,productID,orderDate,))
        print("Successfully added new order to our database!!!")
    except mysql.connector.Error as error:      #Different example of catching an error
        print("Failed to execute stored procedure: {}".format(error)) #uses the string format method

#method that executes a prepared statement and returns all of the customers in the database
def getCustomers(cursor):
    query = ("SELECT * FROM Customers")
    cursor.execute(query)
    print("Here is all of the customer data in our database:\n")
    for(id,name,address) in cursor: #The cursor is a data structure that we can iterate over and collect it's values based on passed keys
        print("id:{}, name:{}, address:{}".format(
            id,name,address))

#method that executes a prepared statement and returns all of the products in the database
def getProducts(cursor):
    query = ("SELECT * FROM Products")
    cursor.execute(query)
    print("Here is all of the product data in our database:\n")
    for(id,name,quantity,price) in cursor: #The cursor is a data structure that we can iterate over and collect it's values based on passed keys
        print("id:{}, name:{}, quantity:{}, price:{}".format(
            id,name,quantity,price))

#method that executes a prepared statement and returns all of the products in the database
def getOrders(cursor):
    query = ("SELECT * FROM Orders")
    cursor.execute(query)
    print("Here is all of the order data in our database:\n")
    for(id,cusid,proid,date) in cursor:  #The cursor is a data structure that we can iterate over and collect it's values based on passed keys
        print("id:{}, customerid:{}, productid:{}, orderdate{:%d %b %y}".format(
            id,cusid,proid,date))

#method that executes a prepared statement and deletes a specific customer from database
def deleteCustomer(id,cursor):
    query = ("DELETE FROM Customers WHERE Customers.id = id")
    try:
        cursor.execute(query)
        print("Successfully deleted customer")
    except mysql.connector.Error as error:      #Different example of catching an error
        print("Failed to delete customer: {}".format(error)) #uses the string format method

#method that executes a prepared statement and deletes a specific product from database
def deleteProduct(id,cursor):
    query = ("DELETE FROM Products WHERE Products.id = id")
    try:
        cursor.execute(query)
        print("Successfully deleted Product")
    except mysql.connector.Error as error:      #Different example of catching an error
        print("Failed to delete Product: {}".format(error)) #uses the string format method

#method that executes a prepared statement and deletes a specific order from database
def deleteOrder(id,cursor):
    query = ("DELETE FROM Orders WHERE Orders.id = id")
    try:
        cursor.execute(query)
        print("Successfully deleted order")
    except mysql.connector.Error as error:      #Different example of catching an error
        print("Failed to delete order: {}".format(error)) #uses the string format method
#The definition of the main method for our program
def main():
    #establish connection and create cursor
    conn = connect()
    cursor = conn.cursor()

    #Call all of our previously defined functions to see their effect on the database
    newCustomer("Doug","whoknows ST",cursor)
    newCustomer("Aiden","whoknows AVE",cursor)
    newCustomer("Eddie","whoknows BLV",cursor)

    newProduct("Corsair something",100,'$10',cursor)
    newProduct("Python courses",1,'$100000',cursor)

    newOrder(2,1,'2021-07-21',cursor)
    newOrder(3,2,'2022-07-23',cursor)
    newOrder(4,3,'2020-16-20',cursor)

    getCustomers(cursor)
    getProducts(cursor)
    getOrders(cursor)

    deleteCustomer(2,cursor)
    deleteCustomer(3,cursor)
    deleteCustomer(4,cursor)

    deleteOrder(2,cursor)
    deleteOrder(3,cursor)
    deleteOrder(4,cursor)

    deleteProduct(3,cursor)

    getCustomers(cursor)
    getProducts(cursor)
    getOrders(cursor)

    #finally disconnect and close cursor for database
    disconnect(conn,cursor)

#The entry point of our program
if __name__ == '__main__':
    main()
