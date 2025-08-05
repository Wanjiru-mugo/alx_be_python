print('Shopping List Manager')

shopping_list = list() #declaring empty list; also shopping_list []

def display_menu():
    print('1. Add Item')
    print('2. Remove Item')
    print('3. View List')
    print('4. Exit')

    while True:
        item = input('Enter your choice (1-4): ').strip()

        if item == '1':
            item = input('Add an item to the shopping list:').strip().lower()
            shopping_list.append(item)
        elif item == '2':
            item = input('Choose an item to remove from shopping list:').strip().lower()
            if not item in shopping_list:
                print(f'Item not found')
            else:
                shopping_list.remove(item)
        elif item == '3':
            print(shopping_list)
        elif item == '4':
            print(f'Goodbye')
        else:
            print(f'Invalid choice. Please try again')
