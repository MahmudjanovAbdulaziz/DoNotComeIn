import sys
from PyQt5.QtWidgets import * #import section

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second GUI") #set widets, set properties
        self.resize(300, 200)

        self.ledText = QLineEdit('Default Text', self)
        self.ledText.move(90, 50)

        self.btnUpdate = QPushButton('Update Window Title', self)
        self.btnUpdate.move(80, 70)
        self.btnUpdate.clicked.connect(self.btn_Title_update)

    def btn_Title_update(self):
        self.setWindowTitle(self.ledText.text())




if __name__ == "__main__":
    app = QApplication(sys.argv) # create run configuration
    dlgMain = DlgMain() #Create Main Gui Window
    dlgMain.show()  #sghow gui
    sys.exit(app.exec_())  # execute the run