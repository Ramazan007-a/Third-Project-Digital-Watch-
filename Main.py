import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt
from PyQt5.QtGui import QFont,QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_Label = QLabel(self)
        self.timer=QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(250,400,900,200)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_Label)
        self.setLayout(vbox)

        self.time_Label.setAlignment(Qt.AlignCenter)

        self.time_Label.setStyleSheet("font-size:250px;"
                                      "color: hsl(225, 100%, 30%);")
        self.setStyleSheet("background-color: rgb(255, 255, 0);")

        font_id=QFontDatabase.addApplicationFont("DS-DIGI.TTF")
        font_family=QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font=QFont(font_family, 150)
        self.time_Label.setFont(my_font)


        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_Label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())


