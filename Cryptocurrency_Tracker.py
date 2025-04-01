from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton, QComboBox
from PyQt5 import uic
import sys
import requests
import res
import json


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the ui file
        uic.loadUi("Cryptocurrency_Tracker.ui", self)

        # Define Our Widgets
        self.comboBox = self.findChild(QComboBox, "comboBox")
        self.textEdit = self.findChild(QTextEdit, "textEdit")
        self.set_crypto_bt = self.findChild(QPushButton, "set_crypto_bt")

        # Do something
        self.set_crypto_bt.clicked.connect(self.set_crypto)

        # Show The App
        self.show()


    def get_data(self, id):
        """
        This function gets data from cryptocurrency API.
        Then loads data with json
        Finally returns data.
        The parameter that this function getting is id and use that for get data from API.
        """
        request_data = requests.get(f"https://api.coinlore.net/api/ticker/?id={id}")
        loud_data = json.loads(request_data.text)
        data = loud_data[0]
        return data


    def set_crypto(self):
        """
        This function calls by set_crypto_bt
        And send id to get_data function Then call that by selected item from QComboBox
        Finally get data from previous function and show it to user
        """
        if self.comboBox.currentText() == 'BTC':
            data = self.get_data(90)
        elif self.comboBox.currentText() == 'ETH':
            data = self.get_data(80)
        elif self.comboBox.currentText() == 'USDT':
            data = self.get_data(518)
        elif self.comboBox.currentText() == 'XRP':
            data = self.get_data(58)
        elif self.comboBox.currentText() == 'BNB':
            data = self.get_data(2710)
        elif self.comboBox.currentText() == 'SOL':
            data = self.get_data(48543)
        elif self.comboBox.currentText() == 'DOGE':
            data = self.get_data(2)
        elif self.comboBox.currentText() == 'ADA':
            data = self.get_data(257)

        self.textEdit.setText(f"you picked {data['name']}")
        self.textEdit.append(f"{data['name']} price is: {data['price_usd']}")
        self.textEdit.append(f"{data['name']} percent change in 1h is:  {data['percent_change_1h']}%")
        self.textEdit.append(f"{data['name']} percent change in 24h is: {data['percent_change_24h']}%")
        self.textEdit.append(f"{data['name']} percent change in 7d is:  {data['percent_change_7d']}%")
        print(data)


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
