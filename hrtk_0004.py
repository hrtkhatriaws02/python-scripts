import requests

# Top 10 popular currencies with country names
TOP_CURRENCIES = {
    "USD": "United States Dollar",
    "EUR": "Euro (European Union)",
    "GBP": "British Pound Sterling",
    "JPY": "Japanese Yen",
    "INR": "Indian Rupee",
    "CAD": "Canadian Dollar",
    "AUD": "Australian Dollar",
    "CNY": "Chinese Yuan",
    "CHF": "Swiss Franc",
    "AED": "UAE Dirham"
}

def get_exchange_rate(base, target):
    url = f"https://api.frankfurter.app/latest?from={base}&to={target}"
    response = requests.get(url)
    data = response.json()
   # print(data)

    if "rates" in data and target in data["rates"]:
        return data["rates"][target]
    else:
        raise ValueError("Invalid currency code or API error.")

def convert_currency(amount, rate):
    return amount * rate

def main():
    print("💱 Welcome to Real-Time Currency Converter\n")

    # Display the top 10 currencies for user reference
    print("💱 Top 10 Currencies (Code — Country):")
    for code, name in TOP_CURRENCIES.items():
        print(f"{code} — {name}")
    print("=" * 75)

    base = input("Enter base currency code (e.g., USD): ").upper()
    if base not in TOP_CURRENCIES:
        print(f"❌ '{base}' is not in the supported list. Please choose from the list above.")
        return

    target = input("Enter target currency code (e.g., INR): ").upper()
    if target not in TOP_CURRENCIES:
        print(f"❌ '{target}' is not in the supported list. Please choose from the list above.")
        return

    try:
        amount = float(input(f"Enter amount in {base}: "))
        rate = get_exchange_rate(base, target)
        converted = convert_currency(amount, rate)
        print(f"\n✅ Result: {amount:.2f} {base} = {converted:.2f} {target}")
        print("=" * 75)
    except ValueError as e:
        print("❌ Error:", e)
    except Exception:
        print("❌ Something went wrong. Please check your internet connection or input.")

if __name__ == "__main__":
    main()
