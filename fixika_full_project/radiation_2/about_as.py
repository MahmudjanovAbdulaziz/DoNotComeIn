from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(851, 620)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(7, 219, 173, 1), stop:0.427447 rgba(7, 219, 35, 1), stop:1 rgba(7, 219, 184, 1));")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 131, 31))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid(255, 255, 255, 40);\n"
"border-radius:7px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 30, 191, 31))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid(255, 255, 255, 40);\n"
"border-radius:7px;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 60, 131, 31))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid(255, 255, 255, 40);\n"
"border-radius:7px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(0, 90, 151, 51))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid(255, 255, 255, 40);\n"
"border-radius:7px;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(0, 140, 831, 51))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid(255, 255, 255, 40);\n"
"border-radius:7px;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(0, 190, 131, 20))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid(255, 255, 255, 40);\n"
"border-radius:7px;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(0, 210, 131, 20))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
"border: 1px solid(255, 255, 255, 40);\n"
"border-radius:7px;")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "about_as"))
        self.label.setText(_translate("Dialog", "Прогамму делал:"))
        self.label_2.setText(_translate("Dialog", "Махмуджанов Абдулазиз Зафарович"))
        self.label_3.setText(_translate("Dialog", "Руководители:"))
        self.label_4.setText(_translate("Dialog", "Чолпонай Дженалиевна \n"
"Феруза Расуловна"))
        self.label_5.setText(_translate("Dialog", "Коротко о программе:  Программа была написана на языке програмирование Python на библиотеке PyQt5 а дизайн и \n"
"внешний вид был создан QtDesigner фон цвет внешний вид программы был создан благодаря сайтам где есть подсказки c (rgba)"))
        self.label_6.setText(_translate("Dialog", "Помогал:"))
        self.label_7.setText(_translate("Dialog", "Маклаков Никита"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog2 = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())
