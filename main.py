import requests
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Replace 'WEATHER_API_KEY' with your openweathermap.org API key
WEATHER_API_KEY = ""
CITY_NAME = "lagos"
# Replace 'WEATHER_API_KEY' with your exchangeratesapi.io API key
EXCHANGE_RATE_API_KEY = ""


class WeatherApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="HNG App")
        self.set_default_size(300, 150)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.get_weather_btn = Gtk.Button(label="Get Weather Forecast for Lagos")
        self.get_currency_btn = Gtk.Button(label="Get current NGN/USD rates")

        self.result_label = Gtk.Label(label="Weather In Lagos: ")
        self.result_conversion_label = Gtk.Label(label="Naira/USD: ")

        self.grid.attach(self.get_weather_btn, 0, 0, 1, 1)
        self.grid.attach(self.get_currency_btn, 0, 1, 1, 1)
        self.grid.attach(self.result_label, 0, 2, 1, 1)
        self.grid.attach(self.result_conversion_label, 0, 3, 1, 1)

        self.get_weather_btn.connect("clicked", self.update_weather)
        self.get_currency_btn.connect("clicked", self.convert_currency)

    def get_weather(self):
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={WEATHER_API_KEY}"
            response = requests.get(url)
            data = response.json()
            weather = data["weather"][0]["description"]
            return weather.capitalize()
        except Exception as e:
            return f"Error: {str(e)}"

    def convert_currency(self, widget):
        try:
            url = f"http://api.exchangeratesapi.io/latest?access_key={EXCHANGE_RATE_API_KEY}&from=USD&to=NGN"
            response = requests.get(url)
            data = response.json()
            exchange_rate = data["rates"]["NGN"]
            self.result_conversion_label.set_text(f"Naira/USD: ₦{exchange_rate:.2f}")
        except Exception as e:
            self.result_conversion_label.set_text(f"Error: {str(e)}")

    def update_weather(self, widget):
        weather_text = self.get_weather()
        self.result_label.set_text(f"Weather In Lagos: {weather_text}")
        return True


if __name__ == "__main__":
    app = WeatherApp()
    app.connect("delete-event", Gtk.main_quit)
    app.show_all()
    Gtk.main()
