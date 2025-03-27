import requests

class WeatherAPI:
    def __init__(self, api_key, base_url="http://api.openweathermap.org/data/2.5/weather"):
        """
        Initialize the WeatherAPI class with the API key and base URL.
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_weather_by_city(self, city_name):
        """
        Fetch weather data for a specific city.
        """
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "metric"  # Use "imperial" for Fahrenheit
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            return data
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def extract_weather_info(self, weather_data):
        """
        Extract and format key weather information from the API response.
        """
        if weather_data:
            city = weather_data["name"]
            temperature = weather_data["main"]["temp"]
            weather_description = weather_data["weather"][0]["description"]
            return f"City: {city}, Temperature: {temperature}°C, Weather: {weather_description}"
        else:
            return "No data available."

# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    api_key = "5f5c5a9bbd6f6db4d60ed3c87bee520e"
    city = "Stafford"

    weather_api = WeatherAPI(api_key)
    weather_data = weather_api.get_weather_by_city(city)
    formatted_weather_info = weather_api.extract_weather_info(weather_data)

    print(formatted_weather_info)
