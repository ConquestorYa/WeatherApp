
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap, QImage, QPalette, QBrush, QFont
from PyQt6.QtWidgets import QLabel
import requests






class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName("WeatherApp")
        MainWindow.resize(640, 480)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")




        common_cities = QtWidgets.QCompleter([
            'New York, USA',
            'Los Angeles, USA',
            'London, UK',
            'Paris, France',
            'Tokyo, Japan',
            'Sydney, Australia',
            'Toronto, Canada',
            'Berlin, Germany',
            'Rome, Italy',
            'Beijing, China',
            'Cairo, Egypt',
            'Moscow, Russia',
            'Rio de Janeiro, Brazil',
            'Cape Town, South Africa',
            'Mumbai, India',
            'Dubai, UAE',
            'Mexico City, Mexico',
            'Buenos Aires, Argentina',
            'Seoul, South Korea',
            'Stockholm, Sweden',
            'Helsinki, Finland',
            'Oslo, Norway',
            'Athens, Greece',
            'Amsterdam, Netherlands',
            'Brussels, Belgium',
            'Vienna, Austria',
            'Zurich, Switzerland',
            'Prague, Czech Republic',
            'Bangkok, Thailand',
            'Singapore, Singapore',
            'Istanbul, Turkey',
            'Dublin, Ireland'
        ])

        common_cities.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)

        self.input_field = QtWidgets.QLineEdit(
                                               parent=self.centralwidget,
                                               placeholderText="enter city or country name you want to search...",
                                               clearButtonEnabled=True)

        self.input_field.setMinimumSize(QtCore.QSize(300, 30))
        self.input_field.setCompleter(common_cities)
        self.input_field.setGeometry(QtCore.QRect(80, 40, 481, 41))
        self.input_field.setObjectName("input_field")
        self.input_field.returnPressed.connect(self.getWeatherInfo)

        palette = QPalette()
        background_image = QPixmap("background.png")
        scaled_background = background_image.scaled(MainWindow.size(), QtCore.Qt.AspectRatioMode.IgnoreAspectRatio)
        palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_background))
        MainWindow.setPalette(palette)

        """
        self.output_field = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.output_field.setGeometry(QtCore.QRect(80, 110, 250, 300))
        self.output_field.setObjectName("output_field")
        """

        self.output_text = QLabel(self.centralwidget)
        self.output_text.setFont(QFont("BlockKie", 13))
        self.output_text.setGeometry(QtCore.QRect(80, 110, 250, 300))
        self.output_text.setObjectName("output_text")

        self.img_lbl = QLabel(self.centralwidget)
        #self.pixmap = QPixmap('ClearSky_small.png')
        #self.img_lbl.setGeometry(410, 150, self.pixmap.width(), self.pixmap.height())
        #self.img_lbl.setPixmap(self.pixmap)

        self.city_name = QLabel(self.centralwidget)
        self.city_name.setFont(QFont("Autum Bright", 25))
        self.city_name.setGeometry(QtCore.QRect(80, 20, 300, 300))
        self.city_name.setObjectName("city_name")

        self.banner = QLabel(self.centralwidget)
        self.banner.setFont(QFont("Autum Bright", 25))
        self.banner.setGeometry(QtCore.QRect(170, 20, 460, 270))
        self.banner.setObjectName("banner")
        self.banner.setText("Weather Application")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def getWeatherInfo(self):

        apiKey = "YOUR_API_KEY"
        city = self.input_field.text()
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={apiKey}"
        response = requests.get(url)


        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            description = data['weather'][0]['description']

            self.output_text.setText(str(f'Temperature: {temperature} C\nDescription: {description}'))
            self.setImage(description)
            print(len(city))

            self.city_name.setText(city.capitalize())

        else:
            self.city_name.setText('')
            self.output_text.setText('Requested region not found!')

    def setImage(self, status):

        if status == "clear sky":
            self.image = "ClearSky"

        elif status == "light rain" or status == "moderate rain":
            self.image = "LightRain"

        elif status == "light intensity shower rain":
            self.image = "lightIntensityShowerRain"

        elif status == "few clouds" or status == "overcast clouds":
            self.image = "fewClouds"

        elif status == "broken clouds":
            self.image = "brokenClouds"

        elif status == "scattered clouds":
            print('hello')
            self.image = "scatteredClouds"

        elif status == "thunderstorm with light rain":
            self.image = "twlr"

        elif status == "smoke" or status == "fog":
            self.image = "Smoke"

        else:
            self.image = "questionMark"

        self.banner.clear()

        if self.image:
            self.pixmap = QPixmap(self.image + ".png")
            self.img_lbl.setGeometry(410, 150, self.pixmap.width(), self.pixmap.height())
            self.img_lbl.setPixmap(self.pixmap)
        print(status)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("WeatherApp", "WeatherApp"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
