from datetime import datetime, timedelta

def display_current_datetime():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_time}")

def calculate_future_date():
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    today = datetime.now()

    future_date = today + timedelta(days=days_to_add)

    formatted_future_date = future_date.strftime("%Y-%m-%d")

    print(f"Future date: {formatted_future_date}")

def main():
    display_current_datetime()

    print("-" * 30)

    calculate_future_date()

if __name__ == "__main__":
    main()

