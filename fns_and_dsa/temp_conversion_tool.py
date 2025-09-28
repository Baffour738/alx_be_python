# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Implement conversion functions
def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User interaction
def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)

        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        elif unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        else:
            # If unit is not C or F
            raise ValueError("Invalid unit.")
    except ValueError as e:
        # Must match exactly
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
