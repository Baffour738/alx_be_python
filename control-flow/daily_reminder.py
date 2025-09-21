# def daily_reminder():
#     task = input("Enter your task: ")
#     priority = input("Priority (high/medium/low): ").lower()
#     time_bound = input("Is it time-bound? (yes/no): ").lower()
#     reminder_message = f"Note: '{task}' is a {priority} priority task."
#     match priority:
#         case 'high':
#             reminder_message = f"Reminder: '{task}' is a high priority task"
#             if time_bound == 'yes':
#                 reminder_message += " that requires immediate attention today!"
#             else:
#                 reminder_message += ". It should be completed as soon as possible."
#         case 'medium':
#             if time_bound == 'yes':
#                 reminder_message += " that should be done today."
#             else:
#                 reminder_message += ". Consider completing it soon."
#         case 'low':
#             if time_bound == 'yes':
#                 reminder_message += " that you should get done today."
#             else:
#                 reminder_message += ". Consider completing it when you have free time."
#         case _:
#             print("Invalid priority entered. Please choose from high, medium, or low.")
#             return
#     print(reminder_message)
# if __name__ == "__main__":
#     daily_reminder()


# daily_reminder.py

# Loop to keep asking until a valid input is given
while True:
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Match case for priority
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority entered. Please enter high, medium, or low.\n")
            continue  # restart the loop if invalid priority
    # Add time sensitivity check
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    elif time_bound == "no":
        reminder = "Note: " + reminder + ". Consider completing it when you have free time."
    else:
        print("Invalid input for time-bound. Please enter yes or no.\n")
        continue  # restart loop if invalid time input

    # Print the final reminder
    print("\nReminder:", reminder)
    break  # exit loop once we have a valid reminder
