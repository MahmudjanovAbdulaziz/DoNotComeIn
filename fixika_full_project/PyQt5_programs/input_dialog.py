import sys
from PyQt5.QtWidgets import * #import section

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200, 300)

        self.btn_name = QPushButton('Name input', self)
        self.btn_name.move(35, 50)
        self.btn_name.clicked.connect(self.evt_btn_clicked)

        self.btn_age = QPushButton('Age input', self)
        self.btn_age.move(35, 75)
        self.btn_age.clicked.connect(self.btn_age_input)

        self.btn_double = QPushButton('Your Height', self)
        self.btn_double.move(35, 100)
        self.btn_double.clicked.connect(self.your_rost)

        self.btn_color = QPushButton('Your favorite color', self )
        self.btn_color.move(35, 125)
        self.btn_color.clicked.connect(self.favorite_color)


    def evt_btn_clicked(self):
        s_name, b_ok = QInputDialog.getText(self, 'Title', 'Enter Your Name:')
        if b_ok:
            QMessageBox.information(self, 'Name', 'Your name is' + s_name)
        else:
            QMessageBox.critical(self, 'Cancal', 'User have clicked "Cancel"')

    def btn_age_input(self):
        i_age, b_ok = QInputDialog.getInt(self, 'Title', 'Enter Your Name:', 18, 18, 65, 1)
        if b_ok:
            QMessageBox.information(self, 'Age', 'Your age is ' + str(i_age))
        else:
            QMessageBox.critical(self, 'Cancal', 'User have clicked "Cancel"')

    def your_rost(self):
        d_height,  b_ok = QInputDialog.getDouble(self, 'Title', 'Enter your height in meters: ', 1.70, 0.50, 2.50, 2)
        if b_ok:
            QMessageBox.information(self, 'Height', 'Your Height is  '+ str(d_height))
        else:
            QMessageBox.critical(self, 'Canceled', 'User have clicked "Cancel"')

    def favorite_color(self):
        colors = ['red', 'green', 'lime', 'yellow', 'indigo', 'violet']
        s_color, b_ok = QInputDialog.getItem(self, 'Color', 'Enter your favorite color: ', colors ,editable=False)
#editable являетсязначением по умолчанию True где можно писать а когда значение равняется False нечего нельзя писать можно только выбирать

        if b_ok:
            QMessageBox.information(self, 'Color', 'Your favorite color is ' + s_color)
        else:
            QMessageBox.critical(self, 'Canceled', 'User have clicked "Cancel"')




if __name__ == "__main__":
    app = QApplication(sys.argv) # create run configuration
    dlgMain = DlgMain() #Create Main Gui Window
    dlgMain.show()  #sghow gui
    sys.exit(app.exec_())  # execute the run