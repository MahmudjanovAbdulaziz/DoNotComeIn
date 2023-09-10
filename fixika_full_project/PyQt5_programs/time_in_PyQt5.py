import sys
from PyQt5.QtWidgets import * #import section
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 300)

        self.btn_color = QPushButton('Data Time ', self )

        self.btn_color.move(35, 50)
        self.btn_color.clicked.connect(self.evt_btn_clicked)


    def evt_btn_clicked(self):
        dt = QDate.currentDate()
        print(dt.toString())
        print(dt.toJulianDay())
        print(dt.dayOfWeek())
        print(dt.dayOfYear())
        print(dt.daysInMonth())
        print(dt.addDays(21).toString())





if __name__ == "__main__":
    app = QApplication(sys.argv) # create run configuration
    dlgMain = DlgMain() #Create Main Gui Window
    dlgMain.show()  #sghow gui
    sys.exit(app.exec_())  # execute the run