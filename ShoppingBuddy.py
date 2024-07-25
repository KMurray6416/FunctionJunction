    # Task 1

needed_items = []

def add_items():
    new_items = input("Enter the item you would like to add to your list: ")
    needed_items.append(new_items)
    
    # Task 2

def delete_items():
    item_to_delete = input("Enter the item to delete from the list: ")
    if item_to_delete in needed_items:
        needed_items.remove(item_to_delete)
        print(f"\n{item_to_delete} has been deleted.")
    else:
        print(f"\n{item_to_delete} is not on the list.")
    
    # Task 3

def view_items():
    list_view = input("would you like to view your list 'as is' or 'alphabetically'?   Enter 'as is' or 'alphabetically': ")
    if list_view.lower() == 'as is':
         print(needed_items)
    elif list_view.lower() == 'alphabetically':
        print(sorted(needed_items))
    else:
        print("\nInvalid input for view")
    
while True:
    print("\nHello! Let me be your shopping buddy!")
    print("1 Add to list")
    print("2 Delete from list")
    print("3 View list")
    print("4 QUIT")
    selection =int(input("Please enter only the number of the task you wish to perform: 1,2,3,4 "))

    if selection == 1:
        add_items()
        print("\nThis item has been put on the list.")
    elif selection == 2:
         delete_items()
    elif selection == 3:
        view_items()
    elif selection == 4:
        print("See ya later buddy!")
        break
    else:
        print("Invalid selection. Please select from: 1,2,3,4")