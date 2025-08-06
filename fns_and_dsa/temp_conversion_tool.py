FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9 #global var
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5 #global var

def convert_to_celsius(fahrenheit):
    fahrenheit = temp
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    celsius = temp
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

temp = int(input('Enter the temperature to convert: '))
ans = input('Is this temperature in Celsius or Farenheit? (C/F): ').upper().strip()
if ans == 'F':
    new_temp = convert_to_celsius(temp)
    print(new_temp)
elif ans == 'C':
    new_temp = convert_to_fahrenheit(temp)
    print(new_temp)
else:
    print('Invalid temperature. Please enter a numeric value.')
