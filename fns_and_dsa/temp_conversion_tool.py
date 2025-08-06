FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 #global var
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5 #global var

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    farenheit = temp
    return farenheit * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    celsius = temp
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

temp = int(input('Enter the temperature to convert: '))
ans = input('Is this temperature in Celsius or Farenheit? (C/F): ').upper().strip()
if ans == 'F':
    new_temp = convert_to_celsius(temp)
    print(new_temp)
elif ans == 'C':
    new_temp = convert_to_celsius(temp)
    print(new_temp)
else:
    print('Invalid temperature. Please enter a numeric value.')
