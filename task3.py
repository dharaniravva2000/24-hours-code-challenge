contacts_list = []  # global variable, list of contacts_list, one string per contact

def pause():
    """ pauses program e.g. to view data or message """
    input("Press enter to continue")

def load():
    """ populate list with data """
    contacts_list.append(('Alice', '0121'))
    contacts_list.append(('Bob', '3467'))
    contacts_list.append(('Sandra', '0122'))
   
    print("%s records have been loaded" % (len(contacts_list)))

def add():
    """ adds contact to list """
    name = input("Enter name: ")
    
    while True:  # Loop until valid phone number is entered
        phone_no = input("Enter phone number: ")
        if phone_no.isdigit():  # Ensures phone number contains only digits
            break
        print("Invalid phone number. Please enter digits only.")
    
    contacts_list.append([name, phone_no])

def view():
    """ displays contacts_list """
    index = 1
    for contact in contacts_list:
        print(index, " ", contact[0], " ", contact[1])
        index += 1
    pause()

def delete():
    """ removes contact based upon index """
    index = int(input("Enter index of contact to delete: "))
    if 1 <= index <= len(contacts_list):
        del contacts_list[index - 1]
    else:
        print("Invalid index")

def find():
    """ finds contact by phone number """
    phone_no = input("Enter phone number to find: ")
    for contact in contacts_list:
        if contact[1] == phone_no:
            print(f"Name associated with {phone_no} is {contact[0]}")
            return
    print("Contact not found")

def menu():
    """ loops menu of options and does these until user quits """
    while True:
        print("\nEnter for option")
        print("  =   ==========")
        print("  v   view contacts_list")
        print("  a   add contact")
        print("  d   delete contact")
        print("  f   find name for given phone no")
        print("  q   quit")
        option = input("Your option: ").lower()
        
        if option == "v":
            view()
        elif option == "d":
            delete()
        elif option == "a":
            add()
        elif option == "f":
            find()
        elif option == "q":
            return  # exit while loop and menu function
        else:
            print("Invalid menu option")
            pause()

def main():
    """ entry point if module imported or run as script """
    load()
    menu()

if __name__ == "__main__":
    main()