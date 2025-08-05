print('Shopping List Manager')

shopping_list = [] #declaring empty list; also shopping_list = list()

def display_menu():
    print('1. Add Item')
    print('2. Remove Item')
    print('3. View List')
    print('4. Exit')

    while True:
        item = input('Enter your choice (1-4): ').strip()

        if item == '1':
            item = input('Enter the item to add: ').strip().lower()
            shopping_list.append(item)
        elif item == '2':
            item = input('Enter the item to remove: ').strip().lower()
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
