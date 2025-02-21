from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date

def calculate_future_date(user_val):
    future_date = datetime.now()
    future_date = future_date + timedelta(days=user_val)
    future_date = future_date.strftime("%Y-%m-%d")
    return future_date


print(f"Current date and time: {display_current_datetime()}")
no_days = int(input("Enter the number of days to add to the current date: "))
print(f"Future date: {calculate_future_date(no_days)}")