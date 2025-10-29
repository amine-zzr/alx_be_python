FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):

    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():

    try:
        temper = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    specify = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if specify == "C":
        result = convert_to_fahrenheit(temper)
        print(f"{temper}°C is {result}°F")

    elif specify == "F":
        result = convert_to_celsius(temper)
        print(f"{temper}°F is {result}°C")

    else:
        print("Please choose F or C")

if __name__ == "__main__":
    main()
