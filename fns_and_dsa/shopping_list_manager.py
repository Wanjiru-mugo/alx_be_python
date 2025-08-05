shopping_list = list() #declaring empty list; also shopping_list []
item = input('please choose option (add, remove, view, exit) to the list:').stripe().lower()
while True:
    if item == 'add':
        item = input('Add an item to the shopping list:').stripe().lower()
        shopping_list.append(item)
    elif item == 'remove':
        item = input('Choose an item to remove from shopping list:').stripe().lower()
        if not item in shopping_list:
            print('Item not found')
        else:
            shopping_list.remove(item)
    elif item == 'view':
        print(shopping_list)
    elif item == 'exit':
        print('Goodbye')
    else:
        print('Invalid choice. Please try again')
