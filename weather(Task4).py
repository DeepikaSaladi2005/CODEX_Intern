from flask import Flask, render_template, request
import requests

app = Flask(__name__)

WEATHER_API_KEY = "8c2ae2725a5727448f1b874e3c7292fa"

def fetch_weather(city):
    """Fetch real-time weather data for a given city using WeatherAPI."""
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": WEATHER_API_KEY,
        "q": city,
        "aqi": "no"
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "city": data['location']['name'],
            "temperature": data['current']['temp_c'],
            "humidity": data['current']['humidity'],
            "condition": data['current']['condition']['text'],
            "icon": data['current']['condition']['icon']
        }
        return weather_info
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        weather_data = fetch_weather(city)
    return render_template("index2.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
