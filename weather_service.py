import requests

def get_live_weather():
    api_key = "bd5e378503939ddaee76f12ad7a97608" 
    city = "Vinnytsia"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ua"
    
    try:
        data = requests.get(url).json()
        temp = data['main']['temp']
        press = data['main']['pressure'] * 0.750062 
        wind = data['wind']['speed']
        humidity = data['main']['humidity']
        desc = data['weather'][0]['description']
        return {
            "temp": temp,
            "press": int(press),
            "wind": wind,
            "humidity": humidity,
            "desc": desc
        }
    except:
        return None