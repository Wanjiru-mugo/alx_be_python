shopping_list = list() #declaring empty list; also shopping_list []
def display_menu():

    while True:
        item = input('please choose option (add, remove, view, exit) to the list:').strip().lower()

        if item == 'add':
            item = input('Add an item to the shopping list:').strip().lower()
            shopping_list.append(item)
        elif item == 'remove':
            item = input('Choose an item to remove from shopping list:').strip().lower()
            if not item in shopping_list:
                print(f'Item not found')
            else:
                shopping_list.remove(item)
        elif item == 'view':
            print(shopping_list)
        elif item == 'exit':
            print(f'Goodbye')
        else:
            print(f'Invalid choice. Please try again')
