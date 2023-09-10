from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QUrl
from hend import Ui_Dialog
from about_as import Ui_Dialog2
from about_dialog import Ui_about_radiation
from calendar import Ui_Dialog3
from graf import Ui_Dialog4
from input_line import Ui_Dialog7



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1247, 775)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/add_circle_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calculate.setIcon(icon)
        self.calculate.setObjectName("calculate")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(110, 180, 47, 13))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.azot = QtWidgets.QLabel(self.frame)
        self.azot.setGeometry(QtCore.QRect(100, 181, 47, 20))
        self.azot.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";")
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
        self.radiation = QtWidgets.QLabel(self.frame)
        self.radiation.setGeometry(QtCore.QRect(150, 340, 300, 20))
        self.radiation.setStyleSheet("font: italic 10pt \"Arial\";")
        self.radiation.setText("")
        self.radiation.setObjectName("radiation")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(0, 300, 501, 20))
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(260, 150, 161, 21))
        self.label_13.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(260, 180, 161, 41))
        self.label_14.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(420, 190, 31, 41))
        self.label_15.setStyleSheet("font: italic 10pt \"Arial\";")
        self.label_15.setObjectName("label_15")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(50, 340, 91, 21))
        self.label_9.setStyleSheet("font: italic 13pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(0, 120, 501, 20))
        self.label_11.setObjectName("label_11")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(930, 590, 321, 91))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255, 30);font: 75 10pt \"Arial\";\n"
                                   "border: 1px solid rgba(255, 255, 255, 40);\n"
                                   "border-radius:7px;")
        self.label_2.setObjectName("label_2")
        self.avary_list = QtWidgets.QPushButton(self.centralwidget)
        self.avary_list.setEnabled(True)
        self.avary_list.setGeometry(QtCore.QRect(61, 132, 351, 31))
        self.avary_list.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                      "border: 1px solid rgba(255, 255, 255, 40);\n"
                                      "border-radius: 7px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/publick_off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.avary_list.setIcon(icon1)
        self.avary_list.setObjectName("avary_list")
        self.calendar = QtWidgets.QPushButton(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(930, 116, 101, 41))
        self.calendar.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                    "border: 1px solid(255, 255, 255, 40);\n"
                                    "border-radius:7px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/calendar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calendar.setIcon(icon2)
        self.calendar.setObjectName("calendar")
        self.viktorino = QtWidgets.QPushButton(self.centralwidget)
        self.viktorino.setGeometry(QtCore.QRect(930, 164, 91, 41))
        self.viktorino.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                     "border: 1px solid(255, 255, 255, 40);\n"
                                     "border-radius:7px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/quiz.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viktorino.setIcon(icon3)
        self.viktorino.setObjectName("viktorino")
        self.graf = QtWidgets.QPushButton(self.centralwidget)
        self.graf.setGeometry(QtCore.QRect(930, 212, 81, 41))
        self.graf.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                "border: 1px solid(255, 255, 255, 40);\n"
                                "border-radius:7px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/monitoring.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.graf.setIcon(icon4)
        self.graf.setObjectName("graf")
        self.about_as = QtWidgets.QPushButton(self.centralwidget)
        self.about_as.setGeometry(QtCore.QRect(930, 260, 71, 41))
        self.about_as.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                        "border: 1px solid(255, 255, 255, 40);\n"
                                        "border-radius:7px;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_as.setIcon(icon5)
        self.about_as.setObjectName("pushButton_5")
        self.online_chat = QtWidgets.QPushButton(self.centralwidget)
        self.online_chat.setEnabled(True)
        self.online_chat.setGeometry(QtCore.QRect(61, 180, 351, 31))
        self.online_chat.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                       "border: 1px solid rgba(255, 255, 255, 40);\n"
                                       "border-radius: 7px;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/group_add_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.online_chat.setIcon(icon6)
        self.online_chat.setObjectName("online_chat")
        self.mchs_call = QtWidgets.QPushButton(self.centralwidget)
        self.mchs_call.setEnabled(True)
        self.mchs_call.setGeometry(QtCore.QRect(61, 228, 351, 31))
        self.mchs_call.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                     "border: 1px solid rgba(255, 255, 255, 40);\n"
                                     "border-radius: 7px;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/support-agent.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mchs_call.setIcon(icon7)
        self.mchs_call.setObjectName("mchs_call")
        self.radiation_about = QtWidgets.QPushButton(self.centralwidget)
        self.radiation_about.setEnabled(True)
        self.radiation_about.setGeometry(QtCore.QRect(61, 276, 351, 31))
        self.radiation_about.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                           "border: 1px solid rgba(255, 255, 255, 40);\n"
                                           "border-radius: 7px;")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/oil.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiation_about.setIcon(icon8)
        self.radiation_about.setObjectName("radiation_about")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.graf

        self.radiation_input = ''
        self.osh = '0.17Mk'
        self.osh_ = 'osh'
        self.bishkek = '0,16mk'
        self.batken = '0,13mk'
        self.djalal_abad = '0,17mk'
        self.naryn = '0,19mk'
        self.talas = '0.18Mk'
        self.issik_kul = '0.17mk'
        self.kyrgyzstan = '1000-1700 квтч/м2'
        self.else_ = 'Неправильный запрос!'
        self.calculate.clicked.connect(open_window)
        self.about_as.clicked.connect(open_about_as)
        self.radiation_about.clicked.connect(open_about_dialog)
        self.calendar.clicked.connect(open_calendar)
        self.graf.clicked.connect(open_graf)
        self.avary_list.clicked.connect(open_wikipedia)
        self.mchs_call.clicked.connect(open_mchs)
        self.online_chat.clicked.connect(dialog_input)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Radiation Zone!!!"))
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
        self.label_10.setText(_translate("MainWindow", "----------------------------------------------------------------------------------------------------------------------------"))
        self.label_13.setText(_translate("MainWindow", "Солнечная радиация:"))
        self.label_14.setText(_translate("MainWindow", "Температура при \n"
                                                       "солнечной радиации:"))
        self.label_15.setText(_translate("MainWindow", "80°С"))
        self.label_9.setText(_translate("MainWindow", "Радиация:"))
        self.label_11.setText(_translate("MainWindow", "----------------------------------------------------------------------------------------------------------------------------"))
        self.label_2.setText(_translate("MainWindow", "Примечание: \n"
                                                      "1)В базе данных присуствует информация только \n"
                                                      "КР другая информация о других странах отсуствует\n"
                                                      "2)Данные являются средне статистическими и \n"
                                                      " являются верными не менее чем на 78%"))
        self.avary_list.setText(_translate("MainWindow", "Списки аварий за все время:"))
        self.calendar.setText(_translate("MainWindow", "Календарь!"))
        self.viktorino.setText(_translate("MainWindow", "Опросник"))
        self.graf.setText(_translate("MainWindow", "График"))
        self.about_as.setText(_translate("MainWindow", "О нас!"))
        self.online_chat.setText(_translate("MainWindow", "Ввести данные..."))
        self.mchs_call.setText(_translate("MainWindow", "Oповестить мчс"))
        self.radiation_about.setText(_translate("MainWindow", "Узнать подробнее о радиации..."))

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
        self.input_line = text
        self.radiation_input = text
    def open_python_file(self):
        # file_name = 'C:\Users\User\PycharmProjects\fixika_full_project\web_site/online_chat.py'
        pass



def open_window():
    global Dialog
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    Dialog.setWindowTitle('Самостоятельное вычесление')
    # MainWindow.hide()



def open_about_as():
    global Dialog2
    Dialog2 = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()



def open_about_dialog():
    global about_radiation
    about_radiation = QtWidgets.QDialog()
    ui = Ui_about_radiation()
    ui.setupUi(about_radiation)
    about_radiation.show()



def open_calendar():
    global Dialog3
    Dialog3 = QtWidgets.QDialog()
    ui = Ui_Dialog3()
    ui.setupUi(Dialog3)
    Dialog3.show()



def open_graf():
    global Dialog4
    Dialog4 = QtWidgets.QDialog()
    ui = Ui_Dialog4()
    ui.setupUi(Dialog4)
    Dialog4.show()



def open_wikipedia():
    url = QUrl("https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%80%D0%B0%D0%B4%D0%B8%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D1%85_%D0%B0%D0%B2%D0%B0%D1%80%D0%B8%D0%B9")
    QDesktopServices.openUrl(url)



def open_mchs():
    mchs_url = QUrl('https://api.whatsapp.com/send?phone=996556112000')
    QDesktopServices.openUrl(mchs_url)



def dialog_input():
    global Dialog7
    Dialog7 = QtWidgets.QDialog()
    ui = Ui_Dialog7()
    ui.setupUi(Dialog7)
    Dialog7.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle('Radiation Zone')
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
