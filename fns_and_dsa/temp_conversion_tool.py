FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

temp = float(input("Enter the temperature to convert: "))
c_or_f = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))

if c_or_f.lower() == "f":
    print(f"{temp}°F is {convert_to_celsius(temp)}°C")
elif c_or_f.lower() == "c":
    print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
else:
    print ("Invalid temperature. Please enter a numeric value.")