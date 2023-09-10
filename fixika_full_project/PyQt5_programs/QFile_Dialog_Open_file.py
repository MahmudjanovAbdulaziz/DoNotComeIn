import sys
from PyQt5.QtWidgets import * #import section

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 300)

        self.btn_name = QPushButton('open file', self)
        self.btn_name.move(25, 25)
        self.btn_name.clicked.connect(self.evt_btn_clicked)

        self.btn_save = QPushButton('save file ', self)
        self.btn_save.move(25, 50)
        self.btn_save.clicked.connect(self.save_file)

    def evt_btn_clicked(self):
        res =QFileDialog.getOpenFileName(self, 'Open File', 'C:/', 'JPG File (*.jpg);;PNG File (*.png)')
        print(res)

    def save_file(self):
        res = QFileDialog.getSaveFileName(self, 'Open File', 'C:/', 'JPG File (*.jpg);;PNG File (*.png)')



if __name__ == "__main__":
    app = QApplication(sys.argv) # create run configuration
    dlgMain = DlgMain() #Create Main Gui Window
    dlgMain.show()  #sghow gui
    sys.exit(app.exec_())  # execute the run