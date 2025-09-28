# temp_conversion_tool.py
"""
Temperature Conversion Tool
Demonstrates variable scope using global conversion factors
"""

# Global conversion factors - accessible throughout the script
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using global conversion factor
    
    Args:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature in Celsius
    """
    # Access global variable without 'global' keyword since we're only reading
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using global conversion factor
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    """
    # Access global variable without 'global' keyword since we're only reading
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def get_temperature_input():
    """
    Get temperature input from user with validation
    
    Returns:
        float: Valid temperature value
    
    Raises:
        ValueError: If input is not a valid number
    """
    try:
        temp_str = input("Enter the temperature to convert: ")
        temperature = float(temp_str)
        return temperature
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

def get_unit_input():
    """
    Get temperature unit from user with validation
    
    Returns:
        str: 'C' for Celsius or 'F' for Fahrenheit
    
    Raises:
        ValueError: If input is not 'C' or 'F'
    """
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper().strip()
    if unit not in ['C', 'F']:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    return unit

def main():
    """
    Main function to run the temperature conversion tool
    """
    try:
        # Get user input
        temperature = get_temperature_input()
        unit = get_unit_input()
        
        # Perform conversion based on input unit
        if unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        else:  # unit == 'C'
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
