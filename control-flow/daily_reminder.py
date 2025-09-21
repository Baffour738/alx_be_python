from collections import deque

while True:
    # Get inputs from the user
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Validate and build the base message using match/case
    match priority:
        case "high":
            base_message = f"'{task}' is a high priority task"
        case "medium":
            base_message = f"'{task}' is a medium priority task"
        case "low":
            base_message = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority entered. Please enter high, medium, or low.\n")
            continue  # ask again

    # Time-sensitivity decides exact output wording and punctuation
    if time_bound == "yes":
        # Exact required format for time-bound tasks
        print(f"Reminder: {base_message} that requires immediate attention today!")
        break
    elif time_bound == "no":
        # Exact required format for non-time-bound tasks
        print(f"Note: {base_message}. Consider completing it when you have free time.")
        break
    else:
        print("Invalid input for time-bound. Please enter yes or no.\n")
        continue  # ask again

