import sys
from PyQt5.QtWidgets import * #import section
from PyQt5.QtGui import *


class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 300)

        self.btn_color = QPushButton('Chooice Font', self )
        font = QFont('Arial', 10, 75, True)
        self.btn_color.setFont(font)
        self.btn_color.move(35, 50)
        self.btn_color.clicked.connect(self.evt_btn_clicked)


    def evt_btn_clicked(self):
        font, b_ok = QFontDialog.getFont()
        if b_ok:
            print(font.famaly())
            print(font.italic())
            print(font.bold())
            print(font.weight())
            print(font.pointSize())
            self.btn_color.setFont(font)




if __name__ == "__main__":
    app = QApplication(sys.argv) # create run configuration
    dlgMain = DlgMain() #Create Main Gui Window
    dlgMain.show()  #sghow gui
    sys.exit(app.exec_())  # execute the run