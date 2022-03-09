# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# DP,03.06.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        DP,03.06.2022,Modified code to complete assignment 8
    """
    # TODO: Add Code to the Product class  -  DONE
    def __init__(self, product, price):  # Constructor
        self.__product = product
        self.__price = price

    @property  # PRODUCT
    def product(self):
        return str(self.__product)

    @product.setter
    def product(self, value):
        self.__product = value

    @property  # PRICE
    def price(self):
        return str(self.__price)

    @price.setter
    def price(self, value):
        if str(value).isnumeric() == True:
            self.__price = value
        else:
            print('Price should be a number')

    def __str__(self):  # String method converts object to string
        return self.product + ", " + str(self. price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)
    """

    # TODO: Add Code to process data from a file  -  DONE
    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        list_of_rows.clear()  # clear current data
        try:
            file = open(file_name, "r")
            for i in file:
                data = i.split(",")
                row = Product(data[0].strip(), data[1].strip())
                list_of_rows.append(row)
            file.close()
        except IOError:
            print("\nNo access to file. Program is terminated")
            exit()
        return list_of_rows
    """
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        <Your Name>,<Today's Date>,Modified code to complete assignment 8
    """

    # TODO: Add Code to process data to a file
    @staticmethod
    def save_data_to_file(file, data):
        f = open(file, "w")
        for i in data:
            f.write(i.__str__() + "\n")
        f.close()
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring  -  DONE
    """ Input/Output
    methods:
        output_menu
        input_menu_choice -> String
        show_data(list_of_rows)
        add_product(product, price)
    """
    pass
    # TODO: Add code to show menu to user - DONE
    @staticmethod
    def output_menu():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current data
        2) Add product
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    # TODO: Add code to get user's choice - DONE
    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    # TODO: Add code to show the current data from the file to user  -  DONE
    @staticmethod
    def show_data(list_of_rows):
        for i in list_of_rows:
            print(i.product + ", " + i.price)
        print()

    # TODO: Add code to get product data from user  -  DONE
    @staticmethod
    def add_product():
        new_product = input("Input new product: ")
        new_price = input("Input price: ")
        return Product(product=new_product, price=new_price)

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Main Body of Script  ---------------------------------------------------- #
FileProcessor.read_data_from_file(file_name=strFileName, list_of_rows=lstOfProductObjects)  # Read file
while (True):
    IO.output_menu()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option
    if choice_str == '1':  # Show current data
        IO.show_data(list_of_rows=lstOfProductObjects)
    if choice_str == '2':  # Add new product
        k = IO.add_product()
        lstOfProductObjects.append(k)
    if choice_str == "3":  # Save data to file
        FileProcessor.save_data_to_file(file=strFileName, data=lstOfProductObjects)
    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # by exiting loop