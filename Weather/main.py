import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Weather App')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText('Enter city name')
        layout.addWidget(self.city_input)

        self.get_weather_btn = QPushButton('Get Weather', self)
        self.get_weather_btn.clicked.connect(self.fetch_weather)
        layout.addWidget(self.get_weather_btn)

        self.result_label = QLabel('', self)
        self.result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def fetch_weather(self):
        city = self.city_input.text()
        if city:
            api_key = 'api_key'  # Replace with your actual API key
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temp = data['main']['temp']
                weather_desc = data['weather'][0]['description']
                self.result_label.setText(f'Temperature: {temp}°C\nDescription: {weather_desc}')
            else:
                self.result_label.setText('City not found!')
        else:
            self.result_label.setText('Please enter a city name!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeatherApp()
    ex.show()
    sys.exit(app.exec_())
