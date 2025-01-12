FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

user_temp = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if unit == "F":
    print(f"{user_temp}°F is {convert_to_celsius(user_temp)}°C")
elif unit == "C":
    print(f"{user_temp}°C is {convert_to_fahrenheit(user_temp)}°F")
else:
    print("Error : Invalid input.")
