from datetime import datetime, date, time, timedelta

def main():
    # Current date and time
    now = datetime.now()
    print("Current datetime:", now)

    # Current date only
    today = date.today()
    print("Today's date:", today)

    # Current time only
    current_time = now.time()
    print("Current time:", current_time)

    # Create a specific date
    some_date = date(2025, 12, 31)
    print("Specific date:", some_date)

    # Create a specific time
    some_time = time(15, 30, 45)
    print("Specific time:", some_time)

    # Date arithmetic: Add 10 days
    future_date = today + timedelta(days=10)
    print("Date after 10 days:", future_date)

    # Date arithmetic: Subtract 5 days
    past_date = today - timedelta(days=5)
    print("Date 5 days ago:", past_date)

    # Difference between two dates
    diff = some_date - today
    print(f"Days until {some_date}: {diff.days} days")

    # Formatting dates
    formatted = now.strftime("%A, %d %B %Y %I:%M %p")
    print("Formatted datetime:", formatted)

    # Parsing date from string
    date_str = "2025-06-23 14:45:00"
    parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    print("Parsed datetime from string:", parsed_date)

    # US format date
    us_format = now.strftime("%m/%d/%Y")  # Month/Day/Year
    print("US format date:", us_format)

if __name__ == "__main__":
    main()
