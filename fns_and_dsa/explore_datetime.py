from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted)
    return now  # return the datetime object so it can be used

# Show current date and time
current = display_current_datetime()

# Ask the user for number of days
number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

# Call the function with the returned current date
calculate_future_date(current, number_of_days)