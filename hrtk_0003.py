import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    try:
        data = response.json()
    except Exception:
        return None

    if response.status_code == 200 and data.get("cod") != "404":
        weather = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']} °C",
            "Humidity": f"{data['main']['humidity']}%",
            "Condition": data["weather"][0]["description"].capitalize()
        }
        return weather
    else:
        return None

def main():
    print("=== 🌦️ Weather Info App ===")
    api_key = input("🔑 Enter your OpenWeatherMap API key: ").strip()

    while True:
        city = input("\n🏙️ Enter city name (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("👋 Exiting the Weather Info App. Goodbye!")
            break

        weather = get_weather(city, api_key)
        if weather:
            print("\n--- ✅ Weather Report ---")
            for key, value in weather.items():
                print(f"{key}: {value}")
        else:
            print("❌ City not found or invalid API key. Please try again using the format 'City,CountryCode' (e.g., Amravati,IN)")

if __name__ == "__main__":
    main()