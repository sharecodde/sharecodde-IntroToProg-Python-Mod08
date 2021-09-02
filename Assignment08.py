# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes.  Program will manage a product list consisting of product name
#and product price.  The user may enter the name and price of a product, view the list of products and
#prices, save the data, and exit the program.

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# BGilbertson, 8.22.2021 Added header, identified variables
# BGilbertson, 8.24.2021 Added code for print current list, imported os module
# BGilbertson, 8.25.2021 Added code for menu and select choice
# BGilbertson, 8.26.2021 Added code to add a product and price
# BGilbertson, 8.29.2021 Troubleshooting and commenting
# BGilbertson, 8.31.2021 Experimenting with additional error handling
# ------------------------------------------------------------------------ #

import os  #to be used later for exception handling

#--- Begin Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = "" #gets users choice

class Product:
    """Stores and organizes data, such as name and price, about a product:
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        BGilbertson,8.22.2021 Developed the characteristics of the class
        BGilbertson,8.26.2021 Edited properties for price
        BGilbertson,8.29.2021 Troubleshooting and added error handling
    """
    #---Fields (data members) # not needed for this class, but including the header as
    # one of the components of a class

    #---Constructors---
    def __init__(self, product_name: str, product_price: float): #initialize and establish string and float type
        #--Attributes--
        self.__product_name = "" #set initial value to empty
        self.__product_price = "" #set initial value to empty
        try:
            self.product_name = str(product_name)
            self.product_price = float(product_price)
        except Exception as e:
            raise Exception("Initialization error: \n" + str(e)) #in case something happens converting to string or float

    #---Properties--:
    #ProductName
    @property
    def product_name(self): # (getter or accessor)
        return str(self.__product_name).title()  # Title case

    @product_name.setter #
    def product_name(self, value: str):  # (setter or mutator)
        if value.isnumeric(): # check if product name is numeric and raise exception if it is
            raise Exception ("Product names cannot be numbers. Please re-run the program")
        else:
            self.__product_name = value

    #ProductPrice
    @property
    def product_price(self): # (getter or accessor)
        return float(self.__product_price)  #confirm float type here too

    @product_price.setter #4
    def product_price(self, value: float):  # (setter or mutator)
        try: # check again for float type
            self.__product_price = float(value)
        except ValueError: #this is a built in error
            raise Exception("Product price must be numbers")

    #---Methods---:
    def __str__(self):
        return self.product_name + ',' + str(self.product_price)

#--- End Data -------------------------------------------------------------------- #

#---Beging Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        BGilbertson,8.22.2021     ##read from and write to file - use @static method
        BGilbertson,8.29.2021     ##troubleshooting and commenting - use @static method
    """
    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :return: (list) of product objects
        """
        list_of_product_rows=[]
        try:
            if os.path.exists(file_name):
                file = open(file_name, "r")
                for line in file:
                    data = line.split(",")  # split into two objects
                    row = Product(data[0], data[1])  #Make a new product object from Product class
                    list_of_product_rows.append(row)  # list_of_product_rows
                file.close()
        except FileNotFoundError as e:  # check to see if there is a file
            print("File not found, please add information to the list by"
                  "\nusing option 2 in the menu below.\n")
            input('Press the [Enter] key to display the main menu.')
        return list_of_product_rows

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """--writes data to the file ----
        :param file_name: name of file
        :param list_of_product_objects: (list) you want filled with file data
        :return list_of_product_objects: list of dictionary rows
        """
        try:
            objFile = open(file_name, "w")
            for product in list_of_product_objects:
                objFile.write(product.__str__() + "\n")
            objFile.close()
        except Exception as e:
            print("An error has occured while saving data to file")
            print(e, e.__doc__, type(e)) #print Exception error info


#---End Processing  ------------------------------------------------------------- #

#---Begin Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_hello():
        '''introduces the program to the user'''
        print()
        print("~" * 90)
        print("""                   
                                WELCOME
            This program allows the user to manage a list of product names 
            and prices. You may view or add products and prices to the list.\n""")
        print("~" * 90)

    @staticmethod
    def print_menu_Products():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) View existing products
        2) Add a product to the list
        3) Save data to file        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Products_in_list(list_of_rows): #changed from RR sample
        """ Shows the current Products in the list of product objects

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("****** The current Products and their Prices are: ******")
        for row in list_of_rows:
            print(row.product_name + " ($ " + str(row.product_price) + ")")
            #print(row)
        print("*************************************************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_product_info():
        """ Asks user to input product name and price
        :return: product info
        """

        try:
            pname = str(input("Enter the name of the product using only letters (no numbers please): ")).strip()  # get product name
            pprice = float(input("Enter product price using only numbers (decimal point is optional): $ ").strip())  # get product price, float type
            p1 = Product(product_name=pname, product_price=pprice)  # a product instance of Product class
            return p1
        except Exception as e:
            print(e)
        return p1

    @staticmethod
    def say_goodbye():
        """summarize Product information for the user and close the program"""
        print("Here is a summary of all the products in your file")
        print("=" * 90)
        IO.print_current_Products_in_list(lstOfProductObjects)
        print("=" * 90)
        print("\nThank you, press 'enter' to end the program.")
        input()
#--- End Presentation (Input/Output)  -------------------------------------------- #

#--- Begin Main Body of Script  ---------------------------------------------------- #

# Step 1 - When the program starts, Load data from file and introduce the program
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)  # read file data
IO.print_hello() # display introductory message to the user

# Step 2 - Print the current products in the list
IO.print_current_Products_in_list(lstOfProductObjects)  # Show current data in the list/table

try:
    while (True):
        # Step 3 Display a menu of choices to the user and get user choice
        IO.print_menu_Products()  # Shows menu of choices
        strChoice = IO.input_menu_choice()  # Get menu option from user

        # Step 4 - Process user's menu choice, Menu option 1 - show data in the list
        if strChoice.strip() == '1':  # View existing products
            IO.print_current_Products_in_list(lstOfProductObjects )
            IO.input_press_to_continue()

        # Step 5
        elif strChoice.strip() == '2': #Add product and price info
            lstOfProductObjects.append(IO.input_product_info())
            continue

        # Step 6 - Process user's menu choice, Menu option 3 - save data to a file
        elif strChoice == '3':  # Save Data to File
            strChoice = IO.input_yes_no_choice("Save this data to file? (y for yes; any other key to cancel) - ")
            if strChoice.lower() == "y":
                FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
                IO.input_press_to_continue()
            else:
                IO.input_press_to_continue("Save Cancelled")
            continue #shows the menu

        # Step 7 - Process user's menu choice, Menu option 4 - exit program
        elif strChoice == '4':  # Exit Program
            IO.say_goodbye()
            print("Goodbye!")
            break  # and Exit
        else:  # This code catches incorrect menu choices by the user
            print("Please choose only 1, 2, 3, or 4 from the menu\n")
except Exception as e:
    print("There was an error while running the program.")
    print(e)

#--- End Main Body of Script  ---------------------------------------------------- #

