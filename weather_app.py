import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    api_key = "9b755d7c7b7e174bea91f31034dec092"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data["cod"] != 200:
            messagebox.showerror("Error", data["message"])
            return
        
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        weather_label.config(text=f"Weather: {weather}")
        temp_label.config(text=f"Temperature: {temp}°C")
        humidity_label.config(text=f"Humidity: {humidity}%")
        wind_label.config(text=f"Wind Speed: {wind_speed} m/s")
    
    except Exception as e:
        messagebox.showerror("Error", "Failed to retrieve data")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x300")

city_entry = tk.Entry(root, width=20)
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Get Weather", command=get_weather)
search_button.pack(pady=5)

weather_label = tk.Label(root, text="Weather: ")
weather_label.pack(pady=5)

temp_label = tk.Label(root, text="Temperature: ")
temp_label.pack(pady=5)

humidity_label = tk.Label(root, text="Humidity: ")
humidity_label.pack(pady=5)

wind_label = tk.Label(root, text="Wind Speed: ")
wind_label.pack(pady=5)

root.mainloop()
