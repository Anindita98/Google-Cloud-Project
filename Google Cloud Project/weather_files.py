from pytz import timezone
from pytz import timezone
def fetch_weather_data(cities):
    berlin_timezone = timezone("Europe/Berlin")
    API_Key = "........."
    weather_items = []
    for city in cities:
        country = "DE"
        geo_url = (f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&limit=20&appid={API_Key}")
        geo_response = requests.get(geo_url)
        geo_json = geo_response.json()
        latitude = geo_json[0]["lat"]
        longitude = geo_json[0]["lon"]
        weather_url = (f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={API_Key}&units=metric")
        weather_response = requests.get(weather_url)
        weather_json = weather_response.json()
        retrieval_time = datetime.now(berlin_timezone).strftime("%y-%m-%d %H:%M:%S")
        for item in weather_json["list"]:
            weather_item = {
                "City" :city,
                "Forecast_item": item.get("dt_txt"),
                "Temperature_celcious": item["main"].get("temp"),
                "Forecast": item["weather"][0].get("main"),                         
                "Rain_in_last_3h": item.get("rain", {}).get("3h", 0),
                "Wind_speed": item["wind"].get("speed"),
                "Data_retrieved_at": retrieval_time
            }
            weather_items.append(weather_item)
    weather_df = pd.DataFrame(weather_items)
    return weather_df
          