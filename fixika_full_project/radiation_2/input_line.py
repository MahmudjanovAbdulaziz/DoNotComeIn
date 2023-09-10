from PyQt5 import QtCore, QtGui, QtWidgets
from grafik import Ui_Dialog6
import webbrowser


class Ui_Dialog7(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(950, 734)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(232, 107, 12, 1), stop:0.427447 rgba(12, 221, 232, 1), stop:1 rgba(92, 12, 232, 1));")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(129, 0, 661, 731))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(126, 12, 232, 1), stop:0.427447 rgba(59, 232, 12, 1), stop:1 rgba(221, 232, 12, 1));\n"
"border-radius:100px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.cislorod = QtWidgets.QLineEdit(self.frame)
        self.cislorod.setGeometry(QtCore.QRect(300, 90, 301, 31))
        self.cislorod.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: rgb(255, 0, 255);")
        self.cislorod.setObjectName("cislorod")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 90, 241, 31))
        self.label.setStyleSheet("font: italic 10pt \"Arial\";\n"
"background-color: rgb(16, 251, 255, 90);\n"
"border: 1px solid rgba(255, 255, 255, 10);\n"
"border-radius: 17px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(40, 130, 241, 31))
        self.label_2.setStyleSheet("font: italic 10pt \"Arial\";\n"
"background-color: rgb(16, 251, 255, 90);\n"
"border: 1px solid rgba(255, 255, 255, 10);\n"
"border-radius: 17px;")
        self.label_2.setObjectName("label_2")
        self.azot = QtWidgets.QLineEdit(self.frame)
        self.azot.setGeometry(QtCore.QRect(300, 130, 301, 31))
        self.azot.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: rgb(255, 0, 255);")
        self.azot.setObjectName("azot")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 241, 31))
        self.label_3.setStyleSheet("font: italic 10pt \"Arial\";\n"
"background-color: rgb(16, 251, 255, 90);\n"
"border: 1px solid rgba(255, 255, 255, 10);\n"
"border-radius: 17px;")
        self.label_3.setObjectName("label_3")
        self.carbon_gaz = QtWidgets.QLineEdit(self.frame)
        self.carbon_gaz.setGeometry(QtCore.QRect(300, 170, 301, 31))
        self.carbon_gaz.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: rgb(255, 0, 255);")
        self.carbon_gaz.setObjectName("carbon_gaz")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(40, 210, 241, 31))
        self.label_7.setStyleSheet("font: italic 10pt \"Arial\";\n"
"background-color: rgb(16, 251, 255, 90);\n"
"border: 1px solid rgba(255, 255, 255, 10);\n"
"border-radius: 17px;")
        self.label_7.setObjectName("label_7")
        self.argon = QtWidgets.QLineEdit(self.frame)
        self.argon.setGeometry(QtCore.QRect(300, 210, 301, 31))
        self.argon.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: rgb(255, 0, 255);")
        self.argon.setObjectName("argon")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(40, 250, 241, 31))
        self.label_8.setStyleSheet("font: italic 10pt \"Arial\";\n"
"background-color: rgb(16, 251, 255, 90);\n"
"border: 1px solid rgba(255, 255, 255, 10);\n"
"border-radius: 17px;")
        self.label_8.setObjectName("label_8")
        self.ksenon = QtWidgets.QLineEdit(self.frame)
        self.ksenon.setGeometry(QtCore.QRect(300, 250, 301, 31))
        self.ksenon.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: rgb(255, 0, 255);")
        self.ksenon.setObjectName("ksenon")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(40, 290, 241, 31))
        self.label_9.setStyleSheet("font: italic 10pt \"Arial\";\n"
"background-color: rgb(16, 251, 255, 90);\n"
"border: 1px solid rgba(255, 255, 255, 10);\n"
"border-radius: 17px;")
        self.label_9.setObjectName("label_9")
        self.kripton = QtWidgets.QLineEdit(self.frame)
        self.kripton.setGeometry(QtCore.QRect(300, 290, 301, 31))
        self.kripton.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: rgb(255, 0, 255);")
        self.kripton.setObjectName("kripton")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(40, 330, 241, 31))
        self.label_10.setStyleSheet("font: italic 10pt \"Arial\";\n"
"background-color: rgb(16, 251, 255, 90);\n"
"border: 1px solid rgba(255, 255, 255, 10);\n"
"border-radius: 17px;")
        self.label_10.setObjectName("label_10")
        self.radiation = QtWidgets.QLineEdit(self.frame)
        self.radiation.setGeometry(QtCore.QRect(300, 330, 301, 31))
        self.radiation.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: rgb(255, 0, 255);")
        self.radiation.setObjectName("radiation")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(40, 370, 241, 31))
        self.label_11.setStyleSheet("font: italic 10pt \"Arial\";\n"
"background-color: rgb(16, 251, 255, 90);\n"
"border: 1px solid rgba(255, 255, 255, 10);\n"
"border-radius: 17px;")
        self.label_11.setObjectName("label_11")
        self.Vodorod = QtWidgets.QLineEdit(self.frame)
        self.Vodorod.setGeometry(QtCore.QRect(300, 370, 301, 31))
        self.Vodorod.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"color: rgb(255, 0, 255);")
        self.Vodorod.setObjectName("Vodorod")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(230, 50, 181, 21))
        self.label_12.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: rgb(255, 240, 17б 70);\n"
"border: 1px solid rgb(85, 255, 255, 20);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_12.setObjectName("label_12")
        self.btn_graf_give = QtWidgets.QPushButton(self.frame)
        self.btn_graf_give.setGeometry(QtCore.QRect(300, 410, 301, 31))
        self.btn_graf_give.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: rgb(255, 240, 17б 70);\n"
"border: 1px solid rgb(85, 255, 255, 40);\n"
"color: rgb(0, 0, 0);\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/analize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_graf_give.setIcon(icon)
        self.btn_graf_give.setObjectName("btn_graf_give")
        self.btn_graf_give.clicked.connect(self.grafik)
        self.send_mchs_btn = QtWidgets.QPushButton(self.frame)
        self.send_mchs_btn.setGeometry(QtCore.QRect(300, 450, 301, 31))
        self.send_mchs_btn.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: rgb(255, 240, 17б 70);\n"
"border: 1px solid rgb(85, 255, 255, 40);\n"
"color: rgb(0, 0, 0);\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/send.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_mchs_btn.setIcon(icon1)
        self.send_mchs_btn.setObjectName("send_mchs_btn")
        self.send_mchs_btn.clicked.connect(self.open_mchs)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ввод данных для построение графика "))
        self.label.setText(_translate("Dialog", "Кислород"))
        self.label_2.setText(_translate("Dialog", "Азот"))
        self.label_3.setText(_translate("Dialog", "Углекислый  газ"))
        self.label_7.setText(_translate("Dialog", "Аргон"))
        self.label_8.setText(_translate("Dialog", "Ксенон"))
        self.label_9.setText(_translate("Dialog", "Криптон"))
        self.label_10.setText(_translate("Dialog", "Радиация"))
        self.label_11.setText(_translate("Dialog", "Водород"))
        self.label_12.setText(_translate("Dialog", "         Для графика"))
        self.btn_graf_give.setText(_translate("Dialog", "Получить график:"))
        self.send_mchs_btn.setText(_translate("Dialog", "Отправить сообщение МЧС:"))

    def grafik(self):
        global Dialog6
        Dialog6 = QtWidgets.QDialog()
        ui = Ui_Dialog6()
        ui.setupUi(Dialog6)
        Dialog6.show()

    def open_mchs(self):
        phone_number = '+996 556 112 000'

        whatsapp_url = f'https://api.whatsapp.com/send?phone=996556112000'

        webbrowser.open(whatsapp_url)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog7 = QtWidgets.QDialog()
    ui = Ui_Dialog7()
    ui.setupUi(Dialog7)
    Dialog7.show()
    sys.exit(app.exec_())
