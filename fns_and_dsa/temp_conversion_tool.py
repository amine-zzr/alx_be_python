# temp_conversion_tool.py

# --- Part 1: Define Global Conversion Factors ---
# These variables are in the global scope, so they are accessible
# for reading inside any function defined below.
FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)


# --- Part 2: Implement Conversion Functions ---

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global factor.
    Formula: C = (F - 32) * (5/9)
    """
    # We are accessing the global variable FAHRENHEIT_TO_CELSIUS_FACTOR here.
    # No 'global' keyword is needed because we are only reading it.
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global factor.
    Formula: F = (C * 9/5) + 32
    """
    # We are accessing the global variable CELSIUS_TO_FAHRENHEIT_FACTOR here.
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# --- Part 3: User Interaction ---

def main():
    """
    Main function to handle user input and display results.
    """
    
    # Get temperature and validate it
    try:
        temp_input = input("Enter the temperature to convert: ")
        # Convert the input to a float (number with decimals)
        temperature = float(temp_input)
    except ValueError:
        # This block runs if float(temp_input) fails
        # This fulfills the error handling requirement
        print("Invalid temperature. Please enter a numeric value.")
        return # Exit the function

    # Get the unit and normalize it (remove whitespace, make uppercase)
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Call the correct function based on the unit
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        # Display the result in the required format
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        # Display the result in the required format
        print(f"{temperature}°C is {converted_temp}°F")
    else:
        # Handle invalid unit input
        print("Invalid unit. Please enter 'C' or 'F'.")

# Standard Python practice to run the main() function
if __name__ == "__main__":
    main()
