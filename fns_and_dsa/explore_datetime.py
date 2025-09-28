from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format as YYYY-MM-DD HH:MM:SS
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date  # return it so we can use it later

def calculate_future_date(current_date, days_to_add):
    # Add days to current date
    future_date = current_date + timedelta(days=days_to_add)
    # Format as YYYY-MM-DD
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Part 1: Display current datetime
    current_date = display_current_datetime()

    # Part 2: Ask user for days to add
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
