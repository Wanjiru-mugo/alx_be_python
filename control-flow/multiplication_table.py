#program asks user for random number and creates a multiplication table for that number running from 1-10
number = int(input('Enter a number to see its multiplication table: '))
i = 1
for i in range(1, 11):
    product = number * i
    print(f'{number} * {i} = {product}')
    print()
