#program prompts the user for 2 numbers and the operation to be performed and displays the result

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
operation = input('Choose the operation (+, -, *, /): ')

#the match expression
match operation:
    case "+":
        result = num1 + num2
        print(f'The result is {result}')
    case "-":
        result = num1 - num2
        print(f'The result is {result}')
    case "*":
        result = num1 * num2
        print(f'The result is {result}')
    case "/":
        result = num1 / num2
        #introduce a guard to handle division by 0
        if num2 == 0:
            print('Cannot divide by zero.')
        else:
            print(f'The result is {result}')
