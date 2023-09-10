from PyQt5 import QtCore, QtGui, QtWidgets
from hend import Ui_Dialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1247, 775)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(420, -1, 500, 711))
        self.frame.setStyleSheet("background-color: rgb(124, 253, 255);\n"
                                 "border-radius: 100px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 30, 331, 51))
        self.label.setStyleSheet("font: 75 14pt \"Arial\";")
        self.label.setObjectName("label")
        self.input_line = QtWidgets.QLineEdit(self.frame)
        self.input_line.setGeometry(QtCore.QRect(70, 80, 291, 31))
        self.input_line.setStyleSheet("color: rgb(0, 255, 0);\n"
                                      "font: 14pt \"Arial\";\n"
                                      "background-color: rgb(170, 255, 255);\n"
                                      "")
        self.input_line.setObjectName("input_line")
        self.input_line.textChanged.connect(self.radiation_input_)
        self.btn_search = QtWidgets.QPushButton(self.frame)
        self.btn_search.setGeometry(QtCore.QRect(380, 80, 91, 31))
        self.btn_search.setStyleSheet("font: 75 36pt \"Arial\";\n"
                                      "color: rgb(0, 255, 8);")
        self.btn_search.setObjectName("btn_search")
        self.btn_search.clicked.connect(self.searche_radiation)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 41, 20))
        self.label_3.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 81, 20))
        self.label_5.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(50, 240, 51, 20))
        self.label_6.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(50, 270, 121, 20))
        self.label_7.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.calculate = QtWidgets.QPushButton(self.frame)
        self.calculate.setGeometry(QtCore.QRect(30, 640, 441, 41))
        self.calculate.setStyleSheet("font: 14pt \"Arial\";\n"
                                     "color: rgb(15, 255, 91);")
        self.calculate.setObjectName("calculate")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(110, 180, 47, 13))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.azot = QtWidgets.QLabel(self.frame)
        self.azot.setGeometry(QtCore.QRect(100, 181, 47, 20))
        self.azot.setStyleSheet("font: italic 10pt \"Arial\";")
        self.azot.setObjectName("azot")
        self.cislorod = QtWidgets.QLabel(self.frame)
        self.cislorod.setGeometry(QtCore.QRect(130, 210, 47, 16))
        self.cislorod.setStyleSheet("font: italic 10pt \"Arial\";")
        self.cislorod.setObjectName("cislorod")
        self.argon = QtWidgets.QLabel(self.frame)
        self.argon.setGeometry(QtCore.QRect(110, 240, 47, 21))
        self.argon.setStyleSheet("font: italic 10pt \"Arial\";")
        self.argon.setObjectName("argon")
        self.carbon_dioxid = QtWidgets.QLabel(self.frame)
        self.carbon_dioxid.setGeometry(QtCore.QRect(170, 270, 47, 20))
        self.carbon_dioxid.setStyleSheet("font: italic 10pt \"Arial\";")
        self.carbon_dioxid.setObjectName("carbon_dioxid")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(50, 150, 181, 21))
        self.label_8.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(50, 330, 81, 31))
        self.label_9.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.radiation = QtWidgets.QLabel(self.frame)
        self.radiation.setGeometry(QtCore.QRect(150, 340, 300, 20))
        self.radiation.setStyleSheet("font: italic 10pt \"Arial\";")
        self.radiation.setText("")
        self.radiation.setObjectName("radiation")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(0, 300, 501, 20))
        self.label_10.setObjectName("label_10")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(930, 630, 311, 61))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.radiation_input = ''
        self.osh = '0.17Mk'
        self.bishkek = '0,16mk'
        self.batken = '0,13mk'
        self.djalal_abad = '0,17mk'
        self.naryn = '0,19mk'
        self.talas = '0.18Mk'
        self.issik_kul = '0.17mk'
        self.kyrgyzstan = '1000-1700 квтч/м2'
        self.else_ = 'Неправильный запрос!'
        self.calculate.clicked.connect(open_window)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Radiation"))
        self.label.setText(_translate("MainWindow", "Введите название города или района: "))
        self.btn_search.setText(_translate("MainWindow", "→"))
        self.label_3.setText(_translate("MainWindow", "Азот:"))
        self.label_5.setText(_translate("MainWindow", "Кислород:"))
        self.label_6.setText(_translate("MainWindow", "Аргон:"))
        self.label_7.setText(_translate("MainWindow", "Углекислый Газ:"))
        self.calculate.setText(_translate("MainWindow", "Вычеслить самому:"))
        self.azot.setText(_translate("MainWindow", "78%"))
        self.cislorod.setText(_translate("MainWindow", "20%"))
        self.argon.setText(_translate("MainWindow", "0.93%"))
        self.carbon_dioxid.setText(_translate("MainWindow", "0.031%"))
        self.label_8.setText(_translate("MainWindow", "Состав воздуха:"))
        self.label_9.setText(_translate("MainWindow", "Радиация:"))
        self.label_10.setText(_translate("MainWindow",
                                         "----------------------------------------------------------------------------------------------------------------------------"))
        self.label_2.setText(_translate("MainWindow", "Примечание: \n"
                                                      "1)В базе данных присуствует информация только \n"
                                                      "КР другая информация о других странах отсуствует\n"
                                                      "2)Данные являются средне статистическими и \n"
                                                      " являются верными не менее чем на 88%"))

    def searche_radiation(self):
        global radiation_input
        if self.radiation_input == 'ош':
            self.radiation.setText(self.osh)
        elif self.radiation_input == 'бишкек':
            self.radiation.setText(self.bishkek)
        elif self.radiation_input == 'баткен':
            self.radiation.setText(self.batken)
        elif self.radiation_input == 'джалал-абад':
            self.radiation.setText(self.djalal_abad)
        elif self.radiation_input == 'нарын':
            self.radiation.setText(self.naryn)
        elif self.radiation_input == 'талас':
            self.radiation.setText(self.talas)
        elif self.radiation_input == 'иссык-куль':
            self.radiation.setText(self.issik_kul)
        elif self.radiation_input == 'кыргызстан':
            self.radiation.setText(self.kyrgyzstan)
        else:
            self.radiation.setText(self.else_)

    def radiation_input_(self, text):
        global radiation_input
        self.radiation_input = text



def open_window():
    global Dialog
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.setWindowTitle('Самостоятельное вычесление')
    # MainWindow.hide()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
