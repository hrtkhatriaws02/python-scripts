from datetime import datetime
from dateutil.relativedelta import relativedelta  # requires installing dateutil

def calculate_age(birthdate_str):
    try:
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        today = datetime.today()

        if birthdate > today:
            return "❌ Birthdate cannot be in the future."

        diff = relativedelta(today, birthdate)

        print(f"\n🗓️ Date of Birth: {birthdate.date()}")
        print(f"📅 Today:        {today.date()}")
        print(f"\n🎉 You are {diff.years} years, {diff.months} months, and {diff.days} days old.")
    except ValueError:
        print("❌ Please enter the date in YYYY-MM-DD format.")

def main():
    dob = input("Enter your birthdate (YYYY-MM-DD): ")
    calculate_age(dob)

if __name__ == "__main__":
    main()
