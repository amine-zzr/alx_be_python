# daily_reminder.py
# A simple script to provide a task reminder based on priority and time sensitivity.

def daily_reminder():
    """
    Prompts the user for a single task and provides a customized reminder.
    """
    # 1. Prompt for a Single Task
    task = input("Enter your task: ")

    # 2. Prompt for Priority (with a validation loop)
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ["high", "medium", "low"]:
            break # Exit the loop if input is valid
        else:
            print("Invalid input. Please enter high, medium, or low.")

    # 3. Prompt for Time Sensitivity (with a validation loop)
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ["yes", "no"]:
            break # Exit the loop if input is valid
        else:
            print("Invalid input. Please enter yes or no.")

    # 4. Process the Task and Provide a Customized Reminder
    print("") # Add a blank line for better readability

    # Use an 'if' statement to handle the most urgent case first
    if time_bound == "yes":
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    else:
        # If not time-bound, use a 'match' statement for different priorities
        match priority:
            case "high":
                print(f"Reminder: '{task}' is a high priority task. Try to complete it soon.")
            case "medium":
                print(f"Note: '{task}' is a medium priority task. Plan to get it done.")
            case "low":
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

# This ensures the script runs only when executed directly
if __name__ == "__main__":
    daily_reminder()
