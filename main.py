from numpy.f2py.auxfuncs import throw_error

from item import *

def write_to_file(file_data):
    try:
        file = open("inventory.txt", "w")
        for x in file_data:
            file.write(x.fields_as_string())
        file.close()
    except:
        print("unknown error has happen :(")
        return -1

def read_from_file():
    list_of_items = []
    try:
        file = open("inventory.txt")
        for x in file:
            temp_list = x.split(",")
            list_of_items.append(Item(temp_list[0], temp_list[1], temp_list[2], temp_list[3]))
        file.close()
        return list_of_items
    except FileNotFoundError:
        file = open("inventory.txt", "w")
        list_of_items.append(Item(1, "Apple", 50, 0.5))
        list_of_items.append(Item(2, "Banana", 30, 0.3))
        list_of_items.append(Item(3, "Orange", 20, 0.7))
        write_to_file(list_of_items)
        return list_of_items
    except:
        print("unknown error has happen :(")
        return -1
        
def show_options():
    print("1. Add Item\r\n"
		+ "2. View Items\r\n"
		+ "3. Update Item\r\n"
		+ "4. Delete Item\r\n"
		+ "5. Exit\r\n\n")

def get_user_input(what_to_show):
    user_input = ""
    
    if what_to_show == 1:
        show_options()
        user_input = input("Choose an option: ")
    elif what_to_show == 2:
        user_input = input("Enter: ")
    
    return user_input

if __name__ == "__main__":
    max_id = None
    while True:
        file_data = read_from_file()
        
        
        
